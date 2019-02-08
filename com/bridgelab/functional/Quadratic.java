package com.bridgelab.functional;

import java.util.Scanner;

public class Quadratic {

	int a, b, c;
	double x1, x2;
	public void rootOfX() {
		
	}
	
	public void getRootOfX() {
		Scanner scan = new Scanner(System.in);
		System.out.println("Equation is a*x*x + b*x + c.");
		System.out.println("Enter a, b and c");
		a = scan.nextInt();
		b = scan.nextInt();
		c = scan.nextInt();
		double delta = (b*b - 4*a*c);
		x1 = ((-b + Math.sqrt(delta))/(2*a));
		x2 = ((-b - Math.sqrt(delta))/(2*a));
		System.out.println("Root 1 of x = "+(int)x1);
		System.out.println("Root 2 of x = "+(int)x2);
	}
}
