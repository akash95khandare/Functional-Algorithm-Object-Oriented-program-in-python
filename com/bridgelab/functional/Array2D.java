package com.bridgelab.functional;

import java.io.PrintWriter;
import java.util.Scanner;

public class Array2D {

	int arr[][];
	int r, c;
	public void getArray() {
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter row and coloumn : ");
		r = scan.nextInt();
		c = scan.nextInt();
		arr = new int[r][c];
		System.out.println("Enter array element : ");
		for(int i=0; i<r; i++) {
			for(int j=0; j<c; j++) {
				arr[i][j]=scan.nextInt();
			}
		}
		scan.close();
	}
	
	public void printArray() {
		PrintWriter writer = new PrintWriter(System.out);
		for(int i=0; i<r; i++) {
			for(int j=0; j<c; j++) {
				try {
					writer.print(arr[i][j]);
					writer.flush();
				} catch(Exception e) {}
					System.out.print(" ");
			}
			System.out.println();
		}
        writer.close();
	}
}
