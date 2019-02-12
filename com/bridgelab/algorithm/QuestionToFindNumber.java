package com.bridgelab.algorithm;

import com.bridgelab.utility.Utility;

public class QuestionToFindNumber {

	public static int binarySearchInt(int[] arr,int start, int end, int key) {
		int mid;
		while(start<end) {
			mid = (start+end)/2;
			if(arr[mid]<key) start = mid + 1;
			else if(arr[mid]>key) end = mid -1;
			else if(arr[mid]==key) return mid;
		}
		return -1;
	}
	private static void display(int a,int b) {
		for(int i=a+1;i<=b;i++) {
			System.out.print(i+" ");
		}
	}
	
	public static void questionToFindNumber() {
		Utility u = new Utility();
		int n = u.getInt("Enter N number : ");
		System.out.println("you think of a number between 0 and N­1");
		int k=1;
		int start = 0;
		int end = n, mid;
		boolean guess = false;
		while(true) {
			if(n<Math.pow(2,k)) {
				k--;
				break;
			}
			k++;
		}
		mid = (start+end)/2;
		while(start<end) {
			int l = u.getInt("Your number is "+mid+" or not.");
			if(l==1) break;
			display(start,mid);
			int i=u.getInt("Enter 1 for true and 2 for false.");
			if(i==1) {
				mid = (start+mid)/2;
			}else {
				start = mid+1;
				mid = end;
			}
			
		}
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		QuestionToFindNumber.questionToFindNumber();
	}

}
