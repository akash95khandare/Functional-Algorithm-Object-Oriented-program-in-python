package com.bridgelab.functional;

import java.util.Scanner;

public class Distance {

	public void euclideanDistance() {
		Scanner scan = new Scanner(System.in);
		int x = scan.nextInt();
		int y = scan.nextInt();
		System.out.println("Euclidean distance from (x,Y) to origin (0,0) is :\n"+Math.sqrt(Math.pow(x,x)+Math.pow(y, y)));
		scan.close();
	}
}
