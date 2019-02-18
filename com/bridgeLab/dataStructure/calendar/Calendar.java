package com.bridgeLab.dataStructure.calendar;

public class Calendar {

	public void calendar() {
		Month month = new Month();
		String mon[][] = month.monthCreation(1,2020);
		for(int i=0; i<7; i++) {
			for(int j=0; j<7; j++) {
				System.out.print(mon[i][j]+"   ");
			}
			System.out.println();
		}
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Calendar calendar = new Calendar();
		calendar.calendar();
	}

}
