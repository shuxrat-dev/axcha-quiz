import asyncio
import aiohttp
import os

async def ping_server():
    url = os.getenv("RENDER_EXTERNAL_URL")
    if not url:
        return
        
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.get(url) as response:
                    print(f"Ping: {response.status}")
            except:
                pass
            await asyncio.sleep(600)  # Ping every 10 minutes

if __name__ == "__main__":
    asyncio.run(ping_server())
