package com.bridgelab.functional;

public class LeapYear {

	public void check(int year) {
		if(year%100==0) {
			if(year%400==0) {
				System.out.println("This is leap year :"+year);
			}else {
				System.out.println("This is not leap year :"+year);
			}
		}else if(year%4==0) {
			System.out.println("This is leap year :"+year);
		}else {
			System.out.println("This is not leap year :"+year);
		}
	}
}
