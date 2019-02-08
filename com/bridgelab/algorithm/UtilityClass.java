package com.bridgelab.algorithm;

public class UtilityClass {

	public int binarySearchInt(int[] arr,int start, int end, int key) {
		int mid;
		while(start<end) {
			mid = (start+end)/2;
			if(arr[mid]<key) start = mid + 1;
			else if(arr[mid]>key) end = mid -1;
			else if(arr[mid]==key) return mid;
		}
		return -1;
	}
	
	public int binarySearchStr(String[] arr,int start, int end, String key) {
		int mid;
		while(start<end) {
			mid = (start+end)/2;
			if(arr[mid].hashCode()<key.hashCode()) start = mid + 1;
			else if(arr[mid].hashCode()>key.hashCode()) end = mid -1;
			else if(arr[mid]==key) return mid;
		}
		return -1;
	}
	
	public int[] insertionSortInt(int [] arr, int start, int end) {
		for(int i=1; i<=end; i++)
			for(int j=i-1; j>=0; j--) {
				if(arr[j]>arr[j+1]) {
					int temp = arr[j];
					arr[j] = arr[j+1];
					arr[j+1] = temp;
				}
			}
		return arr;
	}
	
	public String[] insertionSortStr(String [] arr, int start, int end) {
		for(int i=1; i<=end; i++)
			for(int j=i-1; j>=0; j--) {
				if(arr[j].hashCode()>arr[j+1].hashCode()) {
					String temp = arr[j];
					arr[j] = arr[j+1];
					arr[j+1] = temp;
				}
			}
		return arr;
	}
	
	public int[] bubbleSortInt(int[] arr, int start, int end) {
		for(int i=0; i<=end; i++)
			for(int j=0; j<end-i; j++) {
				if(arr[j]>arr[j+1]) {
					int temp = arr[j];
					arr[j] = arr[j+1];
					arr[j+1] = temp;
				}
			}
		return arr;
	}
	
	public String[] bubbleSortStr(String[] arr, int start, int end) {
		for(int i=0; i<=end; i++)
			for(int j=0; j<end-i; j++) {
				if(arr[j].hashCode()>arr[j+1].hashCode()) {
					String temp = arr[j];
					arr[j] = arr[j+1];
					arr[j+1] = temp;
				}
			}
		return arr;
	}

	public void displayIntArr(int[] arr) {
		for(int i=0; i<arr.length; i++) System.out.print(arr[i]+" ");
	}
	
	public void displayStringArr(String[] arr) {
		for(int i=0; i<arr.length; i++) System.out.print(arr[i]+" ");
	}
	
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
