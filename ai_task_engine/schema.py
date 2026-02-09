# schema.py
class Task:
    def __init__(self, task_id, name, owner, domain, status, priority, dependency, risk):
        self.task_id = task_id
        self.name = name
        self.owner = owner
        self.domain = domain
        self.status = status
        self.priority = priority
        self.dependency = dependency
        self.risk = risk

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "name": self.name,
            "owner": self.owner,
            "domain": self.domain,
            "status": self.status,
            "priority": self.priority,
            "dependency": self.dependency,
            "risk": self.risk
        }