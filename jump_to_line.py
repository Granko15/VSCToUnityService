import asyncio
import websockets

async def send_jump_command(line_number):
    uri = "ws://localhost:8765"  # Adjust to your server URI
    async with websockets.connect(uri) as websocket:
        # Send the jump command
        await websocket.send(f"jump_to_line:{line_number}")

        # Wait for the server's response
        response = await websocket.recv()
        print(f"Received from server: {response}")

if __name__ == "__main__":
    line_to_jump = 25  # Set the line number you want to jump to
    asyncio.run(send_jump_command(line_to_jump))
