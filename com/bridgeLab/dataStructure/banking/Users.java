package com.bridgeLab.dataStructure.banking;

import com.bridgeLab.dataStructure.linkedList.Queue;
import com.bridgelab.utility.Utility;

public class Users {

	static Queue queue = new Queue();
	String work[];
	int index=0;
	
	public void UserEnterInQueue() {
		Utility u =new Utility();
		int n = u.getInt("How many people will stay in queue");
		work = new String[n];
		for(int i=0; i<n; i++) {
			String name = u.getNext("Enter name : ");
			double amt = u.getDouble("Enter amount : ");
			work[i]=u.getNext("Enter work for as deposit or as withdraw");
			queue.enqueue(name, amt);
		}
	}
	
	public void Casher() {
		String str[]=queue.dequeue().split(" ");
		Banking bank = new Banking();
		if(work[index].equals("withdraw")) {
			bank.withdraw(str[0],Double.parseDouble(str[1]));
		}else if(work[index].equals("deposit")) {
			bank.deposit(str[0], Double.parseDouble(str[1]));
		}
	}
	
	public static void main(String args[]) throws InterruptedException {
		Users user = new Users();
		user.UserEnterInQueue();
		int size = queue.size();
		for(int i=0; i<size; i++) {
			user.Casher();
			System.out.println("Success");
			Thread.sleep(1000);
		}
	}
}
