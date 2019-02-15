package com.bridgeLab.dataStructure.banking;

import com.bridgelab.utility.Utility;

public class Banking {

	static ListBank bankUser = new ListBank();
	Utility u = new Utility();
	
	public void createAccount(String name) {
		bankUser.add(name,0.0);
	}
	
	public void withdraw(String name,double amount) {
		if(bankUser.getAmount(name)>=amount) {
			double newAmt = bankUser.getAmount(name)-amount;
			bankUser.modifyAmount(name, newAmt);
			System.out.println("Available amount is : "+bankUser.getAmount(name));
			System.out.println("Collect the cash..");
		}
		else {
			System.out.println("Insufficient balance.");
		}
	}
	
	public void deposit(String name, double amount) {
		double newAmt = bankUser.getAmount(name) + amount;
		bankUser.modifyAmount(name, newAmt);
	}
	
	public void bankSystem() {
		System.out.println("Welcome in bank system");
		String name = u.getNext("Enter your name : ");
		if(!bankUser.search(name)) {
			createAccount(name);
			System.out.println("Account created..");
			bankSystem();
		}else {
			System.out.println("1. Withdraw\n2. Deposit");
			int choice = u.getInt("Select one of that : ");
			switch(choice) {
				case 1:
					double amt = u.getDouble("Enter amount for deposit : ");
					withdraw(name,amt);
					break;
				case 2:
					double amount = u.getDouble("Enter amount for deposit : ");
					deposit(name, amount);
					System.out.println("Deposit done.");
					break;
			}
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Banking bank = new Banking();
		Restore res = new Restore();
		String data[] = res.readFromFile().split(" ");
		for(int i=0; i<data.length-1; i+=2) {
			bankUser.add(data[i],Double.parseDouble(data[i+1]));
		}
		bank.bankSystem();
		res.writeToFile(bankUser);
	}

}
