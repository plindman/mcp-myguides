from rich import print

from mcp_myguides.config import get_settings
from mcp_myguides.server import get_app
mcp_server = get_app()

import asyncio
from fastmcp import Client

mcp_client = Client(mcp_server)

async def call_tool():

    settings = get_settings()
    print(settings.GUIDES_ROOT_PATH)

    async with mcp_client:

        await mcp_client.ping()

        result = await mcp_client.call_tool("get_guides_content_by_tags", {"tags": ['python', 'python/overview']})
        print(result)

asyncio.run(call_tool())
