import asyncio
from server import Server


async def startup():
    server = Server()
    server.start()


def main():
    asyncio.run(startup())


if __name__ == '__main__':
    main()