package com.bridgelab.algorithm;

public class Merge {

	
	
	public static void main(String args[]) {
		
		String str[] = {"K","H","U","E","T","U","C","A"};
		Merge m = new Merge();
		UtilityClass u =new UtilityClass();
		u.displayStringArr(str);
		m.mergeSort(str, 0, str.length-1);
		System.out.println();
		u.displayStringArr(str);
	}
}
