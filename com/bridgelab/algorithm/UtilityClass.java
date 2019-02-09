package com.bridgelab.algorithm;

public class UtilityClass {

	

	
	
	public static void main(String args[]) {
		Long start;
		UtilityClass u = new UtilityClass();
		int intArr[] = {10,5,2,6,45,78,952,1,2,6};
		String strArr[] = {"B","F","S","K","E","J","LA"};
		start = System.currentTimeMillis();
//		u.insertionSortInt(intArr, 0, intArr.length-1);
//		u.bubbleSortInt(intArr, 0, intArr.length-1);
//		System.out.println(System.currentTimeMillis()-start);
//		u.display(intArr);
//		start = System.currentTimeMillis();
//		System.out.println("\n"+u.binarySearchInt(intArr, 0, intArr.length-1,78));
//		System.out.println(System.currentTimeMillis()-start);	
		
		u.insertionSortStr(strArr, 0, strArr.length-1);
		System.out.println(System.currentTimeMillis()-start);
		u.displayStringArr(strArr);
		start = System.currentTimeMillis();
		System.out.println("\n"+u.binarySearchStr(strArr, 0, intArr.length-1,"K"));
		System.out.println(System.currentTimeMillis()-start);
	}
}
