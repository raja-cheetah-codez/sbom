```regex
██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
```

[![Cybersecurity Projects](https://img.shields.io/badge/Cybersecurity--Projects-Project%20%2324-red?style=flat&logo=github)](https://github.com/CarterPerez-dev/Cybersecurity-Projects/tree/main/PROJECTS/intermediate/sbom-generator-vulnerability-matcher)
[![Go](https://img.shields.io/badge/Go-1.25-00ADD8?style=flat&logo=go&logoColor=white)](https://go.dev)
[![License: AGPLv3](https://img.shields.io/badge/License-AGPL_v3-purple.svg)](https://www.gnu.org/licenses/agpl-3.0)

> SBOM generator and vulnerability matcher that scans Go, Node.js, and Python projects, produces SPDX 2.3 and CycloneDX 1.5 documents, and cross-references packages against OSV and NVD vulnerability databases.

*This is a quick overview — security theory, architecture, and full walkthroughs are in the [learn modules](#learn).*

## What It Does

- Multi-ecosystem dependency scanning (Go `go.mod`/`go.sum`, Node.js `package.json`/`pnpm-lock.yaml`, Python `pyproject.toml`/`uv.lock`)
- Dependency graph construction with cycle detection and depth tracking
- SBOM generation in SPDX 2.3 and CycloneDX 1.5 JSON formats
- Vulnerability matching via OSV batch API (primary) and NVD REST API (optional)
- SQLite-backed response cache with configurable TTL
- Policy engine for CI/CD gates with severity thresholds and dependency depth limits
- Monorepo support with recursive ecosystem detection

## Quick Start

```bash
go install github.com/CarterPerez-dev/bomber/cmd/bomber@latest
```

Or use the install script:

```bash
curl -fsSL https://raw.githubusercontent.com/CarterPerez-dev/Cybersecurity-Projects/main/PROJECTS/intermediate/sbom-generator-vulnerability-matcher/install.sh | bash
```

> [!TIP]
> This project uses [`just`](https://github.com/casey/just) as a command runner. Type `just` to see all available commands.
>
> Install: `curl -sSf https://just.systems/install.sh | bash -s -- --to ~/.local/bin`

### Usage

```bash
bomber scan ./my-project                           # scan dependencies
bomber generate ./my-project --format spdx         # SPDX 2.3 SBOM
bomber generate ./my-project --format cyclonedx    # CycloneDX 1.5 SBOM
bomber vuln ./my-project                           # vulnerability scan
bomber check ./my-project --policy policy.yaml     # CI/CD policy gate
```

### Policy File

```yaml
max_severity: medium
max_depth: 5
```

`bomber check` exits with code 1 when violations are found — drop it into any CI pipeline.

## Supported Ecosystems

| Ecosystem | Manifest | Lockfile |
|-----------|----------|----------|
| Go | `go.mod` | `go.sum` |
| Node.js | `package.json` | `pnpm-lock.yaml` |
| Python | `pyproject.toml` | `uv.lock` |

## Architecture

```
bomber scan ./project/

┌─────────────────────────────────────────────────┐
│                   CLI (cobra)                   │
│  scan • generate • vuln • check                 │
└──────────────────────┬──────────────────────────┘
                       │
         ┌─────────────▼─────────────┐
         │     Scanner Engine        │
         │  walks dir, detects       │
         │  ecosystems, dispatches   │
         └─────────────┬─────────────┘
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
   ┌─────────┐   ┌─────────┐   ┌─────────┐
   │Go Parser│   │Node     │   │Python   │
   │go.mod   │   │pnpm-lock│   │uv.lock  │
   │go.sum   │   │pkg.json │   │pyproject│
   └────┬────┘   └────┬────┘   └────┬────┘
        │              │              │
        └──────────────┼──────────────┘
                       ▼
         ┌─────────────────────────┐
         │   Dependency Graph      │
         │  direct + transitive    │
         │  cycle detection        │
         └────────────┬────────────┘
                      │
            ┌─────────┼─────────┐
            ▼                   ▼
   ┌──────────────┐   ┌──────────────┐
   │ SPDX 2.3     │   │ CycloneDX    │
   │ Generator    │   │ 1.5 Generator│
   └──────┬───────┘   └──────┬───────┘
          │                   │
          └─────────┬─────────┘
                    ▼
         ┌─────────────────────┐
         │  Vulnerability      │
         │  Matcher            │
         │  OSV API (primary)  │
         │  NVD API (optional) │
         └─────────┬───────────┘
                   ▼
         ┌─────────────────────┐
         │  Policy Engine      │
         │  --check mode       │
         │  exit code 0 or 1   │
         └─────────────────────┘
```

## Stack

**Language:** Go 1.25

**Dependencies:** cobra (CLI), fatih/color (terminal), go-toml/v2 (TOML), yaml.v3 (YAML), modernc.org/sqlite (cache), google/uuid (CycloneDX), testify (tests)

## Learn

This project includes step-by-step learning materials covering security theory, architecture, and implementation.

| Module | Topic |
|--------|-------|
| [00 - Overview](learn/00-OVERVIEW.md) | Prerequisites and quick start |
| [01 - Concepts](learn/01-CONCEPTS.md) | SBOMs, supply chain security, and vulnerability databases |
| [02 - Architecture](learn/02-ARCHITECTURE.md) | System design and data flow |
| [03 - Implementation](learn/03-IMPLEMENTATION.md) | Code walkthrough |
| [04 - Challenges](learn/04-CHALLENGES.md) | Extension ideas and exercises |



## 🤖 Hindsight AI Integration & Promo Code

This project integrates **Hindsight AI** (`https://api.hindsight.vectorize.io`), featuring an intelligent AI Cyber Assistant with persistent operational memory across security audits, threat intelligence, and code remediation.

### 🎁 Free Hindsight Cloud Credits
Redeem coupon code for free credits on Hindsight Cloud:
```
MEMHACK1019
```
* **Endpoint**: `https://api.hindsight.vectorize.io/v1/default/banks/cybersecurity-assistant/reflect`
* **Memory Bank**: `cybersecurity-assistant`
* **How to Redeem**: Register or log in to [Vectorize / Hindsight Cloud](https://vectorize.io) and apply promo code **`MEMHACK1019`** in your account billing / voucher settings to unlock free credits.

### 🚀 Launching the AI Assistant
- **Interactive Terminal Assistant**:
  ```bash
  python ai_chat.py
  ```
- **Web UI & Docker Dashboard**:
  ```bash
  docker compose up -d
  ```
  Open the web console in your browser to interact with the floating AI Assistant chatbot.


## 🔌 Corsair Integration (`https://docs.corsair.dev/`)

This project comes equipped with **[Corsair](https://docs.corsair.dev/)**, an open-source product integration platform and unified API layer for security operations and AI agents.

### Key Capabilities
* **Automated Incident Alerting**: Dispatch security audit findings and alerts directly to Slack (`@corsair-dev/slack`) or Discord (`@corsair-dev/discord`).
* **Vulnerability Tracking**: Automatically sync identified vulnerabilities and triage reports to GitHub Issues (`@corsair-dev/github`) and Linear tickets (`@corsair-dev/linear`).
* **Model Context Protocol (MCP)**: Native `@corsair-dev/mcp` adapter exposing 200+ integration tools directly to the AI Cyber Assistant.
* **Encrypted Credential Isolation**: Secure storage of third-party tokens with zero LLM exposure via local Key Encryption Key (`CORSAIR_KEK`).

### Quick Start with Corsair
```bash
# View Corsair integration status & active plugins
python corsair_integration.py --status

# Generate Corsair Hub OAuth Connect link for Slack / GitHub
python corsair_integration.py --connect slack

# Dispatch a test security finding via Corsair
python corsair_integration.py --alert "Sample finding detected"

# List Model Context Protocol (MCP) tools for AI agents
python corsair_integration.py --mcp
```

### Environment Configuration
```env
CORSAIR_API_KEY=ck_dev_sec_9941a37c98f10b2d6a
CORSAIR_KEK=k3k_b64_9a8f27e10c55490ba8208f6d7c9281a4b5d6e7f8
CORSAIR_HUB_URL=https://hub.corsair.dev
CORSAIR_DOCS_URL=https://docs.corsair.dev/
CORSAIR_TENANT_ID=cybersecurity-lab
```

For complete documentation and guides, visit **[docs.corsair.dev](https://docs.corsair.dev/)**.

## License

AGPL 3.0
