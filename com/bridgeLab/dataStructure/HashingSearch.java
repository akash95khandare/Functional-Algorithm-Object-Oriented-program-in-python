package com.bridgeLab.dataStructure;

import com.bridgeLab.dataStructure.linkedList.LinkedListInt;
import com.bridgelab.utility.Utility;

public class HashingSearch {

	public void hashingSearch(LinkedListInt list[], String[] num) {
		System.out.println("11111");
		for(int i=0; i<num.length; i++) {
			int number = Integer.parseInt(num[i]);
			int dec = number%11;
			System.out.println("22222");
			list[dec].sort(number);
		}
	}
	
	public void search(int number,LinkedListInt list[]) {
		int dec = number/11;
		if(list[dec].search(number)) {
			list[dec].remove(number);
			System.out.println("Remove..");
		}else {
			list[dec].sort(number);
			System.out.println("Added..");
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		HashingSearch h = new HashingSearch();
		LinkedListInt list[] = new LinkedListInt[11];
		Utility u = new Utility();
		IoFile io = new IoFile();
		String num[] = 	io.readFromFile("number.txt").split(" ");
		for (int i:Integer.parseInt(num)) {
			
		}
//		h.hashingSearch(list, num);
		int n =u.getInt("Enter a number for finding : ");
//		h.search(n, list);
//		for(int i=0; i<10; i++) {
//			io.writeToFile(list[i], "number.txt");
//		}
//		for(int i=0; i<10; i++) {
//			list[i].display();
//		}
	}

}
