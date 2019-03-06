from OOPS.AddressBook.Service import Service


class AddressBook:
    def __init__(self):
        self.obj = Service()
        self.choice = (self.obj.create(), self.obj.open(), self.obj.save(), self.obj.save_as(), self.obj.add_person(),
                       self.obj.delete_person(), self.obj.edit_person(), self.obj.quit())

    def address_book(self):
        print("1.Create\n2.Open\n3.Save\n4.Save As\n5.Add Person\n6.Delete Person\n7.Edit Person\n8.Quit")
        choice = int(input("Select any choice : "))
        self.choice[choice]


obj = AddressBook()
obj.address_book()
