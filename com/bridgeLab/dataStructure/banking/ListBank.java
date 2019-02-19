package com.bridgeLab.dataStructure.banking;

import com.bridgeLab.dataStructure.banking.Node;
import com.bridgeLab.dataStructure.banking.data.Restore;
import com.bridgeLab.dataStructure.banking.entity.Customer;

public class ListBank {

	Node head;
	
	public void add(Customer cust) {
		Node newNode = new Node();
		newNode.cust = cust;
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

	public boolean search(Customer cust) {
		Node tempNode = head;
		while(tempNode!=null){
				if(tempNode.cust.getName().equals(cust.getName())) return true;
				tempNode = tempNode.next;
			}
		 return false;
	}

	public Customer getAmount(Customer cust) {
		Node tempNode = head;
		while(tempNode!=null){
				if(tempNode.cust.getName().equals(cust.getName())) return tempNode.cust;
				tempNode = tempNode.next;
			}
		 return null;
	}
	
	public Customer pollFirst() {
		Customer cust = head.cust;
		head = head.next;
		return cust;
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
			System.out.print(tempNode.cust.getName()+" ");
			tempNode = tempNode.next;
		}
	}
	
	public Customer getLast() {
		Node tempNode = head;
		while(tempNode.next!=null) {
			tempNode = tempNode.next;
		}
		return tempNode.cust;
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
		while(!tempNode.cust.getName().equals(name)) {
			tempNode = tempNode.next;
			if(tempNode==null) {
				System.out.println("User not available.");
			}
		}
		tempNode.cust.setAmount(amount);;
	}

	public void getUsersData() {
		Restore res = new Restore();
		String data[] = res.readFromFile().split(" ");
		for(int i=0; i<data.length-1; i+=2) {
			Customer cust = new Customer();
			cust.setName(data[i]);
			cust.setAmount(Double.parseDouble(data[i+1]));
			add(cust);
		}
	}
}
