package com.bridgeLab.dataStructure.banking.util;

import com.bridgeLab.dataStructure.banking.ListBank;
import com.bridgeLab.dataStructure.banking.entity.Customer;
import com.bridgeLab.dataStructure.linkedList.LinkedList;

public class Queue {

	ListBank queue = new ListBank();
	LinkedList list = new LinkedList();
	
	public void enqueue(Customer cust) {
		System.out.println("Success");
		queue.add(cust);
	}
	
	public void enqueue(String name) {
		list.add(name);
	}
	
	public String dequeueOne() {
		return list.pollFirst();
	}
	
	public Customer dequeue() {
		return queue.pollFirst();
	}
	
	public void display() {
		queue.display();
	}
	
	public int size() {
		return queue.size();
	}
	
	public int sizeOfList() {
		return list.size();
	}
}
