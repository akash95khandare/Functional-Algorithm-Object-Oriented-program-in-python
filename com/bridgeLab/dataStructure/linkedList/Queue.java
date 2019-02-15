package com.bridgeLab.dataStructure.linkedList;

import com.bridgeLab.dataStructure.banking.ListBank;

public class Queue {

	ListBank queue = new ListBank();
	
	public void enqueue(String name,double amount) {
		queue.add(name, amount);
	}
	
	public String dequeue() {
		return queue.returnAll();
	}	
	
	public int size() {
		return queue.size();
	}
}
