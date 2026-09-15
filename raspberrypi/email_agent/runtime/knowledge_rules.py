"""
knowledge_rules.py
Curated Domain & Keyword Seed Knowledge Datasets for Pi-loop Email Intelligence.
Provides deterministic, high-accuracy Tier-2 classification prior to LLM inference.
"""

import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class SeedRuleMatch:
    category: str
    priority: str
    action_needed: bool
    action_type: str
    auto_archive: bool
    reason: str


# ── Curated Domain Dictionaries ───────────────────────────────────────────────

# 1. Shopping / Retail / E-commerce Brands
SHOPPING_DOMAINS = {
    "hm.com", "email.hm.com",
    "skechers.com", "emails.skechers.com",
    "underarmour.com", "emails.underarmour.com",
    "shein.com", "email.us.shein.com",
    "amazon.com", "marketplace.amazon.com",
    "ebay.com", "ebay.co.uk",
    "target.com", "target.scene7.com",
    "walmart.com", "email.walmart.com",
    "bestbuy.com", "emailinfo.bestbuy.com",
    "nike.com", "nike.com.au",
    "adidas.com", "news.adidas.com",
    "zara.com", "itx.zara.com",
    "uniqlo.com", "email.uniqlo.com",
    "nordstrom.com", "e.nordstrom.com",
    "sephora.com", "shop.sephora.com",
    "ulta.com", "e.ulta.com",
    "gap.com", "oldnavy.com", "bananarepublic.com",
    "costco.com", "online.costco.com",
    "homedepot.com", "orders.homedepot.com",
    "lowes.com", "ikea.com",
    "etsy.com", "mail.etsy.com",
    "wayfair.com", "newegg.com",
    "aliexpress.com", "temu.com",
    "babbel.com", "chewy.com",
    "lululemon.com", "asos.com",
    "craftdlondon.com", "trueclassictees.com", "fabletics.com",
}

# 2. Finance / Banking / Fintech / Invoicing
FINANCE_DOMAINS = {
    "chase.com", "alerts.chase.com",
    "bankofamerica.com", "bofa.com",
    "wellsfargo.com", "wellsfargoemail.com",
    "citi.com", "citibank.com",
    "americanexpress.com", "amex.com",
    "discover.com", "discovercard.com",
    "capitalone.com", "capitalone.messages.com",
    "fidelity.com", "vanguard.com", "schwab.com",
    "paypal.com", "intl.paypal.com", "stripe.com",
    "square.com", "squareup.com", "venmo.com",
    "sofi.com", "robinhood.com", "coinbase.com",
    "turbotax.intuit.com", "intuit.com",
    "mint.com", "creditkarma.com", "experian.com",
    "equifax.com", "transunion.com",
}

# 3. Travel / Airlines / Hotels / Transport
TRAVEL_DOMAINS = {
    "united.com", "unitedairlines.com",
    "delta.com", "deltaairlines.com",
    "aa.com", "americanairlines.com",
    "southwest.com", "southwestairlines.com",
    "alaskaair.com", "jetblue.com",
    "singaporeair.com", "emirates.com", "qantas.com",
    "airbnb.com", "vrbo.com", "booking.com",
    "expedia.com", "hotels.com", "kayak.com", "priceline.com",
    "marriott.com", "hilton.com", "hyatt.com",
    "uber.com", "lyft.com", "lyftmail.com",
    "amtrak.com", "hertz.com", "enterprise.com",
}

# 4. Work Infrastructure / Developer Platforms
WORK_DOMAINS = {
    "github.com", "gitlab.com", "bitbucket.org",
    "jira.com", "atlassian.com", "confluence.atlassian.net",
    "linear.app", "notion.so", "asana.com", "trello.com",
    "slack.com", "slack-msgs.com",
    "amazon.com/aws", "aws.amazon.com", "amazonaws.com",
    "cloud.google.com", "google.com/cloud",
    "azure.com", "microsoft365.com",
    "datadoghq.com", "sentry.io", "pagerduty.com",
    "cloudflare.com", "digitalocean.com", "heroku.com",
    "docker.com", "npm.org", "pypi.org",
}

