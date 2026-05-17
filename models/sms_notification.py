from models.notification import Notification

class SmsNotification(Notification):
    def __init__(self, subject, description, detail, date_time, phone_number):
        super().__init__(subject, description, detail, date_time)
        self._phone_number = phone_number

    #Getters
    def get_phone_number(self):
        return self._phone_number

    #Setters
    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def send(self):
        print(f"Sending SMS Notification (subject='{self._subject}', "
              f"description='{self._description}', "
              f"detail='{self._detail}', "
              f"date_time='{self._date_time}', "
              f"phone_number='{self._phone_number}')")