import asyncio
from docker_integration import DockerIntegration
from UI_manager import UIManager
from testing import Testing
from error_handling_manager import ErrorHandlingManager
from database_migrations import DatabaseMigrations
from logging_manager import LoggingManager
from documentation import Documentation
from agent_system import AgentSystem


async def startup(idea: str, investment: float = 3.0, n_round: int = 5):
    agent_system = AgentSystem()
    agent_system.start()
    await asyncio.sleep(n_round)
    agent_system.stop()

def main(idea: str = 'New Project', investment: float = 3.0, n_round: int = 5):
    asyncio.run(startup(idea, investment, n_round))

if __name__ == '__main__':
    main()