package com.bridgeLab.dataStructure;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

import com.bridgeLab.dataStructure.linkedList.LinkedListInt;
import com.bridgeLab.dataStructure.linkedList.Stack;

public class Sample {

	public static void main(String[] args) throws IOException {
		FileWriter fw = new FileWriter("abc.txt",true);
		BufferedWriter bw = new  BufferedWriter(fw);
		PrintWriter pw = new PrintWriter(bw);
		pw.write(" akash");
		pw.write(" shubham");
		pw.write(" master");
		pw.flush();
		pw.close();
		bw.close();
	}
}
