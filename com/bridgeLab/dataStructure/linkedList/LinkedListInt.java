package com.bridgeLab.dataStructure.linkedList;

public class LinkedListInt {

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
			 if(head.data==item) {
				 head = tempNode.next;
			 }
			 else if(tempNode.data!=item.) {
				previousNode = tempNode;
				tempNode = tempNode.next;
			}else {
				previousNode.next = tempNode.next;
				break;
			}
		}while(tempNode!=null);
	}	

	public boolean search(int item) {
		Node tempNode = head;
		while(tempNode!=null){
				if(tempNode.data==item) return true;
				tempNode = tempNode.next;
			}
		 return false;
	}

	public int pollFirst() {
		int str = head.data;
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

	public void addAfter(Node previousNode,Node newNode) {
		newNode.next=previousNode.next;
		previousNode.next=newNode;
	}
	
	public void sort(int item) {
		Node newNode = new Node();
		newNode.data = item;
		newNode.next = null;
		if(head==null) {
			head = newNode;
		}else {
			Node tempNode = head;
			Node previousNode=head;
			if(head.data>item) {
				newNode.next = tempNode;
				head = newNode;
			}else {
				while(true) {
					if(tempNode.data>item) {
						addAfter(previousNode, newNode);
						break;
					}
					else if(tempNode.next==null && tempNode.data<item) {
						tempNode.next=newNode;
						break;
					}
					if(tempNode.next==null) {
						break;
					}
					previousNode = tempNode;
					tempNode = tempNode.next;
				}
			}
		}
	}
}
