package com.bridgelab.algorithm;

import java.util.Scanner;

public class Anagram {

	Scanner scan;
	String first, second;
	boolean bool[];
	int counter = 0;
	
	public Anagram(Scanner scan) {
		this.scan = scan;
	}
	
	public void checkAnagram() {
		System.out.println("Enter two string : ");
		first = scan.next();
		second = scan.next();	
		if(first.length() == second.length()) {
			bool = new boolean[second.length()];
			for(int j=0; j<second.length(); j++) bool[j] = false;
			for(int i=0; i<first.length(); i++) {
				for(int j=0; j<second.length(); j++) {
					if(first.charAt(i)==second.charAt(j) && bool[j]==false) {
						bool[j]=true;
						counter++;
					}
				}
			}
			if(counter==second.length()) {
				System.out.println("Strings are anagram.");
			} else {
				System.out.println("Strings are not anagram.");
			}
		}else {
			System.out.println("Strings are not anagram.");
		}
	}
}
