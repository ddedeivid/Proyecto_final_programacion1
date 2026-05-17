class Project:
    def __init__(self, title, description, start_date, end_date, client, project_leader):
        self._title = title
        self._description = description
        self._start_date = start_date
        self._end_date = end_date
        self._client = client  # Object type: Client
        self._project_leader = project_leader  # Object type: User

    # Getters
    def get_title(self):
        return self._title

    def get_description(self):
        return self._description

    def get_start_date(self):
        return self._start_date

    def get_end_date(self):
        return self._end_date

    def get_client(self):
        return self._client

    def get_project_leader(self):
        return self._project_leader

    # Setters
    def set_title(self, title):
        self._title = title

    def set_description(self, description):
        self._description = description

    def set_start_date(self, start_date):
        self._start_date = start_date

    def set_end_date(self, end_date):
        self._end_date = end_date

    def set_client(self, client):
        self._client = client

    def set_project_leader(self, project_leader):
        self._project_leader = project_leader
