package com.bridgeLab.dataStructure.linkedList;


public class LinkedList {

	Node head;
	public void add(int item) {
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
	
	public void remove(int item) {
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

	public boolean search(int item) {
		Node tempNode = head;
		 do{
			 
				if(tempNode.data==item) return true;
				tempNode = tempNode.next;
			}while(tempNode.next!=null);
		 return false;
	}

	public boolean isEmpty() {
		if(head==null) return true;
		else return false;
	}

	public int size() {
		Node tempNode = head;
		int count = 0;
		
		if(tempNode!=null) {
			do {
				count++;
				tempNode = tempNode.next;
			}while(tempNode.next!=null);
		}else return 0;
		return count+1;
	}

	public void display() {
		Node tempNode = head;
		while(tempNode.next!=null){
			System.out.println(tempNode.data+" ");
			tempNode = tempNode.next;
		}
		System.out.print(tempNode.data+"\n");
	}
}
