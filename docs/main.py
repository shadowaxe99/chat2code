import asyncio
from src.server import Server


def startup():
    server = Server()
    server.start()


def main():
    asyncio.run(startup())


if __name__ == '__main__':
    main()