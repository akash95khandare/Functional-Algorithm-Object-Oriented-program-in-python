class CliniqueService:
    def __init__(self):
        pass

    def add_doctor(self):
        try:
            id = input("Enter id : ").strip()
            name = input("Enter name : ").strip()
            specialization = input("Enter specialization : ").strip()
            available_from = input("Enter available from :").strip()
            available_to = input("Enter available to : ").strip()
            if not id.isnumeric() and not name.is

    def add_patient(self):
        id = input("Enter id : ").strip()
        name = input("Enter name : ").strip()
        mobile_number = input("Enter mobile number : ").strip()
        age = input("Enter age : ").strip()

