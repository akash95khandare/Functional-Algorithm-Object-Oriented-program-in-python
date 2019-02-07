package com.bridgelab.functional;

import java.io.OutputStreamWriter;

public class MainClass {
	
	public static void main(String[] args)throws Exception {
//		LeapYear l=new LeapYear();
//		l.check(1996);
//		l.check(1961);
//		PowerOf2 power = new PowerOf2();
//		power.tableOfPowerOf2();
//		Harmonic h = new Harmonic();
//		System.out.println("Harmonic value is :"+h.getFloatValue(20));
//		PrimeFactor pf = new PrimeFactor();
//		pf.printPrimeFactor(33);
		OutputStreamWriter osw = new OutputStreamWriter(System.out);
		osw.write("Print Array..");
		Array2D arr = new Array2D();
		arr.getArray();
		arr.printArray();
	}
}
