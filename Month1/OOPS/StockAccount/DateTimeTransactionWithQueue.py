"""
Overview : Maintain transaction of stock account with date and time
purpose : Maintain transaction by using queue
class name : TransactionQueue
author : Akash Khandare
date : 08/03/2019
"""

import json

from util.Queue import Queue


class TransactionQueue:
    def __init__(self):
        """
        Reading old transaction from transaction json file and maintain in queue
        """
        self.queue = Queue()
        with open("Transaction_queue.json") as data:
            try:
                temp = json.load(data)
            except Exception:
                pass
            else:
                for i in temp:
                    self.queue.enqueue(i)

    def transaction_queue(self, transaction, customer_name, company_name, no_of_share, cost, time):
        """
        Taking all data about stock account transaction and maintain in queue
        :param transaction: it is transaction like sell or buy
        :param customer_name: it is customer name
        :param company_name: it is company name
        :param no_of_share: it is no of share
        :param cost: total cost of share
        :param time: it is time of transaction
        """
        new_transaction = {"transaction": transaction, "customer_name": customer_name, "company_name": company_name,
                           "no_of_share": no_of_share, "cost": cost, "time": time}
        self.queue.enqueue(new_transaction)

    def save_transaction(self):
        """
        update transaction json file by queue
        """
        temp1 = []
        size = self.queue.size()
        for i in range(size):
            temp1.append(self.queue.dequeue())
        with open("Transaction_queue.json", 'w') as data:
            json.dump(temp1, data)


# Main method
if __name__ == "__main__":
    pass
