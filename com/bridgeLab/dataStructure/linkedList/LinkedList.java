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
			if(tempNode.data!=item) {
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
				if(tempNode.data==item) return true;
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
}
