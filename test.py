from rich import print

from mcp_myguides.config import get_settings
from mcp_myguides.server import get_app
mcp_server = get_app()

import asyncio
from fastmcp import Client

mcp_client = Client(mcp_server)

async def call_tool():

    settings = get_settings()
    print(settings.GUIDES_BASE_PATH)

    async with mcp_client:

        await mcp_client.ping()

        # tools = await mcp_client.list_tools()
        # print(tools)

        result = await mcp_client.call_tool("list_guides")
        print(result)

asyncio.run(call_tool())
