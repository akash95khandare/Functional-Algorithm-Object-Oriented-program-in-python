package com.bridgelab.functional;

import java.util.Random;
import java.util.Scanner;


public class MainClass {
	
	public static void main(String[] args)throws Exception {
		Scanner scan = new Scanner(System.in);
//		LeapYear l=new LeapYear();
//		l.check(1996);
//		l.check(1961);
//		PowerOf2 power = new PowerOf2();
//		power.tableOfPowerOf2();
//		Harmonic h = new Harmonic();
//		System.out.println("Harmonic value is :"+h.getFloatValue(20));
//		PrimeFactor pf = new PrimeFactor();
//		pf.printPrimeFactor(33);
//		Array2D arr = new Array2D();
//		arr.printArray();
//		Distance d = new Distance();
//		d.euclideanDistance();
//		Stopwatch sw = new Stopwatch();
//		sw.start();
//		Thread.sleep(10000);
//		System.out.println(sw.elapseTime());
		TicTacToe t = new TicTacToe();
		t.ticTacToe();
//		Quadratic qu = new Quadratic();
//		qu.getRootOfX();
//		WindChill w = new WindChill(scan);
//		w.weather();
//		Anagram a =new Anagram(scan);
//		a.checkAnagram();
	}
}
