from fastmcp import FastMCP, Context
from typing import Dict, Any

mcp = FastMCP(name="SQLMcpTool")


@mcp.tool()
async def analyze_query_security(query: str, ctx: Context) -> Dict[str, Any]:
    """
    Analyzes a SQL query for potential security issues.
    """
    ctx.info(f"Analyzing query security: {query}")

    security_issues = []
    risk_level = "low"

    # Simple checks for common SQL injection patterns
    lower_query = query.lower()

    if "--" in query:
        security_issues.append(
            "Contains comment operator (--) which may be used to comment out the rest of the query"
        )
        risk_level = "high"

    if ";" in query and (
        "select" in lower_query
        or "insert" in lower_query
        or "update" in lower_query
        or "delete" in lower_query
    ):
        security_issues.append(
            "Contains semicolon followed by another SQL command, potential for multiple statement execution"
        )
        risk_level = "high"

    if "union" in lower_query and "select" in lower_query:
        security_issues.append(
            "Contains UNION operator which may be used to append additional queries"
        )
        risk_level = "high"

    if (
        "or 1=1" in lower_query
        or "or '1'='1'" in lower_query
        or 'or "1"="1"' in lower_query
    ):
        security_issues.append(
            "Contains tautology (OR 1=1) which may bypass authentication"
        )
        risk_level = "high"

    if lower_query.count("select") > 1:
        security_issues.append(
            "Contains nested SELECT statements which may indicate an attempt to extract additional data"
        )
        risk_level = "medium"

    if not security_issues:
        security_issues.append(
            "No obvious security issues detected, but further analysis is recommended"
        )

    return {
        "query": query,
        "security_issues": security_issues,
        "risk_level": risk_level,
        "recommendation": "Use parameterized queries instead of string concatenation",
    }


@mcp.resource("config://version")
def get_version(ctx: Context):
    ctx.info("Returning version")
    return "1.0.0"


@mcp.resource("config://help")
def get_help(ctx: Context):
    ctx.info("Returning help information")
    return {
        "tool_description": "SQL Injection Testing Tool for Security Researchers",
        "purpose": "This tool demonstrates SQL injection vulnerabilities in a safe, controlled environment",
        "example_vulnerable_queries": [
            "SELECT * FROM users WHERE username = 'admin' OR 1=1",
            "SELECT * FROM users WHERE username = 'admin'; DROP TABLE users;",
            "SELECT * FROM users WHERE username = 'admin' UNION SELECT * FROM products",
        ],
        "disclaimer": "This tool is for educational purposes only. Do not use these techniques on systems without explicit permission.",
    }


if __name__ == "__main__":
    mcp.run()
