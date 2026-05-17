from abc import abstractmethod, ABC


class Notification(ABC):
    def __init__(self, subject, description, detail, date_time):
        self._subject = subject
        self._description = description
        self._detail = detail
        self._date_time = date_time

    # Getters
    def get_subject(self):
        return self._subject

    def get_description(self):
        return self._description

    def get_detail(self):
        return self._detail

    def get_date_time(self):
        return self._date_time

    # Setters
    def set_subject(self, subject):
        self._subject = subject

    def set_description(self, description):
        self._description = description

    def set_detail(self, detail):
        self._detail = detail

    def set_date_time(self, date_time):
        self._date_time = date_time

    @abstractmethod
    def send(self):
        pass  # Defined in the subclasses
