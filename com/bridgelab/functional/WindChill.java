package com.bridgelab.functional;

import java.util.Scanner;

public class WindChill {
	
	double t, v,w;
	Scanner scan;
	public WindChill(Scanner scan) {
		this.scan = scan;
	}
	
	public void weather() {
		System.out.println("Enter temperature less than 50 and enter wind speed between 3 to 120 : ");
		t = scan.nextDouble();
		v = scan.nextDouble();
		if(t<50 && v>3 && v<120) {
				w = (35.74 + 0.6215*t + (0.4275*t -35.75)*Math.pow(v, 0.16));
				System.out.println("Weather is : "+w);
		}else {
			System.out.println("You have entered wrong value.");
		}
		
	}
}
