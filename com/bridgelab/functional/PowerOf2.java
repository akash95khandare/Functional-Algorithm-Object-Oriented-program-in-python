package com.bridgelab.functional;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class PowerOf2 {
	
	int number;
	public void get() {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
		number = Integer.parseInt(br.readLine());
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void tableOfPowerOf2() {
		get();
		if(number<31) {
			for(int i=1; i<=number; i++) {
				int temp = 1;
				for(int j=1; j<i; j++) temp = temp*2;
				System.out.println(i+" is power of 2 : "+temp);
			}
		}else {
			System.out.println("You have enter greater number than 31..");
		}
	}
}
