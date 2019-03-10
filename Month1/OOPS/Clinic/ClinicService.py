import json


class ClinicService:
    def __init__(self):
        self.temp = []

    def add_doctor(self):
        id = input("Enter id : ").strip()
        name = input("Enter name : ").strip().upper()
        specialization = input("Enter specialization : ").strip().upper()
        available_from = input("Enter available from :").strip()
        available_to = input("Enter available to : ").strip()
        new_doctor = {"id": id, "name": name, "specialization": specialization, "available_from": available_from,
                      "available_to": available_to}

        with open("Doctor.json", 'w') as data:
            json.dump(new_doctor, data)
            data.close()

    def add_patient(self):
        id = input("Enter id : ").strip()
        name = input("Enter name : ").strip().upper()
        mobile_number = input("Enter mobile number : ").strip()
        age = input("Enter age : ").strip()
        new_patient = {"id": id, "name": name, "mobile_number": mobile_number, "age": age}
        with open("Patient.json", 'w') as data:
            json.dump(new_patient, data)
            data.close()

    def delete_doctor(self):
        id = input("Enter id : ").strip()
        name = input("Enter name : ").strip().upper()
        with open("Doctor.json") as data:
            self.temp = json.load(data)
            for i in range(len(self.temp)):
                if self.temp[i]["name"] == name and self.temp[i]["id"] == id:
                    self.temp.remove(self.temp[i])
                    break
            json.dump(self.temp, data)

    def delete_patient(self):
        id = input("Enter id : ").strip()
        name = input("Enter name : ").strip().upper()
        with open("Patient.json") as data:
            self.temp = json.load(data)
            for i in range(len(self.temp)):
                if self.temp[i]["id"] == id and self.temp[i]["name"] == name:
                    self.temp.remove(self.temp[i])
                    break
            json.dump(self.temp, data)

    def show_details(self, file_name):
        with open(file_name + ".json") as data:
            self.temp = json.load(data)
            for i in self.temp:
                print(i)
            data.close()

    def search(self, file_name):
        id = input("Enter id : ").strip()
        name = input("Enter name : ").strip().upper()
        with open(file_name + ".json") as data:
            self.temp = json.load(data)
            for i in range(len(self.temp)):
                if self.temp[i]["id"] == id and self.temp[i]["name"] == name:
                    print(self.temp[i])
                    flag = False

            if flag:
                print("Data not found.")

    def get_appointment(self):
        doctor_name = input("Enter doctor name : ").strip().upper()
        doctor_id = input("Enter doctor id : ").strip()
        patient_name = input("Enter patient name : ").strip().upper()
        patient_id = input("Enter patient id : ").strip()

    def search_by_name(self, name, file_name):
        with open(file_name+".json") as data:
            self.temp = json.load(data)
            for i in self.temp:
                if i["name"] == name:
                    print(i)
                    flag = False
                    break

            if flag:
                print("Data not found by name.")


    def search_by_id(self, id, file_name):
        pass

    def search_by_mobile_number(self, mobile_number, file_name):
        pass

    def search_by_specialization(self, specialization, file_name):
        pass
