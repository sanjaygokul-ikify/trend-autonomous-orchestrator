from packages.core import Engine
from packages.utils.logging import OrchestratorLogger

class OrchestratorService:
    def __init__(self):
        self.engine = Engine()
        self.logger = OrchestratorLogger('orchestrator')

    def register_agent(self, agent):
        self.engine.register_agent(agent)
        self.logger.info('Agent registered')

    def assign_task(self, task_id: str, agent_id: str):
        self.engine.assign_task(task_id, agent_id)
        self.logger.info('Task assigned to agent')

    def monitor_agent(self, agent_id: str):
        self.engine.monitor_agent(agent_id)
        self.logger.info('Agent monitored')

    def update_environment(self, environment_id: str, environment):
        self.engine.update_environment(environment_id, environment)
        self.logger.info('Environment updated')

    def execute_task(self, task_id: str):
        self.engine.execute_task(task_id)
        self.logger.info('Task executed')