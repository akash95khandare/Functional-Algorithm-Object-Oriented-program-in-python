package com.bridgeLab.dataStructure.banking;

import com.bridgeLab.dataStructure.linkedList.Queue;
import com.bridgelab.utility.Utility;

public class Users {

	static Queue queue = new Queue();
	static String work[];
	int index=0;
	Utility u =new Utility();
	
	public void UserEnterInQueue() {
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
		bank.restoreUserData();
		if(bank.isBankUser(str[0])) {
			System.out.println("Welcome in bank system");
			System.out.println(str[0]+", your account not available. First you should be created account");
			String name = u.getNext("Enter your name for creating account: ");
			bank.createAccount(name);
			System.out.println("Account created..");
		}
		if(work[index].equals("withdraw")) {
			bank.withdraw(str[0],Double.parseDouble(str[1]));
			index++;
		}else if(work[index].equals("deposit")) {
			bank.deposit(str[0],Double.parseDouble(str[1]));
			index++;
		}
		
		bank.storeUserData();
	}
	
	public static void main(String args[]) throws InterruptedException {
		Users user = new Users();
		user.UserEnterInQueue();
		int size = queue.size();
		for(int i=0; i<size; i++) {
			user.Casher();
			System.out.println("Success");
			Thread.sleep(2000);
		}
		
	}
}
