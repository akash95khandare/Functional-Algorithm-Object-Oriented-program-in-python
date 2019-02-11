package com.bridgelab.functional;

public class ToBinary {

	public static int toBinary(int n) {
		int arr[] = n/2<8?new int[4]:new int[8];
		int i=arr.length-1;
		while(i>=0) {
				int temp1 = n%2;
				n = n/2;
				arr[i] = temp1;
				i--;
		}
		i++;
		int binaryNo=0;
		while(i<arr.length) {
			binaryNo = (binaryNo*10)+arr[i];
			i++;
		}
		return binaryNo;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(ToBinary.toBinary(64));
	}

}
