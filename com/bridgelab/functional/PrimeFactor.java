package com.bridgelab.functional;

public class PrimeFactor {

	public void printPrimeFactor(int n) {
		System.out.println("Prime Factor are :");
		for(int i=2; i<=n; i++) {
			if(n%i==0) {
				if((i!=2 && i!=3 && i!=5) && (i%2==0 || i%3==0 || i%5==0)) {}
				else System.out.print(i+","); 
			}
		}
	}
}
