import asyncio


class Client:
    def __init__(self, host='localhost', port=8888):
        self.host = host
        self.port = port

    async def start(self):
        reader, writer = await asyncio.open_connection(self.host, self.port)
        while True:
            message = input('Enter message: ')
            print(f'Send: {message}')
            writer.write(message.encode())
            await writer.drain()
            if message == 'exit':
                break
        print('Closing the connection')
        writer.close()
        await writer.wait_closed()