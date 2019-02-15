package com.bridgeLab.dataStructure.linkedList;

public class Stack {

	LinkedList stack = new LinkedList();
	public void push(String item) {
		stack.add(item);
	}
	
	public void pop() {
		stack.removeLast();
	}
	
	public String peak() {
		if(stack.isEmpty()) return "-1";
		String str = stack.getLast();
		return str;
	}
	
	public boolean isEmpty() {
		return stack.isEmpty();
	}
	
	public int size() {
		return stack.size();
	}
}
