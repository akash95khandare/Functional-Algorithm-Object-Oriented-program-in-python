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
	
	public boolean isBankUser(String name) {
		if(!bankUser.search(name)) {
			return true;
		}else {
			return false;
		}
	}
	
	
	public void restoreUserData() {
		Restore res = new Restore();
		String data[] = res.readFromFile().split(" ");
		for(int i=0; i<data.length-1; i+=2) {
			bankUser.add(data[i],Double.parseDouble(data[i+1]));
		}
	}
	
	public void storeUserData() {
		Restore res = new Restore();
		res.writeToFile(bankUser);
	}

}
