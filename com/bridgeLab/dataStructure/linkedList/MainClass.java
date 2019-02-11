package com.bridgeLab.dataStructure.linkedList;

public class MainClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		LinkedList l =new LinkedList();
		l.add(50);
		l.add(25);
		l.add(25);
		l.add(36);
		l.display();
		System.out.println(l.size());
		System.out.println(l.isEmpty());
		System.out.println(l.search(25));
		l.remove(25);
		l.display();
	}

}
