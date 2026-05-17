class User:
    def __init__(self, first_name, last_name, birth_date, email, position):
        self._first_name = first_name
        self._last_name = last_name
        self.set_birth_date(birth_date)
        self._email = email
        self._position = position

    # Getters
    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_birth_date(self):
        return self._birth_date

    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"

    def get_email(self):
        return self._email

    def get_position(self):
        return self._position

    # Setters
    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def set_birth_date(self, birth_date):
        from datetime import datetime
        if isinstance(birth_date, str):
            try:
                self._birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Invalid date format. Please use YYYY-MM-DD")
        else:
            self._birth_date = birth_date

    def set_email(self, email):
        self.validate_email(email)
        self._email = email

    def set_position(self, position):
        self._position = position

    # Functionality
    def validate_email(self, email):
        if not email:
            raise ValueError("Email cannot be empty")
        if "@" and "." not in email:
            raise ValueError("Invalid email format")

    def get_age(self):
        from datetime import date
        today = date.today()
        return today.year - self._birth_date.year - (
                (today.month, today.day) < (self._birth_date.month, self._birth_date.day))

    def show_info(self):
        print(f"Name : {self.get_first_name()}\t"
              f"Last Name : {self.get_last_name()}\t"
              f"Age : {self.get_age()}\t"
              f"Email : {self.get_email()}\t"
              f"Position : {self.get_position()}\n")