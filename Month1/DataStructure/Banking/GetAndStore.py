from DataStructure.Banking import Customer


def data_transfer_file_to_list(user_list):
    """
    :param user_list: Take one parameter as link list
    read data from bank_user_data.txt file and store in linked list
    """
    f = open("bank_user_data.txt", 'r')
    temp = ""
    for i in f:
        temp += i
    data = temp.strip().split("\n")

    for i in range(len(data)-1):
        cust = Customer()
        cust.set_account_no(data[i].split(" ")[0])
        cust.set_customer_name(data[i].split(" ")[1])
        cust.set_amount(data[i].split(" ")[2])
        user_list.add(cust)


def data_transfer_list_to_file(user_list):
    """
    :param user_list: Take one parameter as link list
    write data in bank_user_data.txt file from linked list
    """
    f = open("bank_user_data.txt", 'w')
    size = user_list.size()
    for i in range(size):
        cust = Customer()
        cust = user_list.poll_first()
        f.write(cust.to_string() + "\n")
