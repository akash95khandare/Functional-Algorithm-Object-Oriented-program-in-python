package com.bridgeLab.dataStructure.linkedList;

import com.bridgeLab.dataStructure.banking.ListBank;

public class Queue {

	ListBank queue = new ListBank();
	
	public void enqueue(String name, double amount) {
		queue.add(name, amount);
	}
	
	public void enqueue(String name) {
		queue.add(name);
	}
	
	public String dequeueOne() {
		return queue.pollFirst();
	}
	
	public String dequeue() {
		return queue.returnAll();
	}
	
	public int size() {
		return queue.size();
	}
}