# 5. Curated Tech Publications & Newsletters
TECH_NEWSLETTER_DOMAINS = {
    "substack.com", "medium.com", "tldr.tech",
    "bytebytego.com", "hackernewsletter.com",
    "morningbrew.com", "thehustle.co", "theverge.com",
    "wired.com", "arstechnica.com", "bloomberg.com",
    "economist.com", "wsj.com", "nytimes.com",
    "balsamiq.com", "pocket.com", "educative.io",
    "signaturely.com", "devpost.com",
}

# 6. Security / Authentication Platforms
SECURITY_DOMAINS = {
    "accounts.google.com", "appleid.apple.com", "account.microsoft.com",
    "okta.com", "auth0.com", "1password.com", "bitwarden.com",
    "duomobile.com", "authy.com", "yubico.com",
}

# 7. Social Network Notifications & Social Updates
SOCIAL_NETWORK_DOMAINS = {
    "facebookmail.com", "facebook.com",
    "linkedin.com", "e.linkedin.com",
    "instagram.com", "mail.instagram.com",
    "twitter.com", "x.com",
    "pinterest.com", "redditmail.com", "tiktok.com",
}



# ── Pattern Matchers ─────────────────────────────────────────────────────────

# High-confidence subject/body patterns
SHOPPING_PATTERNS = [
    r"\b\d+%\s*off\b", r"\bflash sale\b", r"\bclearance\b", r"\bdoorbuster\b",
    r"\bfree shipping\b", r"\byour order (?:has shipped|is confirmed|has been placed)\b",
    r"\border confirmation\b", r"\btracking number\b", r"\bpackage delivered\b",
    r"\bitem(?:s)? in your cart\b", r"\bexclusive discount\b", r"\bpromo code\b",
    r"\bweekend sale\b", r"\bbuy (?:one|1) get (?:one|1)\b", r"\bbogo\b",
]

FINANCE_PATTERNS = [
    r"\bstatement is ready\b", r"\bpayment (?:received|processed|due|scheduled)\b",
    r"\btransaction alert\b", r"\bdirect deposit\b", r"\bwire transfer\b",
    r"\baccount summary\b", r"\btax document\b", r"\bform 1099\b", r"\bform w-2\b",
    r"\bavailable balance\b", r"\bminimum payment\b", r"\bcredit score update\b",
]

TRAVEL_PATTERNS = [
    r"\bflight (?:confirmation|status|delayed|cancelled|boarding)\b",
    r"\bboarding pass\b", r"\bhotel reservation\b", r"\bcheck-in reminder\b",
    r"\bitinerary\b", r"\bcar rental confirmation\b", r"\bticket confirmation\b",
]

SECURITY_PATTERNS = [
    r"\bverification code\b", r"\bsecurity code\b", r"\bpassword reset\b",
    r"\bnew login from\b", r"\bunfamiliar device\b", r"\btwo-factor authentication\b",
    r"\b2fa code\b", r"\bsecurity alert\b", r"\bsuspicious activity\b",
]


def extract_domain(sender: str) -> str:
    """Extract root/subdomain from email sender address."""
    match = re.search(r"@([\w.-]+)", sender.lower())
    if not match:
        return ""
    return match.group(1)


def is_subdomain_of(domain: str, parent: str) -> bool:
    """Check if domain is or ends with parent domain."""
    return domain == parent or domain.endswith("." + parent)


