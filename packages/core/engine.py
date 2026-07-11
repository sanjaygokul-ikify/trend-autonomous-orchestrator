import logging
from typing import List, Dict
from .types import Agent, Task, Environment
from .exceptions import OrchestratorError

class Engine:
    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        self.tasks: Dict[str, Task] = {}
        self.environments: Dict[str, Environment] = {}
        self.logger = logging.getLogger(__name__)

    def register_agent(self, agent: Agent):
        if agent.id in self.agents:
            raise OrchestratorError("Agent already registered")
        self.agents[agent.id] = agent
        self.logger.info(f"Agent {agent.id} registered")

    def assign_task(self, task_id: str, agent_id: str):
        if task_id not in self.tasks:
            raise OrchestratorError("Task not found")
        if agent_id not in self.agents:
            raise OrchestratorError("Agent not found")
        task: Task = self.tasks[task_id]
        agent: Agent = self.agents[agent_id]
        agent.assign_task(task)
        self.logger.info(f"Task {task_id} assigned to agent {agent_id}")

    def monitor_agent(self, agent_id: str):
        if agent_id not in self.agents:
            raise OrchestratorError("Agent not found")
        agent: Agent = self.agents[agent_id]
        self.logger.info(f"Agent {agent_id} status: {agent.status}")

    def update_environment(self, environment_id: str, environment: Environment):
        if environment_id not in self.environments:
            raise OrchestratorError("Environment not found")
        self.environments[environment_id] = environment
        self.logger.info(f"Environment {environment_id} updated")

    def execute_task(self, task_id: str):
        if task_id not in self.tasks:
            raise OrchestratorError("Task not found")
        task: Task = self.tasks[task_id]
        task.execute()
        self.logger.info(f"Task {task_id} executed")

    def get_agents(self) -> List[Agent]:
        return list(self.agents.values())

    def get_tasks(self) -> List[Task]:
        return list(self.tasks.values())

    def get_environments(self) -> List[Environment]:
        return list(self.environments.values())

    def create_task(self, task_id: str, name: str, description: str, agent_id: str):
        if task_id in self.tasks:
            raise OrchestratorError("Task already exists")
        task = Task(task_id, name, description, agent_id)
        self.tasks[task_id] = task
        self.logger.info(f"Task {task_id} created")

    def create_environment(self, environment_id: str, name: str, description: str, agents: List[str]):
        if environment_id in self.environments:
            raise OrchestratorError("Environment already exists")
        environment = Environment(environment_id, name, description, agents)
        self.environments[environment_id] = environment
        self.logger.info(f"Environment {environment_id} created")
