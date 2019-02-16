package com.bridgeLab.dataStructure;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;

import com.bridgeLab.dataStructure.linkedList.LinkedList;
import com.bridgeLab.dataStructure.linkedList.LinkedListInt;

public class IoFile {

	public String readFromFile(String fileName) {
		BufferedReader br;
		String str;
		try{
			br = new BufferedReader(new FileReader(fileName));
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
	
	public void writeToFile(LinkedList list,String fileName) {
		BufferedWriter bw;
		try{
			bw = new BufferedWriter(new FileWriter(fileName));
			int i=0;
			int n = list.size();
			System.out.println(list.size());
			while(i<n) {
				bw.write(list.pollFirst()+" ");
				i++;
			}
			bw.flush();
			bw.close();
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void writeToFile(LinkedListInt list,String fileName) {
		BufferedWriter bw;
		try{
			bw = new BufferedWriter(new FileWriter(fileName));
			int i=0;
			int n = list.size();
			System.out.println(list.size());
			while(i<n) {
				bw.write(list.pollFirst()+" ");
				i++;
			}
			bw.flush();
			bw.close();
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
}
