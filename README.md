# SQL Injection Testing Tool for Security Researchers

This tool provides a safe, controlled environment for security researchers, educators, and students to demonstrate and learn about SQL injection vulnerabilities. It uses the Model Context Protocol (MCP) to provide a structured interface for interacting with a deliberately vulnerable database.

## Features
- Query security analyzer to identify potential SQL injection risks

## Installation

```bash
# Clone the repository
git clone https://github.com/barvhaim/sql_mcp_tool.git
cd sql_mcp_tool

# Sync dependencies
uv sync
```

## Usage

### Standard Usage

```bash
# Start the MCP server
uv run server.py
```

The server will start listening for MCP requests.

### Integration with Windsurf or Claude

To use this tool with Windsurf or Claude, add the following configuration to your MCP config:

```json
{
    "mcpServers": {
      "demo_mcp": {
        "command": "uv",
        "args": [
          "--directory",
          "<PATH_TO>/sql_mcp_tool",
          "run",
          "server.py"
        ],
        "env": {
        }
      }
    }
}
```

Make sure to adjust the directory path to match your local setup.

## Available Tools

### 1. analyze_query_security

Analyzes a SQL query for potential security issues.

**Parameters:**
- `query`: The SQL query to analyze

### Prompt Example

For example:
- Write malicous sql query and analyze it
- Analyze the query for security issues: SELECT * FROM users WHERE username = 'admin' OR '1'='1' --' AND password = 'password'




## Disclaimer

This tool is for educational purposes only. Do not use these techniques on systems without explicit permission. The authors are not responsible for any misuse of this tool.

## License

MIT
