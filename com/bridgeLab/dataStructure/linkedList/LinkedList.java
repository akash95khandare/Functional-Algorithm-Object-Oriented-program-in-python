package com.bridgeLab.dataStructure.linkedList;


public class LinkedList {

	Node head;
	public void add(String item) {
		Node newNode = new Node();
		newNode.data = item;
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
			if(tempNode.data.hashCode()!=item.hashCode()) {
				previousNode = tempNode;
				tempNode = tempNode.next;
			}else {
				previousNode.next = tempNode.next;
				break;
			}
		}while(tempNode.next!=null);
	}	

	public boolean search(String item) {
		Node tempNode = head;
		while(tempNode!=null){
				if(tempNode.data.hashCode()==item.hashCode()) return true;
				tempNode = tempNode.next;
			}
		 return false;
	}

	public String pollFirst() {
		String str = head.data;
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
			System.out.print(tempNode.data+" ");
			tempNode = tempNode.next;
		}
	}

	public void addAfter(int pos) {
		for(int i=1; i<=pos; i++) {
			
		}
	}
	
	public void sort(String item) {
		Node newNode = new Node();
		newNode.data = item;
		newNode.next = null;
		if(head==null) {
			head = newNode;
		}else {
			System.out.println("1");
			Node tempNode = head;
			Node previousNode;
			 while(true) {
				System.out.println("2");
				if(Math.abs(head.data.hashCode())>Math.abs(item.hashCode())) {
					System.out.println("3");
					newNode.next=tempNode;
					head = newNode;
					break;
				}
				else if(Math.abs(tempNode.data.hashCode())>Math.abs(item.hashCode())) {
					newNode.next=tempNode;
					previousNode=tempNode;
					previousNode.next=newNode;
					tempNode = tempNode.next;
					break;
				}else {
					previousNode=tempNode;
					tempNode = tempNode.next;
				}
			}
			 tempNode.next=newNode;
//			previousNode.next=newNode;
		}
		
	}
}
