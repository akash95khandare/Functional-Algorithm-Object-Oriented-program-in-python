import json

from util.Queue import Queue


class TransactionQueue:
    def __init__(self):
        self.queue = Queue()
        with open("Transaction_queue.json") as data:
            temp = json.load(data)
            for i in temp:
                self.queue.enqueue(i)

    def transaction_queue(self, transaction, customer_name, company_name, no_of_share, cost, time):
        new_transaction = {"transaction": transaction, "customer_name": customer_name, "company_name": company_name,
                           "no_of_share": no_of_share, "cost": cost, "time": time}
        self.queue.enqueue(new_transaction)

    def save_transaction(self):
        temp1 = []
        size = self.queue.size()
        for i in range(size):
            temp1.append(self.queue.dequeue())
        with open("Transaction_queue.json", 'w') as data:
            json.dump(temp1, data)
