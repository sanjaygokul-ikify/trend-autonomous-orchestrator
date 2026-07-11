import time

class MetricCollector:
    def __init__(self):
        self.metrics = {}

    def record(self, name: str, value: float):
        self.metrics[name] = value

    def get_metric(self, name: str) -> float:
        return self.metrics.get(name, 0.0)