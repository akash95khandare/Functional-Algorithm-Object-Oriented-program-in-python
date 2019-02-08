package com.bridgelab.algorithm;

import java.util.Scanner;

public class Prime {

	Scanner scan;
	int range;
	Palindrome p =new Palindrome();
	
	public Prime(Scanner scan) {
		this.scan = scan;
	}
	
	public boolean isPrime(int n) {
		for(int i=2; i<n; i++) {
			if(n%i==0) return false;
		}
		return true;
	}
	
	public void getPrime() {
		System.out.println("Enter range");
		range = scan.nextInt();
		for(int i=2; i<=range; i++) {
			if(isPrime(i)) if(p.isPalendrome(i)) System.out.print(i+" ");
		}
	}
}
