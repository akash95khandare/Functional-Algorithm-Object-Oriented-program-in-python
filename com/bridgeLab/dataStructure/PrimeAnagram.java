package com.bridgeLab.dataStructure;

import java.util.ArrayList;

import com.bridgeLab.dataStructure.linkedList.Queue;
import com.bridgelab.utility.Utility;

public class PrimeAnagram {

	public Queue primeAnagram() {
		Queue queue = new Queue();
		Utility u = new Utility();
		ArrayList arr = u.getPrimeNumberInRange(100);
		System.out.println(arr);
		for(int i=0; i<arr.size()-1; i++) {
			for(int j=i+1; j<arr.size(); j++) {
				if(u.isAnagram(String.valueOf(arr.get(i)),String.valueOf(arr.get(j)))) {
					queue.enqueue(String.valueOf(arr.get(i)));
				}
			}
		}
		return queue;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		PrimeAnagram p = new PrimeAnagram();
		Queue queue = p.primeAnagram();
		int len = queue.size();
		for(int i=0; i<len; i++) {
			System.out.print(queue.dequeueOne()+" ");
		}
	}

}
