package com.bridgeLab.dataStructure.banking;

import com.bridgeLab.dataStructure.banking.Node;

public class ListBank {

	Node head;
	public void add(String item) {
		Node newNode = new Node();
		newNode.name = item;
		newNode.next = null;
		
		if(head==null) head = newNode;
		else {
			Node tempNode = head;
			while(tempNode.next!=null) {
				tempNode = tempNode.next;
			}
			tempNode.next = newNode;
		}
	}
	
	public void add(String item,double amount) {
		Node newNode = new Node();
		newNode.name = item;
		newNode.amount = amount;
		newNode.next = null;
		
		if(head==null) head = newNode;
		else {
			Node tempNode = head;
			while(tempNode.next!=null) {
				tempNode = tempNode.next;
			}
			tempNode.next = newNode;
		}
	}
	
	public void remove(String item) {
		Node tempNode = head;
		Node previousNode = tempNode;
		 do{
			 if(head.name.hashCode()==item.hashCode()) {
				 head = tempNode.next;
			 }
			 else if(tempNode.name.hashCode()!=item.hashCode()) {
				previousNode = tempNode;
				tempNode = tempNode.next;
			}else {
				previousNode.next = tempNode.next;
				break;
			}
		}while(tempNode!=null);
	}	

	public boolean search(String item) {
		Node tempNode = head;
		while(tempNode!=null){
				if(tempNode.name.hashCode()==item.hashCode()) return true;
				tempNode = tempNode.next;
			}
		 return false;
	}

	public double getAmount(String item) {
		Node tempNode = head;
		while(tempNode!=null){
				if(tempNode.name.hashCode()==item.hashCode()) return tempNode.amount;
				tempNode = tempNode.next;
			}
		 return -1;
	}
	
	public String pollFirst() {
		String str = head.name;
		head = head.next;
		return str;
	}
	
	public String returnAll() {
		String str = head.name+" "+head.amount;
		head = head.next;
		return str;
	}
	
	public boolean isEmpty() {
		if(head==null) return true;
		else return false;
	}

	public int size() {
		Node tempNode = head;
		int count = 0;
		
		if(tempNode!=null) {
			while(tempNode!=null){
				count++;
				tempNode = tempNode.next;
			}
		}else return 0;
		return count;
	}

	public void display() {
		Node tempNode = head;
		while(tempNode!=null){
			System.out.print(tempNode.name+" ");
			tempNode = tempNode.next;
		}
	}
	
	public String getLast() {
		Node tempNode = head;
		while(tempNode.next!=null) {
			tempNode = tempNode.next;
		}
		return tempNode.name;
	}
	
	public void removeLast() {
		Node tempNode = head;
		Node previousNode = tempNode;
		if(tempNode.next==null) {
			head=null;
			return;
		}
		while(tempNode.next!=null) {
			previousNode = tempNode;
			tempNode = tempNode.next;
		}
		previousNode.next=null;
	}

	public void modifyAmount(String name,double amount) {
		Node tempNode = head;
		while(!tempNode.name.equals(name)) {
			tempNode = tempNode.next;
			if(tempNode==null) {
				System.out.println("User not available.");
			}
		}
		tempNode.amount = amount;
	}
}
