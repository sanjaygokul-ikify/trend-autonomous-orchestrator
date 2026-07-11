import argparse
from packages.core import Engine
from packages.services.orchestrator import OrchestratorService

def main():
    parser = argparse.ArgumentParser(description='Autonomous Orchestrator CLI')
    subparsers = parser.add_subparsers(dest='command')

    register_parser = subparsers.add_parser('register', help='Register an agent')
    register_parser.add_argument('--agent-id', required=True, help='Agent ID')
    register_parser.add_argument('--agent-name', required=True, help='Agent name')

    assign_parser = subparsers.add_parser('assign', help='Assign a task to an agent')
    assign_parser.add_argument('--task-id', required=True, help='Task ID')
    assign_parser.add_argument('--agent-id', required=True, help='Agent ID')

    monitor_parser = subparsers.add_parser('monitor', help='Monitor an agent')
    monitor_parser.add_argument('--agent-id', required=True, help='Agent ID')

    update_parser = subparsers.add_parser('update', help='Update an environment')
    update_parser.add_argument('--environment-id', required=True, help='Environment ID')
    update_parser.add_argument('--environment-name', required=True, help='Environment name')

    execute_parser = subparsers.add_parser('execute', help='Execute a task')
    execute_parser.add_argument('--task-id', required=True, help='Task ID')

    args = parser.parse_args()

    service = OrchestratorService()

    if args.command == 'register':
        agent = Engine.Agent(args.agent_id, args.agent_name, 'online', [])
        service.register_agent(agent)
    elif args.command == 'assign':
        task = Engine.Task(args.task_id, 'Task', 'Task description', args.agent_id)
        service.assign_task(args.task_id, args.agent_id)
    elif args.command == 'monitor':
        service.monitor_agent(args.agent_id)
    elif args.command == 'update':
        environment = Engine.Environment(args.environment_id, args.environment_name, 'Environment description', [])
        service.update_environment(args.environment_id, environment)
    elif args.command == 'execute':
        service.execute_task(args.task_id)

if __name__ == '__main__':
    main()