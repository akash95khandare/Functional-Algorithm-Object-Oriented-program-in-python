package com.bridgelab.algorithm;

public class Merge {

	public static void mergeSort(String[] str, int start, int end) {
		if(start<end) {
			int mid = (start + end)/2;
			mergeSort(str, start, mid);
			mergeSort(str, mid+1, end);
			merge(str, start, mid, end);
		}
	}
	
	public static void merge(String[] str, int start, int mid, int end) {
		int n1 = mid-start+1;
		int n2 = end-mid;
		int s = start;
		String[] tm1 = new String[n1];
		String[] tm2 = new String[n2];
		
		for(int i=0; i<n1; i++) {
			tm1[i] = str[s];
			s++;
		}
		for(int i=0; i<n2; i++) {
			tm2[i] = str[mid];
			mid++;
		}
		int i=0, j=0;
		while(i<n1 && j<n2) {
			if(Math.abs(tm1[i].hashCode())<Math.abs(tm2[j].hashCode())) {
				str[start] = tm1[i];
			}else {
				str[start] = tm2[j];
			}
		}
		
		
	}
}
