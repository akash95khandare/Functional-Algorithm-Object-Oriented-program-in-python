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
	
	
}
