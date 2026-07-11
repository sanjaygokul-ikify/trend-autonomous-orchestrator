from typing import Dict, List
from dataclasses import dataclass

@dataclass
class Agent:
    id: str
    name: str
    status: str
    tasks: List[str]

    def assign_task(self, task: 'Task'):
        self.tasks.append(task.id)

@dataclass
class Task:
    id: str
    name: str
    description: str
    agent_id: str

    def execute(self):
        # task execution logic
        pass

@dataclass
class Environment:
    id: str
    name: str
    description: str
    agents: List[str]

    def update(self, new_environment: 'Environment'):
        self.name = new_environment.name
        self.description = new_environment.description
        self.agents = new_environment.agents
