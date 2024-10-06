import asyncio
import websockets

async def get_line_number(websocket, line_number):
    await websocket.send(f"You are on line {line_number}")

async def jump_to_line(websocket, line_number, connected_clients):
    await websocket.send(f"Jumping to line {line_number}") 
    
    # Broadcast the jump command to all connected clients
    for client in connected_clients:
        print(f"Sending to client: {client}")
        if client != websocket: 
            await client.send(f"Jumping to line {line_number}") 

async def unknown_command(websocket):
    await websocket.send("Error: Unknown command.")

async def handle_client(websocket, connected_clients):
    connected_clients.add(websocket)  # Register the new client
    print(f"New client connected: {websocket}")
    try:
        async for message in websocket:
            print(f"Message received: {message}")

            # Split the message into command and parameters
            command_parts = message.split(":")
            command = command_parts[0]
            params = command_parts[1:] if len(command_parts) > 1 else []

            # Check if the command exists in the dictionary
            if command in command_dict:
                if command == "jump_to_line":
                    await command_dict[command](websocket, *params, connected_clients)  # Pass the line number
                elif command == "get_line_number":
                    if params:
                        await command_dict[command](websocket, params[0])  # Pass the line number
                    else:
                        await websocket.send("Error: Line number is missing for get_line_number")
                else:
                    await command_dict[command](websocket)  # No parameters needed
            else:
                await unknown_command(websocket)
    finally:
        connected_clients.remove(websocket)  # Remove the client when done

command_dict = {
    "get_line_number": get_line_number,
    "jump_to_line": jump_to_line,
}
