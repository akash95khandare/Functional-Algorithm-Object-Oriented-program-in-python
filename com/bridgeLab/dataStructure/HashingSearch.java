package com.bridgeLab.dataStructure;

import java.io.FileWriter;
import java.io.IOException;

import com.bridgeLab.dataStructure.linkedList.LinkedListInt;
import com.bridgelab.utility.Utility;

public class HashingSearch {

	public void hashingSearch(LinkedListInt list[], String[] num) {
		for(int i=0; i<num.length; i++) {
			int number = Integer.parseInt(num[i]);
			int dec = number%11;
			list[dec].sort(number);
		}
	}
	
	public void search(int number,LinkedListInt list[]) {
		int dec = number%11;
		if(list[dec].search(number)) {
			list[dec].remove(number);
			System.out.println("Remove..");
		}else {
			list[dec].sort(number);
			System.out.println("Added..");
		}
	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		HashingSearch h = new HashingSearch();
		LinkedListInt list[] = new LinkedListInt[11];
		Utility u = new Utility();
		IoFile io = new IoFile();
		String num[] = 	io.readFromFile("number.txt").split(" ");
		for(int i=0; i<11; i++) {
			list[i] = new LinkedListInt();
		}
		h.hashingSearch(list, num);
		for(int i=0; i<11; i++) {
			if(list[i].size()==0) {
				continue;
			}
			list[i].display();
			System.out.println();
		}
		int n =u.getInt("Enter a number for finding : ");
		h.search(n, list);
		FileWriter fw = new FileWriter("number.txt");
		fw.write("");
		fw.close();
		for(int i=0; i<11; i++) {
			if(list[i].size()==0) {
				continue;
			}
			list[i].display();
			System.out.println();
		}
		for(int i=0; i<11; i++) {
			if(list[i].size()==0) {
				continue;
			}
			io.appendToFile(list[i], "number.txt");
		}
	
	}

}
