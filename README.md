# Ranger MCP Server

This is a simple Model Context Protocol (MCP) server based on `FastMCP`.
It consistently responds with "Ranger!" to any MCP tool request it receives via standard input/output (stdio).

## Installation

```bash
git clone https://github.com/ryuichi1208/ranger-mcp-server.git
cd ranger-mcp-server
pip install -r requirements.txt
```

## Usage

Run the server script:

```bash
python ranger_fastmcp.py
```

The server will start, listen for MCP requests on stdin, send "Ranger!" responses to stdout, and print JSON logs to stderr.

It provides several tools (like `ranger`, `ranger_with_input`, `any_request`, etc.), but all of them ignore inputs and simply return "Ranger!".

## About MCP (Model Context Protocol)

MCP (Model Context Protocol) is a protocol designed for connecting AI models with external tools and services. This server is a very basic example implementation of an MCP server. Real-world MCP servers often involve more complex protocols and service definitions.
