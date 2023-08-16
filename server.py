import asyncio
import websockets


class Server:
    def __init__(self):
        self.connected = set()

    async def handler(self, websocket, path):
        self.connected.add(websocket)
        try:
            async for message in websocket:
                await asyncio.wait([ws.send(message) for ws in self.connected])
        except Exception as e:
            print(f'Error: {e}')
        finally:
            self.connected.remove(websocket)

    def start(self):
        start_server = websockets.serve(self.handler, 'localhost', 8765)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    server = Server()
    server.start()