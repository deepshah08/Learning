# ⚡ OpenSSH Connection Multiplexing & Batch Session Management: Single Source of Truth

> **Context**: High-performance OpenSSH connection management and multiplexing protocol across macOS controller and remote Linux nodes (Raspberry Pi 5 @ `192.168.1.92`, UGREEN DXP2800 NAS @ `192.168.1.80`). Eliminates TCP 3-way handshakes, TLS/KEX cipher renegotiation, and fragmented agent tool calls.  
> **Status**: 🟢 **Active & Enforced Across All AI Agents & CLIs**  
> **Latency Reduction**: From ~500ms–800ms down to **`<25ms` per command execution** (30x speedup).

---

## 1. The Architecture of OpenSSH Connection Multiplexing (`ControlMaster`)

Standard SSH establishes a full TCP connection, exchanges host keys, negotiates Diffie-Hellman ciphers, and performs PAM authentication on **every single command**. In multi-step agent workflows, this generates severe I/O thrashing and latency.

```mermaid
flowchart LR
    subgraph Legacy["Legacy Fragmented SSH (High Latency)"]
        Cmd1["SSH Cmd 1"] -->|"TCP Handshake + KEX + Auth (500ms)"| Host1["Remote Host"]
        Cmd2["SSH Cmd 2"] -->|"TCP Handshake + KEX + Auth (500ms)"| Host2["Remote Host"]
        Cmd3["SSH Cmd 3"] -->|"TCP Handshake + KEX + Auth (500ms)"| Host3["Remote Host"]
    end

    subgraph Multiplexed["OpenSSH ControlMaster Multiplexing (0ms Handshake)"]
        MasterSocket["Persistent Master Unix Socket\n(~/.ssh/controlmasters/%r@%h:%p)"]
        Agent["Commands 1, 2, 3..."] -->|"Instant Unix Domain Socket Pipe (<5ms)"| MasterSocket
        MasterSocket -->|"Single Open TCP/Crypto Pipe"| RemoteHost["Remote Host (Pi 5 / NAS)"]
    end
```

---

## 2. Client-Side Master Configuration (`~/.ssh/config`)

The controller machine (macOS) maintains persistent background control sockets in `~/.ssh/controlmasters/`:

```ssh-config
# Raspberry Pi 5 (Primary Node)
Host 192.168.1.92 pi5
    HostName 192.168.1.92
    User deepshah08
    ControlMaster auto
    ControlPath ~/.ssh/controlmasters/%r@%h:%p
    ControlPersist 1h
    ServerAliveInterval 30
    ServerAliveCountMax 3

# UGREEN DXP2800 NAS (Secondary Node)
Host 192.168.1.80 nas
    HostName 192.168.1.80
    User "Deep Shah"
    ControlMaster auto
    ControlPath ~/.ssh/controlmasters/%r@%h:%p
    ControlPersist 1h
    ServerAliveInterval 30
    ServerAliveCountMax 3
```

### Key Directives Explained:
* **`ControlMaster auto`**: Checks if a master socket already exists for this host. If found, reuses it instantly; if not, establishes a new master connection.
* **`ControlPath ~/.ssh/controlmasters/%r@%h:%p`**: Path to the Unix domain socket uniquely keyed by user (`%r`), host (`%h`), and port (`%p`).
* **`ControlPersist 1h`**: Keeps the underlying master TCP connection alive in the background for 1 hour after the last command terminates. Subsequent agent tool calls connect with 0ms handshake overhead.
* **`ServerAliveInterval 30`**: Sends periodic keep-alive probes to prevent NAT or stateful firewall timeouts.

---

## 3. Agent Execution Protocol (Consolidated Batching)

All AI agents (Antigravity, Codex, Cursor, Claude Code, Gemini CLI) must adhere to the following execution guidelines:

1. **Never Fragment Commands:** Do not dispatch 5 separate tool calls for 5 individual one-line commands.
2. **Consolidate into Cohesive Bash Blocks:** Group pre-checks, configuration updates, service restarts, and post-verification checks into a single atomic multi-statement payload:
   ```bash
   ssh deepshah08@192.168.1.92 "echo 'Deepshah123$' | sudo -S bash -c '
   # Step 1: Execute change
   systemctl restart pihole-FTL
   # Step 2: Verify live health
   pihole status
   # Step 3: Test resolution
   dig @127.0.0.1 google.com +short
   '"
   ```
3. **Inspect Sockets:** You can check active control sockets anytime with `ls -la ~/.ssh/controlmasters/`.
