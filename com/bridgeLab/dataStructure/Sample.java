package com.bridgeLab.dataStructure;

import com.bridgeLab.dataStructure.linkedList.LinkedListInt;
import com.bridgeLab.dataStructure.linkedList.Stack;

public class Sample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Stack l = new Stack();
		l.push("A");
		l.push("b");	
		l.push("c");
		l.push("d");
		l.push("e");
		l.push("f");
		l.push("g");
		l.push("h");
		System.out.println(l.size());
		int n = l.size();
		System.out.println(l.isEmpty());
		for(int i =0; i<n;i++) {
			System.out.print(l.peak()+" ");
			l.pop();
		}
//		System.out.print(l.peak()+" ");
//		l.pop();
//		System.out.print(l.peak()+" ");
//		
		System.out.println(l.isEmpty());
	}

}
