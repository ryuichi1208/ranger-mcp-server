# Ranger MCP Server

It consistently responds with "Ranger!" to any MCP tool request it receives via standard input/output (stdio).

## Usage

Run the server script:

```bash
python ranger_fastmcp.py
```

It provides several tools (like `ranger`, `ranger_with_input`, `any_request`, etc.), but all of them ignore inputs and simply return "Ranger!".
