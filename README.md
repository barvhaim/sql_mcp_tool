# SQL Injection Testing Tool for Security Researchers

This tool provides a safe, controlled environment for security researchers, educators, and students to demonstrate and learn about SQL injection vulnerabilities. It uses the Model Context Protocol (MCP) to provide a structured interface for interacting with a deliberately vulnerable database.

## Features

- Demonstration database with sample user and product data
- Tools to execute both vulnerable and safe SQL queries
- Query security analyzer to identify potential SQL injection risks
- Database schema explorer
- Educational resources and examples

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/sql-injection-test-tool.git
cd sql-injection-test-tool

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Start the MCP server
python server.py
```

The server will create a demonstration SQLite database and start listening for MCP requests.

## Available Tools

### 1. run_vulnerable_query

Executes a SQL query directly without sanitization, demonstrating SQL injection vulnerabilities.

**Parameters:**
- `query`: The SQL query to execute (intentionally vulnerable)

### 2. run_safe_query

Executes a SQL query with proper parameterization, demonstrating safe SQL practices.

**Parameters:**
- `table`: The table to query
- `columns`: (Optional) List of columns to select
- `where_clause`: (Optional) Dictionary of column-value pairs for the WHERE clause

### 3. analyze_query_security

Analyzes a SQL query for potential security issues.

**Parameters:**
- `query`: The SQL query to analyze

### 4. get_database_schema

Returns the schema of the demonstration database.

## Sample Demo Prompt

```
I want to explore SQL injection vulnerabilities in a safe environment. Show me:

1. The database schema to understand what tables and columns are available
2. A safe query to retrieve all users
3. A vulnerable query that would allow me to bypass authentication
4. An analysis of why the vulnerable query is dangerous
5. The proper way to implement the same query securely

Then, demonstrate a more advanced SQL injection technique using UNION attacks to extract data from a different table.
```

## Educational Resources

- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [PortSwigger SQL Injection Tutorial](https://portswigger.net/web-security/sql-injection)
- [SANS SQL Injection Cheat Sheet](https://www.sans.org/blog/sql-injection-cheat-sheet/)

## Disclaimer

This tool is for educational purposes only. Do not use these techniques on systems without explicit permission. The authors are not responsible for any misuse of this tool.

## License

MIT
