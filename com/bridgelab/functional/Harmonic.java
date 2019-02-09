package com.bridgelab.functional;

public class Harmonic {

	public int getIntValue(int n) {
		int value=0;
		for(int i=1; i<=n; i++) {
			value = value + (1/i);
		}
		return value;
	}
	
	
}
