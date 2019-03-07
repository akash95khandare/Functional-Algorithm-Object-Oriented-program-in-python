from OOPS.AddressBook.Service import Service


class AddressBook:
    def __init__(self):
        self.obj = Service()

    def address_book(self):
        while True:
            print("1.Create\n2.Open\n3.Save\n4.Save As\n5.Add Person\n6.Delete Person\n7.Edit Person\n8.Quit")
            try:
                choice_selected = int(input("Select any choice : "))
            except Exception:
                print("You have enter wrong input.")
                continue
            if choice_selected == 8:
                print("Exited")
                break
            elif choice_selected > 8:
                print("You have selected wrong choice.")
                continue

            choice = {1: "create", 2: "open", 3: "save", 4: "save_as",
                      5: "add_person", 6: "delete_person", 7: "edit_person"}
            fun = getattr(self.obj, choice[choice_selected])
            fun()


obj = AddressBook()
obj.address_book()