def match_seed_knowledge(sender: str, subject: str, body: str = "") -> Optional[SeedRuleMatch]:
    """
    Tier-2 Classification: Matches curated domain and keyword seed knowledge.
    Returns SeedRuleMatch if high-confidence match is found, otherwise None.
    """
    sender_lower = sender.lower()
    subject_lower = subject.lower()
    text = f"{subject_lower} {body[:500].lower()}"
    domain = extract_domain(sender_lower)

    # 1. Security Alerts (Highest Priority)
    is_security_domain = any(is_subdomain_of(domain, d) for d in SECURITY_DOMAINS)
    has_security_pattern = any(re.search(p, text) for p in SECURITY_PATTERNS)
    if is_security_domain or (has_security_pattern and ("code" in text or "login" in text or "alert" in text)):
        return SeedRuleMatch(
            category="Work" if "work" in text else "Personal",
            priority="URGENT",
            action_needed=True,
            action_type="Review",
            auto_archive=False,
            reason=f"Security/auth alert detected from {domain or sender[:30]}",
        )

    # 2. Finance / Banking
    is_finance_domain = any(is_subdomain_of(domain, d) for d in FINANCE_DOMAINS)
    has_finance_pattern = any(re.search(p, text) for p in FINANCE_PATTERNS)
    if is_finance_domain or has_finance_pattern:
        is_urgent = bool(re.search(r"\b(past due|overdue|fraud alert|immediate action|unauthorized)\b", text))
        return SeedRuleMatch(
            category="Finance",
            priority="URGENT" if is_urgent else "IMPORTANT" if is_finance_domain else "NORMAL",
            action_needed=is_urgent or bool(re.search(r"\b(payment due|pay by|due on|action required)\b", text)),
            action_type="Pay" if "payment" in text or "due" in text else "Review",
            auto_archive=False,
            reason=f"Financial transaction/statement from {domain or sender[:30]}",
        )

    # 3. Travel Confirmations & Itineraries
    is_travel_domain = any(is_subdomain_of(domain, d) for d in TRAVEL_DOMAINS)
    has_travel_pattern = any(re.search(p, text) for p in TRAVEL_PATTERNS)
    if is_travel_domain or has_travel_pattern:
        return SeedRuleMatch(
            category="Travel",
            priority="IMPORTANT" if ("boarding" in text or "check-in" in text or "today" in text) else "NORMAL",
            action_needed=bool("check-in" in text or "action required" in text),
            action_type="Review",
            auto_archive=False,
            reason=f"Travel itinerary/booking from {domain or sender[:30]}",
        )

    # 4. Shopping / Retail E-Commerce
    is_shopping_domain = any(is_subdomain_of(domain, d) for d in SHOPPING_DOMAINS)
    has_shopping_pattern = any(re.search(p, text) for p in SHOPPING_PATTERNS)
    if is_shopping_domain or has_shopping_pattern:
        is_order = bool(re.search(r"\b(order confirmation|tracking|shipped|delivered|receipt)\b", text))
        return SeedRuleMatch(
            category="Shopping",
            priority="NORMAL" if is_order else "LOW",
            action_needed=False,
            action_type="None",
            auto_archive=not is_order,
            reason=f"E-commerce/retail match: {domain or sender[:30]}",
        )

    # 5. Work Infrastructure & Dev Platforms
    is_work_domain = any(is_subdomain_of(domain, d) for d in WORK_DOMAINS)
    if is_work_domain:
        has_mention = bool(re.search(r"\b(assigned to you|requested your review|mentioned you|failed build|pipeline failed)\b", text))
        return SeedRuleMatch(
            category="Work",
            priority="IMPORTANT" if has_mention else "NORMAL",
            action_needed=has_mention,
            action_type="Review" if has_mention else "None",
            auto_archive=False,
            reason=f"Work/developer platform notification from {domain}",
        )

    # 6. Tech Newsletters & Publications
    is_newsletter_domain = any(is_subdomain_of(domain, d) for d in TECH_NEWSLETTER_DOMAINS)
    if is_newsletter_domain:
        return SeedRuleMatch(
            category="Newsletter",
            priority="LOW",
            action_needed=False,
            action_type="None",
            auto_archive=True,
            reason=f"Curated tech publication/newsletter from {domain}",
        )

    # 7. Social Network Notifications (Friend suggestions, stories, photo updates, group digests)
    is_social_domain = any(is_subdomain_of(domain, d) for d in SOCIAL_NETWORK_DOMAINS)
    if is_social_domain:
        # Check if it's an explicit critical security alert from the platform
        is_platform_security = "security@" in sender_lower or any(p in subject_lower for p in ("reset password", "security alert", "suspicious login"))
        if is_platform_security:
            return SeedRuleMatch(
                category="Personal",
                priority="IMPORTANT",
                action_needed=True,
                action_type="Review",
                auto_archive=False,
                reason=f"Social account security alert from {domain}",
            )
        # Direct person-to-person messages via messenger/DM vs automated passive activity
        is_direct_msg = "messages@" in sender_lower or "sent a message" in subject_lower
        return SeedRuleMatch(
            category="Personal",
            priority="NORMAL" if is_direct_msg else "LOW",
            action_needed=False,
            action_type="None",
            auto_archive=not is_direct_msg,
            reason=f"Social network automated notification from {domain}",
        )

    return None

