import uuid

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, title, priority):
        task_id = str(uuid.uuid4())  # Генерация уникального ID для задачи
        task = {
            "id": task_id,
            "title": title,
            "priority": priority
        }
        self.tasks[task_id] = task
        return task

    def get_tasks(self):
        return list(self.tasks.values())

    def update_task(self, task_id, title=None, priority=None):
        if task_id in self.tasks:
            if title:
                self.tasks[task_id]["title"] = title
            if priority:
                self.tasks[task_id]["priority"] = priority
            return self.tasks[task_id]
        return None

    def delete_task(self, task_id):
        return self.tasks.pop(task_id, None)