from datetime import date, datetime


class Task:
    def __init__(self, task_id, title, description, responsible_user, project, category, priority, status, due_date):
        self._task_id = task_id
        self._title = title
        self._description = description
        self._responsible_user = responsible_user  # Object type: User
        self._project = project  # Object type: Project
        self._category = category
        self._priority = priority
        self._status = status
        self.set_due_date(due_date)
        self._comments = []

    # Getters
    def get_task_id(self):
        return self._task_id

    def get_title(self):
        return self._title

    def get_description(self):
        return self._description

    def get_responsible_user(self):
        return self._responsible_user

    def get_project(self):
        return self._project

    def get_category(self):
        return self._category

    def get_priority(self):
        return self._priority

    def get_status(self):
        return self._status

    def get_due_date(self):
        return self._due_date

    def get_comments(self):
        if not self._comments:
            return None
        else:
            formatted_comments = ""
            for comment in self._comments:
                formatted_comments += f"{comment}\n"

            return formatted_comments

    # Setters
    def set_task_id(self, task_id):
        self._task_id = task_id

    def set_title(self, title):
        self._title = title

    def set_description(self, description):
        self._description = description

    def set_responsible_user(self, responsible_user):
        self._responsible_user = responsible_user

    def set_project(self, project):
        self._project = project

    def set_category(self, category):
        self._category = category

    def set_priority(self, priority):
        self._priority = priority

    def set_status(self, status):
        self._status = status

    def set_due_date(self, due_date):
        converted = datetime.strptime(due_date, "%Y-%m-%d").date()
        if converted <= date.today():
            raise ValueError("Due date must be in the future")
        self._due_date = converted

    # Functionality
    def add_comment(self, comment):
        self._comments.append(comment)

    def show_info(self):
        print(f"Task ID: {self.get_task_id()}\t"
              f"Title: {self.get_title()}\t"
              f"Description: {self.get_description()}\t"
              f"Category: {self.get_category()}\t"
              f"Priority: {self.get_priority()}\t"
              f"Status: {self.get_status()}\t"
              f"Due Date: {self.get_due_date()}\n"
              f"Comments: \n"
              f"\t{self.get_comments()}")
