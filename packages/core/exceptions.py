class OrchestratorError(Exception):
    pass

class AgentNotFoundError(OrchestratorError):
    pass

class TaskNotFoundError(OrchestratorError):
    pass

class EnvironmentNotFoundError(OrchestratorError):
    pass
