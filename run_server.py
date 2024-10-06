import asyncio
import websockets
import api

if __name__ == "__main__":
    asyncio.run(api.start_server())