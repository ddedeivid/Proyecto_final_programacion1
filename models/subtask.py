from models.task import Task


class SubTask(Task):
    def __init__(self, task_id, title, description, responsible_user, project, category, priority, status, due_date,
                 parent_task):
        super().__init__(task_id, title, description, responsible_user, project, category, priority, status, due_date)
        self._parent_task = parent_task  # Object type: Task

    # Getter
    def get_parent_task(self):
        return self._parent_task

    # Setter
    def set_parent_task(self, parent_task):
        self._parent_task = parent_task

    # Functionality
    def show_info(self):
        return (f"SubTask ID: {self.get_task_id()}\t"
                f"Title: {self._parent_task.get_title()}\t"
                f"Parent ID: {self._parent_task.get_task_id()}\n")
