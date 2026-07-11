import unittest
from packages.core import Engine, Agent, Task, Environment

class TestCore(unittest.TestCase):
    def test_register_agent(self):
        engine = Engine()
        agent = Agent('agent-1', 'Agent 1', 'online', [])
        engine.register_agent(agent)
        self.assertIn(agent.id, engine.agents)

    def test_assign_task(self):
        engine = Engine()
        agent = Agent('agent-1', 'Agent 1', 'online', [])
        task = Task('task-1', 'Task 1', 'Task description', 'agent-1')
        engine.register_agent(agent)
        engine.tasks['task-1'] = task
        engine.assign_task('task-1', 'agent-1')
        self.assertIn('task-1', agent.tasks)

    def test_monitor_agent(self):
        engine = Engine()
        agent = Agent('agent-1', 'Agent 1', 'online', [])
        engine.register_agent(agent)
        engine.monitor_agent('agent-1')
        # No assertions, just testing that no exceptions are raised

    def test_update_environment(self):
        engine = Engine()
        environment = Environment('env-1', 'Environment 1', 'Environment description', [])
        engine.environments['env-1'] = environment
        new_environment = Environment('env-1', 'New Environment 1', 'New Environment description', [])
        engine.update_environment('env-1', new_environment)
        self.assertEqual(engine.environments['env-1'].name, 'New Environment 1')

    def test_execute_task(self):
        engine = Engine()
        task = Task('task-1', 'Task 1', 'Task description', 'agent-1')
        engine.tasks['task-1'] = task
        engine.execute_task('task-1')
        # No assertions, just testing that no exceptions are raised

if __name__ == '__main__':
    unittest.main()