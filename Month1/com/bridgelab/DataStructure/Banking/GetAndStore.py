from com.bridgelab.DataStructure.Banking.Customer import Customer


def data_transfer_file_to_list(user_list):
    f = open("bank_user_data.txt", 'r')
    temp = ""
    for i in f:
        temp += i
    data = temp.split("\n")
    for i in range(len(data) - 1):
        cust = Customer()
        cust.set_account_no(data[i].split(" ")[0])
        cust.set_customer_name(data[i].split(" ")[1])
        cust.set_amount(data[i].split(" ")[2])
        user_list.add(cust)


def data_transfer_list_to_file(user_list):
    f = open("bank_user_data.txt", 'w')
    for i in range(user_list.size()):
        cust = Customer()
        cust = user_list.poll_first()
        f.write(cust.toString() + "\n")
