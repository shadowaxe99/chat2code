from .agent import Agent
from .communication_manager import CommunicationManager
from .data_storage import DataStorage
from .flow_controller import FlowController
from .learning_manager import LearningManager


class AgentSystem:
    def __init__(self):
        self.agent = Agent()
        self.communication_manager = CommunicationManager()
        self.data_storage = DataStorage()
        self.flow_controller = FlowController()
        self.learning_manager = LearningManager()

    def start(self):
        self.flow_controller.start_flow()

    def stop(self):
        self.flow_controller.stop_flow()
}