from models.notification import Notification


class EmailNotification(Notification):
    def __init__(self, subject, description, detail, date_time, email):
        super().__init__(subject, description, detail, date_time)
        self._email = email

    # Getter
    def get_email(self):
        return self._email

    # Setter
    def set_email(self, email):
        self._email = email

    def send(self):
        print(f"Sending Email Notification (subject='{self._subject}', "
              f"description='{self._description}', "
              f"detail='{self._detail}', "
              f"date_time='{self._date_time}', "
              f"email='{self._email}')")
