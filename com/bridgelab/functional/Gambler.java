package com.bridgelab.functional;

import java.util.Random;

import com.bridgelab.utility.Utility;

public class Gambler {

	public static void gambler(int goal) {
		int doller = 1;
		int win=0;
		int tMatch=0;
		Utility u = new Utility();
		Random rand = new Random();
		while(doller!=0) {
			System.out.println("Guess number :");
			int n = u.getInt();
			tMatch++;
			if(rand.nextInt(3)==n) {
				doller++;
				win++;
			} else doller--;
			if(doller==goal) System.out.println("You reached goal"); break;
		}
		if(doller==0) System.out.println("You loss your doller");
		System.out.println(tMatch);
		int temp = (win*100)/tMatch;
		System.out.println("Persentage of win : "+temp);
		System.out.println("Persentage of loss : "+(100-temp));
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Gambler.gambler(10);
	}

}
