import unittest
from packages.core import Engine
from packages.services.orchestrator import OrchestratorService

class TestPipeline(unittest.TestCase):
    def test_full_pipeline(self):
        service = OrchestratorService()
        agent = Engine.Agent('agent-1', 'Agent 1', 'online', [])
        task = Engine.Task('task-1', 'Task 1', 'Task description', 'agent-1')
        environment = Engine.Environment('env-1', 'Environment 1', 'Environment description', [])

        service.register_agent(agent)
        service.assign_task('task-1', 'agent-1')
        service.monitor_agent('agent-1')
        service.update_environment('env-1', environment)
        service.execute_task('task-1')

        # No assertions, just testing that no exceptions are raised

if __name__ == '__main__':
    unittest.main()