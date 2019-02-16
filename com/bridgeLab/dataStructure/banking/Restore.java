package com.bridgeLab.dataStructure.banking;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;

import com.bridgeLab.dataStructure.linkedList.LinkedList;

public class Restore {

	public String readFromFile() {
		BufferedReader br;
		String str;
		try{
			br = new BufferedReader(new FileReader("bank_user_data.txt"));
			str=br.readLine();
			String temp;
			while((temp=br.readLine())!=null) {
				str = str+" "+temp;
			}
			br.close();
			return str;
		}catch(Exception e) {
			e.printStackTrace();
		}
		return "None";
	}
	
	public void writeToFile(ListBank list) {
		BufferedWriter bw;
		try{
			bw = new BufferedWriter(new FileWriter("bank_user_data.txt"));
			int i=0;
			int n = list.size();
			System.out.println(list.size());
			while(i<n) {
				bw.write(list.returnAll()+" ");
				i++;
			}
			bw.flush();
			bw.close();
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
}
