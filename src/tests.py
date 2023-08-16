import unittest
from .agent_system import AgentSystem


class TestAgentSystem(unittest.TestCase):
    def setUp(self):
        self.agent_system = AgentSystem()

    def test_start(self):
        self.agent_system.start()
        self.assertEqual(self.agent_system.get_status(), {'agent_status': 'running', 'flow_status': 'started'})

    def test_stop(self):
        self.agent_system.stop()
        self.assertEqual(self.agent_system.get_status(), {'agent_status': 'idle', 'flow_status': 'stopped'})

    def test_handle_message(self):
        self.assertEqual(self.agent_system.handle_message('test_message'), 'test_message')

    def test_handle_data(self):
        self.assertEqual(self.agent_system.handle_data('test_key', 'test_value'), 'test_value')

    def test_handle_learning(self):
        self.assertEqual(self.agent_system.handle_learning('test_data'), 'model_evaluation')

if __name__ == '__main__':
    unittest.main()