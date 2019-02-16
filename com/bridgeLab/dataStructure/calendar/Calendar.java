package com.bridgeLab.dataStructure.calendar;

public class Calendar {

	public void calendar() {
		Month month[] = new Month[12];
		for(int i=0; i<12; i++) {
			month[i] = new Month();
			month[i].monthCreation();
		}
		
		for(int i=0; i<12; i++) {
			month[i].display();
			System.out.println();
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Calendar calendar = new Calendar();
		calendar.calendar();
	}

}
