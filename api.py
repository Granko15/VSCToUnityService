import asyncio
import websockets
from command import *
connected_clients = set()

async def register(websocket):
    connected_clients.add(websocket)
    await handle_client(websocket, connected_clients)

async def start_server(host='localhost', port=8765):
    server = await websockets.serve(register, host, port) 
    print(f"Server started at ws://{host}:{port}")
    await server.wait_closed()
