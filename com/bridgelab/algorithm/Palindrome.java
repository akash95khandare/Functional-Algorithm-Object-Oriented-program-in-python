package com.bridgelab.algorithm;

public class Palindrome {

	public boolean isPalendrome(int n) {
		int revNo=0;
		int temp1, temp2=n; 
		while(true) {
			temp1 = temp2%10;
			temp2 = temp2/10;
			revNo = (revNo*10)+temp1;
			if(temp2==0) {
				break;
			}
		}
		if(n==revNo) return true;
		else return false;
	}
}
