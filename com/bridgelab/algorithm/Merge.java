package com.bridgelab.algorithm;

import com.bridgelab.utility.Utility;

public class Merge {

	public static void main(String args[]) {
		
		String str[] = {"K","H","U","E","T","U","C","A"};
		Utility.displayStringArr(str);
		Utility.mergeSort(str, 0, str.length-1);
		System.out.println();
		Utility.displayStringArr(str);
	}
}
