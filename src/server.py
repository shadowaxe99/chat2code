import asyncio
import websockets


class Server:
    def __init__(self, host='localhost', port=8765):
        self.host = host
        self.port = port

    async def start(self):
        async with websockets.serve(self.handler, self.host, self.port):
            await asyncio.Future()  # run forever

    async def handler(self, websocket, path):
        async for message in websocket:
            await websocket.send(message)


if __name__ == '__main__':
    server = Server()
    asyncio.run(server.start())