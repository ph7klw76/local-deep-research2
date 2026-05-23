# Local Deep Research — DeepSeek v4 Edition

<div align="center">

**AI-powered research assistant with DeepSeek v4 Flash integration and full MCP support**

*Fork of [Local Deep Research](https://github.com/LearningCircuit/local-deep-research) optimized for DeepSeek v4 models with enhanced MCP server capabilities*

</div>

---

## ⚡ Why This Fork?

This fork of the **Local Deep Research** (LDR) project is specifically optimized for:

- 🚀 **DeepSeek v4 Flash** — Default model: fast, cost-effective deep research
- 🧠 **DeepSeek v4 Pro** — Premium reasoning for complex research tasks
- 🔌 **MCP Server** — Full Model Context Protocol integration for AI agent workflows
- 🎯 **Ready to use** — Pre-configured DeepSeek provider with auto-discovery

---

## 📦 Quick Start

### Prerequisites

- Python 3.12+
- A DeepSeek API key ([get one here](https://platform.deepseek.com/api_keys))
- SearXNG (optional, for web search)

### Install

```bash
# Clone the repo
git clone https://github.com/ph7klw76/local-deep-research2.git
cd local-deep-research2

# Install with MCP support
pip install -e ".[mcp]"

# Set your DeepSeek API key
export LDR_LLM_PROVIDER=deepseek
export LDR_LLM_DEEPSEEK_API_KEY=sk-your-api-key-here
export LDR_LLM_MODEL=deepseek-v4-flash

# Start the web UI
python -m local_deep_research.web.app
# Open http://localhost:5000
```

### Using Docker

```bash
docker run -d -p 5000:5000 \
  -e LDR_LLM_PROVIDER=deepseek \
  -e LDR_LLM_DEEPSEEK_API_KEY=sk-your-api-key-here \
  -e LDR_LLM_MODEL=deepseek-v4-flash \
  -v deep-research-data:/data \
  -e LDR_DATA_DIR=/data \
  ghcr.io/ph7klw76/local-deep-research2:latest
```

---

## 🔌 MCP Server

This project includes a full **Model Context Protocol (MCP)** server, allowing AI agents like Claude, Cursor, and others to use Local Deep Research as a tool.

### Available MCP Tools

| Tool | Description | Time |
|------|-------------|------|
| `quick_research` | Fast research summary | 1-5 min |
| `detailed_research` | Comprehensive analysis with sources | 5-15 min |
| `generate_report` | Full markdown report with citations | 10-30 min |
| `analyze_documents` | Search your local document collection | 30s-2 min |
| `search` | Raw search without LLM processing | 5-30s |
| `list_search_engines` | List available search engines | Instant |
| `list_strategies` | List research strategies | Instant |
| `get_configuration` | View current server config | Instant |

### MCP Configuration

Add to your MCP client config (e.g., Claude Desktop `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "local-deep-research": {
      "command": "python",
      "args": ["-m", "local_deep_research.mcp"],
      "env": {
        "LDR_LLM_PROVIDER": "deepseek",
        "LDR_LLM_DEEPSEEK_API_KEY": "sk-your-api-key-here",
        "LDR_LLM_MODEL": "deepseek-v4-flash"
      }
    }
  }
}
```

Or use the CLI entry point:

```bash
ldr-mcp
```

### Testing the MCP Server

```bash
# Smoke test (requires bash)
bash scripts/mcp_smoke_test.sh

# Manual test
python -c "
from local_deep_research.mcp.server import mcp
# Server starts on STDIO transport
"
```

---

## 🤖 Supported DeepSeek Models

| Model | Description | Best For |
|-------|-------------|----------|
| `deepseek-v4-flash` | Fast, cost-effective (default) | Quick research, summaries |
| `deepseek-v4-pro` | Premium reasoning | Complex analysis, reports |
| `deepseek-reasoner` | Legacy R1 reasoning | Deep reasoning tasks |
| `deepseek-chat` | Legacy V3 chat | General purpose |

---

## 🌐 Web UI

Launch the web interface:

```bash
python -m local_deep_research.web.app
```

Then open **http://localhost:5000** in your browser.

### Configuration via Web UI

1. Go to **Settings** → **LLM**
2. Select **DeepSeek** as the provider
3. Enter your API key
4. Choose model: `deepseek-v4-flash` or `deepseek-v4-pro`
5. Click **Save**

---

## 🏗️ Architecture

```
                    ┌──────────────────────┐
                    │   MCP Server (STDIO)  │
                    │   AI Agents ↔ LDR     │
                    └──────────┬───────────┘
                               │
┌──────────────┐    ┌──────────▼───────────┐    ┌──────────────┐
│  Web UI      │    │                      │    │  SearXNG     │
│  :5000       │◄──►│  Local Deep Research │◄──►│  Search      │
│  Flask + JS  │    │  Research Engine     │    │  Engine      │
└──────────────┘    └──────────┬───────────┘    └──────────────┘
                               │
                    ┌──────────▼───────────┐
                    │  DeepSeek v4 API     │
                    │  api.deepseek.com    │
                    │  Flash / Pro models  │
                    └──────────────────────┘
```

---

## 🔧 CLI Usage

```bash
# Quick research via CLI
ldr research "What are the latest developments in fusion energy?"

# Start MCP server
ldr-mcp

# Start web server
ldr-web
```

---

## ⚙️ Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `LDR_LLM_PROVIDER` | LLM provider | `deepseek` |
| `LDR_LLM_DEEPSEEK_API_KEY` | DeepSeek API key | (required) |
| `LDR_LLM_MODEL` | Model name | `deepseek-v4-flash` |
| `LDR_LLM_TEMPERATURE` | Generation temperature | `0.7` |
| `LDR_DATA_DIR` | Data storage directory | `~/.local/share/local-deep-research` |
| `LDR_SEARCH_TOOL` | Default search engine | `duckduckgo` |

---

## 📚 Original Project

This is a fork of [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research), a powerful AI research assistant with:
- 20+ research strategies (LangGraph agent, iterative, source-based, etc.)
- 30+ search engines (arXiv, PubMed, Wikipedia, Semantic Scholar, etc.)
- Encrypted SQLCipher database (AES-256)
- Full library & RAG pipeline
- Self-hosted, zero telemetry

See the [original documentation](docs/) for complete features.

---

## 📄 License

MIT License — see [LICENSE](LICENSE).

---

## 🙏 Acknowledgements

Built on the incredible work of the [Local Deep Research](https://github.com/LearningCircuit/local-deep-research) team and the open-source community.

