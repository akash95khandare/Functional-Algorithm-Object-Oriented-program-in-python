package com.bridgeLab.dataStructure;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;

import com.bridgeLab.dataStructure.linkedList.LinkedList;
import com.bridgelab.utility.Utility;

public class UnOrderedList {

	public String readFromFile() {
		BufferedReader br;
		String str;
		try{
			br = new BufferedReader(new FileReader("abc.txt"));
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
	
	public void writeToFile(LinkedList list) {
		BufferedWriter bw;
		try{
			bw = new BufferedWriter(new FileWriter("abc.txt"));
			int i=0;
			int n = list.size();
			System.out.println(list.size());
			while(i<n) {
				System.out.print(list.pollFirst().hashCode()+" ");
//				bw.write(list.pollFirst()+" ");
				i++;
			}
			bw.flush();
			bw.close();
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void unorderList() {
		String str[]=readFromFile().split(" ");
		Utility u = new Utility();
		LinkedList list = new LinkedList();
		for(int i=0; i<str.length; i++) {
			list.sort(str[i]);
		}
		list.display();
		String st = u.getNext("\nEnter word");
		if(list.search(st)) {
			list.remove(st);
		}else list.add(st);
		list.display();
		writeToFile(list);
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		UnOrderedList un = new UnOrderedList();
		un.unorderList();
	}

}
