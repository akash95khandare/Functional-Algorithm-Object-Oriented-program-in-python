package com.bridgeLab.dataStructure.calendar;

public class Month {

	String month[][] = new String[7][7];
	public void monthCreation() {
		month[0][0]="S";
		month[0][1]="M";
		month[0][2]="T";
		month[0][3]="W";
		month[0][4]="Th";
		month[0][5]="F";
		month[0][6]="S";
		for(int i=1; i<7; i++) {
			for(int j=0; j<7; j++) {
				month[i][j]="-";
			}
		}
	}
	
	public void display() {
		for(int i=0; i<7; i++) {
			for(int j=0; j<7; j++) {
				System.out.print(month[i][j]+" ");
			}
			System.out.println();
		}
	}
}
