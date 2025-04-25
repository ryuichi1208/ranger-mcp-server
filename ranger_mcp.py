#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ranger MCP Server module.

This module implements a Model Context Protocol (MCP) server.
It responds with "Ranger!" to any request.
It uses the FastMCP framework to provide the Ranger response as an MCP tool.
"""

import datetime
import json
import logging
import os
import sys
from typing import Dict, List, Optional, Any

from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent, Tool


# Custom formatter for JSON log output
class JsonFormatter(logging.Formatter):
    """
    Custom formatter to output logs in JSON format.
    """

    def format(self, record):
        log_record = {
            "timestamp": datetime.datetime.now().isoformat(),
            "level": record.levelname,
            "name": record.name,
            "message": record.getMessage(),
        }

        # Add exception info if present
        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)

        # Add any extra attributes
        if hasattr(record, "extra"):
            log_record.update(record.extra)

        return json.dumps(log_record, ensure_ascii=False)


# Configure root logger with JSON formatter
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logging.basicConfig(level=logging.INFO, handlers=[handler])

logger = logging.getLogger(__name__)

# FastMCP instance
mcp = FastMCP("ranger server")


@mcp.tool()
async def ranger():
    """
    A tool that responds with "Ranger!" to any question or request.

    Returns:
        list: A list containing a TextContent object with "Ranger!".
    """
    logger.info("ranger function was called")
    return [TextContent(type="text", text="Ranger！")]


@mcp.tool()
async def ranger_with_input(input_text: str):
    """
    A tool that accepts user input but always responds with "Ranger!".

    Args:
        input_text (str): Input text from the user.

    Returns:
        list: A list containing a TextContent object with "Ranger!".
    """
    logger.info("ranger_with_input function was called", extra={"input": input_text})
    return [TextContent(type="text", text="Ranger！")]


@mcp.tool()
async def ranger_json():
    """
    A tool that responds with "Ranger!" in JSON format.

    Returns:
        list: A list containing a TextContent object with JSON-formatted "Ranger!".
    """
    logger.info("ranger_json function was called")
    response = {
        "response": "Ranger！",
        "timestamp": datetime.datetime.now().isoformat(),
    }
    return [TextContent(type="text", text=json.dumps(response, ensure_ascii=False))]


@mcp.tool()
async def ranger_with_options(option_type: str = "simple"):
    """
    A tool that returns variations of the Ranger response based on different options.
    The "Ranger!" response remains the same regardless of the option.

    Args:
        option_type (str): Response option ('simple', 'json', 'extended').

    Returns:
        list: A list containing a TextContent object with "Ranger!".
    """
    logger.info("ranger_with_options function was called", extra={"option": option_type})

    if option_type == "json":
        response = {
            "response": "Ranger！",
            "timestamp": datetime.datetime.now().isoformat(),
        }
        return [TextContent(type="text", text=json.dumps(response, ensure_ascii=False))]
    elif option_type == "extended":
        return [TextContent(type="text", text="Ranger！ Ranger！ Ranger！")]
    else:
        # Default is the simple "Ranger!"
        return [TextContent(type="text", text="Ranger！")]


@mcp.tool()
async def ranger_with_params(param1: Optional[str] = None, param2: Optional[int] = None, param3: Optional[Dict] = None):
    """
    A tool that accepts parameters but ignores them and always responds with "Ranger!".

    Args:
        param1 (Optional[str]): An arbitrary string parameter.
        param2 (Optional[int]): An arbitrary integer parameter.
        param3 (Optional[Dict]): An arbitrary dictionary parameter.

    Returns:
        list: A list containing a TextContent object with "Ranger!".
    """
    logger.info(
        "ranger_with_params was called",
        extra={"param1": param1, "param2": param2, "param3": str(param3)},
    )
    return [TextContent(type="text", text="Ranger！")]


# Add a generic tool for all other requests
@mcp.tool()
async def any_request(request: Optional[str] = None, **kwargs):
    """
    A generic tool that responds with "Ranger!" to any request.
    Functions as an alternative to a catch-all.

    Args:
        request (Optional[str]): The request string.
        **kwargs: Any other arbitrary parameters.

    Returns:
        list: A list containing a TextContent object with "Ranger!".
    """
    logger.info("any_request was called", extra={"request": request, "args": str(kwargs)})
    return [TextContent(type="text", text="Ranger！")]


if __name__ == "__main__":
    try:
        # Display server start message
        logger.info("Starting Ranger MCP server")
        print("MCP server that responds 'Ranger!' to everything has started", file=sys.stderr)

        # Execute FastMCP (call the run method directly, do not use asyncio.run)
        mcp.run(transport="stdio")
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
        print("Shutting down Ranger MCP server", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        logger.error(f"Failed to start server: {e}")
        sys.exit(1)
