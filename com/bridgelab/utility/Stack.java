package com.bridgelab.utility;


public class Stack {

	LinkedList stack = new LinkedList();
	public void push(String item) {
		stack.add(item);
	}
	
	public void pop() {
		stack.removeLast();
	}
	
	public Object peak() {
		if(stack.isEmpty()) return "-1";
		Object obj = stack.getLast();
		return obj;
	}
	
	public boolean isEmpty() {
		return stack.isEmpty();
	}
	
	public int size() {
		return stack.size();
	}
}
