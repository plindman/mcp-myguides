from src.server import get_app
mcp = get_app()

import asyncio
from fastmcp import Client

client = Client(mcp)

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("health")
        print(result.content[0].text)

        result = await client.call_tool("list_guides")
        print(result)

asyncio.run(call_tool("Ford"))
