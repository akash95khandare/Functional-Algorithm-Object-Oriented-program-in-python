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
			str="";
			String temp;
			while((temp=br.readLine())!=null) {
				str = temp+" ";
			}
			br.close();
			System.out.println(str);
			return str;
		}catch(Exception e) {
			e.printStackTrace();
		}
		return "";
	}
	
	public void writeToFile(LinkedList list) {
		BufferedWriter bw;
		try{
			bw = new BufferedWriter(new FileWriter("abc.txt"));
			int i=0;
			while(i<list.size()) {
				bw.write(list.pollFirst());
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
			list.add(str[i]);
		}
		list.display();
		String st = u.getNext("Enter word");
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
