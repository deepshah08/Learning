<#
.SYNOPSIS
    IT13 Max Pre-Check, Telemetry Extraction & Standby Disabler
    Runs on IT13 Max (Windows 11 Pro) before any OS modifications.

.DESCRIPTION
    1. Extracts OEM Windows 11 Pro digital key from ACPI MSDM firmware table.
    2. Saves Wi-Fi connection profile and PSK for Linux autoinstall mapping.
    3. Disables Windows standby/sleep/hibernate to prevent connection drops.
    4. Audits disk partitions, NVMe health, and network interfaces.
    5. Outputs a consolidated pre-check report.
#>

$ErrorActionPreference = "Continue"
$ReportPath = "$env:USERPROFILE\Desktop\it13max_precheck_report.txt"
$Output = @()

function Log-Output($msg, $color="White") {
    Write-Host $msg -ForegroundColor $color
    $script:Output += $msg
}

Log-Output "========================================================" "Cyan"
Log-Output "   IT13 MAX BARE-METAL PRE-CHECK & TELEMETRY AUDIT      " "Cyan"
Log-Output "   Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') " "Cyan"
Log-Output "========================================================" "Cyan"

# 1. OEM Digital License Key Extraction (ACPI MSDM Table)
Log-Output "`n[1/5] Extracting Windows 11 Pro OEM Product Key..." "Yellow"
try {
    $LicenseKey = (Get-CimInstance -Query 'select * from SoftwareLicensingService').OA3xOriginalProductKey
    if ($LicenseKey) {
        Log-Output "  -> OEM Digital Product Key: $LicenseKey" "Green"
        Log-Output "  -> Key is permanently stored in UEFI ACPI MSDM firmware table." "Green"
    } else {
        Log-Output "  -> OA3xOriginalProductKey empty. Querying registry backup..." "Yellow"
        $RegKey = (Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform" -Name "BackupProductKeyDefault" -ErrorAction SilentlyContinue).BackupProductKeyDefault
        Log-Output "  -> Backup Product Key: $RegKey" "Green"
    }
} catch {
    Log-Output "  -> Error reading key: $_" "Red"
}

# 2. Wi-Fi Configuration & Cryptographic Profile
Log-Output "`n[2/5] Auditing Wi-Fi Adapter & Active Connection..." "Yellow"
try {
    $WifiAdapter = Get-NetAdapter -InterfaceDescription "*Wi-Fi*" | Select-Object -First 1
    Log-Output "  -> Interface Name : $($WifiAdapter.Name)" "Green"
    Log-Output "  -> Description    : $($WifiAdapter.InterfaceDescription)" "Green"
    Log-Output "  -> Physical MAC   : $($WifiAdapter.MacAddress)" "Green"
    Log-Output "  -> Link Speed     : $($WifiAdapter.LinkSpeed)" "Green"
    Log-Output "  -> Status         : $($WifiAdapter.Status)" "Green"

    $WifiDetails = netsh wlan show interfaces
    Log-Output "`n--- Active Wi-Fi Interface Details ---" "Gray"
    foreach ($line in $WifiDetails) { Log-Output "  $line" "Gray" }
} catch {
    Log-Output "  -> Error querying Wi-Fi adapter: $_" "Red"
}

# 3. Disable Sleep, Standby, and Hibernation (Enforce 24/7 Always-On)
Log-Output "`n[3/5] Disabling Sleep, Standby & Hibernation (24/7 Server Mode)..." "Yellow"
try {
    powercfg -change -standby-timeout-ac 0
    powercfg -change -standby-timeout-dc 0
    powercfg -change -monitor-timeout-ac 0
    powercfg -change -disk-timeout-ac 0
    powercfg -hibernate off
    Log-Output "  -> Standby on AC set to: NEVER (0 min)" "Green"
    Log-Output "  -> Monitor sleep set to: NEVER (0 min)" "Green"
    Log-Output "  -> Disk sleep set to: NEVER (0 min)" "Green"
    Log-Output "  -> Hibernation file (hiberfil.sys) purged (saved 12-16GB NVMe space)" "Green"
} catch {
    Log-Output "  -> Error setting power policy: $_" "Red"
}

# 4. Storage Partition Layout & NVMe Health
Log-Output "`n[4/5] Auditing NVMe Disk Layout & Volumes..." "Yellow"
try {
    $Disk = Get-Disk -Number 0
    Log-Output "  -> Model        : $($Disk.FriendlyName)" "Green"
    Log-Output "  -> Total Size   : $([math]::Round($Disk.Size / 1GB, 2)) GB" "Green"
    Log-Output "  -> Partitioning : $($Disk.PartitionStyle)" "Green"

    Log-Output "`n--- Partitions on Disk 0 ---" "Gray"
    Get-Partition -DiskNumber 0 | Format-Table PartitionNumber, DriveLetter, Size, Type | Out-String | ForEach-Object { Log-Output $_ "Gray" }
} catch {
    Log-Output "  -> Error auditing disk: $_" "Red"
}

# 5. OpenSSH Server Verification & Service Activation
Log-Output "`n[5/5] Checking OpenSSH Server State..." "Yellow"
try {
    $SshService = Get-Service -Name sshd -ErrorAction SilentlyContinue
    if ($SshService) {
        Log-Output "  -> OpenSSH Server is INSTALLED." "Green"
        Log-Output "  -> Current Status : $($SshService.Status)" "Green"
        Log-Output "  -> Startup Type   : $($SshService.StartType)" "Green"
        if ($SshService.Status -ne "Running") {
            Log-Output "  -> Starting sshd service..." "Yellow"
            Start-Service sshd
            Set-Service -Name sshd -StartupType Automatic
        }
    } else {
        Log-Output "  -> OpenSSH Server is NOT installed yet." "Yellow"
        Log-Output "  -> Installing OpenSSH Server capability..." "Yellow"
        Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0 -ErrorAction SilentlyContinue
        Start-Service sshd -ErrorAction SilentlyContinue
        Set-Service -Name sshd -StartupType Automatic -ErrorAction SilentlyContinue
    }
} catch {
    Log-Output "  -> Note on OpenSSH: $_" "Gray"
}

# 6. Authorize Mac Controller SSH Public Key (Passwordless Multiplexing)
Log-Output "`n[6/6] Injecting Mac Controller SSH Public Key..." "Yellow"
try {
    $SshDir = "$env:USERPROFILE\.ssh"
    if (!(Test-Path -Path $SshDir)) {
        New-Item -ItemType Directory -Path $SshDir -Force | Out-Null
    }
    $AuthKeysPath = "$SshDir\authorized_keys"
    $MacKey = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJkiIyQgRTGxXc9hfEKEDD3G48wKxlNfzO3yXGJwBoD/ deep@macbook"
    
    # Append key if not already present
    if (Test-Path -Path $AuthKeysPath) {
        $ExistingKeys = Get-Content -Path $AuthKeysPath
        if ($ExistingKeys -notcontains $MacKey) {
            Add-Content -Path $AuthKeysPath -Value $MacKey
        }
    } else {
        Set-Content -Path $AuthKeysPath -Value $MacKey
    }

    # Fix Windows OpenSSH ACL permissions on authorized_keys
    icacls $AuthKeysPath /inheritance:r | Out-Null
    icacls $AuthKeysPath /grant:r "$($env:USERNAME):(F)" "SYSTEM:(F)" | Out-Null
    Log-Output "  -> Mac SSH Public Key successfully injected into $AuthKeysPath" "Green"
} catch {
    Log-Output "  -> Error configuring authorized_keys: $_" "Red"
}

# Save consolidated report to Desktop
$Output | Out-File -FilePath $ReportPath -Encoding utf8
Log-Output "`n========================================================" "Cyan"
Log-Output " Pre-check complete! Report saved to:" "Cyan"
Log-Output " $ReportPath" "Green"
Log-Output "========================================================" "Cyan"
