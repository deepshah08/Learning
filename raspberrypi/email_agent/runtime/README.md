# Pi-loop Email Agent Runtime Snapshot

This directory is the shareable source snapshot for the Pi-loop Email
Intelligence Agent deployed at `/home/deepshah08/email-agent` on the Raspberry
Pi 5. It complements the architecture and operational history in the parent
[`README.md`](../README.md) and [`CODEX_HANDOFF.md`](../CODEX_HANDOFF.md).

The snapshot includes the Python runtime, tests, systemd unit templates,
configuration example, dependency manifest, and the measured resource ledger.
It intentionally excludes Gmail databases, logs, OAuth files, bot tokens,
API keys, virtual environments, model weights, and generated caches.

Validation recorded before publication:

- Local unit, accuracy, and five-iteration challenge suites passed.
- Pi-side unit checks passed after deployment.
- Latest production run processed 15/15 messages in 145.7 seconds with no
  resource-budget overage.
- The historical 900-second ingestion failure remains documented in
  `RESOURCE_BUDGET.md`.

The systemd templates are references for deployment; the live Pi may contain
host-specific drop-ins and credentials outside this directory.
