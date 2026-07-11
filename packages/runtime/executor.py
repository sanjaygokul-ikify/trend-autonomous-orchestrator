import logging
from typing import Dict, List
from ..core.engine import Engine
from ..core.types import Agent, Task, Environment
from ..core.exceptions import OrchestratorError

class Executor:
    def __init__(self):
        self.engine: Engine = Engine()
        self.logger = logging.getLogger(__name__)

    def execute(self, task_id: str):
        try:
            self.engine.execute_task(task_id)
            self.logger.info(f"Task {task_id} executed successfully")
        except OrchestratorError as e:
            self.logger.error(f"Error executing task {task_id}: {e}")

    def register_agent(self, agent: Agent):
        try:
            self.engine.register_agent(agent)
            self.logger.info(f"Agent {agent.id} registered successfully")
        except OrchestratorError as e:
            self.logger.error(f"Error registering agent {agent.id}: {e}")

    def assign_task(self, task_id: str, agent_id: str):
        try:
            self.engine.assign_task(task_id, agent_id)
            self.logger.info(f"Task {task_id} assigned to agent {agent_id} successfully")
        except OrchestratorError as e:
            self.logger.error(f"Error assigning task {task_id} to agent {agent_id}: {e}")

    def monitor_agent(self, agent_id: str):
        try:
            self.engine.monitor_agent(agent_id)
            self.logger.info(f"Agent {agent_id} status monitored successfully")
        except OrchestratorError as e:
            self.logger.error(f"Error monitoring agent {agent_id}: {e}")
