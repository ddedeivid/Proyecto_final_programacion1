class Client:
    def __init__(self, company_name, contact_name, contact_email, phone_number, business_sector):
        self._company_name = company_name
        self._contact_name = contact_name
        self._contact_email = contact_email
        self._phone_number = phone_number
        self._business_sector = business_sector

    # Getters
    def get_company_name(self):
        return self._company_name

    def get_contact_name(self):
        return self._contact_name

    def get_contact_email(self):
        return self._contact_email

    def get_phone_number(self):
        return self._phone_number

    def get_business_sector(self):
        return self._business_sector

    # Setters
    def set_company_name(self, company_name):
        self._company_name = company_name

    def set_contact_name(self, contact_name):
        self._contact_name = contact_name

    def set_contact_email(self, contact_email):
        self._contact_email = contact_email

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def set_business_sector(self, business_sector):
        self._business_sector = business_sector

    def show_info(self):
        print(f"Company name : {self.get_company_name()}\t"
              f"Contact name : {self.get_contact_name()}\t"
              f"Contact Email : {self.get_contact_email()}\t"
              f"Phone number : {self.get_phone_number()}\t"
              f"Business Sector : {self.get_business_sector()}\n")