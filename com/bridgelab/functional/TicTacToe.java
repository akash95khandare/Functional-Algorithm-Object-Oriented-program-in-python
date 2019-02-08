package com.bridgelab.functional;

import java.util.Random;
import java.util.Scanner;

public class TicTacToe {
	
	Scanner scan = new Scanner(System.in);
	boolean check = true;
	int player = 0;
	int x,y;
	int counter = 1;
	char game[][] = new char[][] {{'-','-','-'}, {'-','-','-'}, {'-','-','-'}}; 
	
	public void computer() {
		Random random = new Random();
		x = random.nextInt(3);
		y = random.nextInt(3);
		if(game[x][y]=='-') { game[x][y] = 'O'; return; }
		computer();
	}
	
	public void getPlayer() {
		System.out.println("do you want 1 player or 2 player..");
		player = scan.nextInt();
	}
	
	public void player() {
		display();
		System.out.println("Which position do you want to mark X");
		x = scan.nextInt();
		y = scan.nextInt();
		if(game[x][y]=='-') {
			game[x][y] = 'X'; 
			return; 
		} else {
			System.out.println("This position have already marked.");
			player();
		}
	}
	
	public void display() {
		for(int i=0; i<3; i++) {
			for(int j=0; j<3; j++) {
				System.out.print(game[i][j]+" ");
			}
			System.out.println();
		}
	}
	
	public void ticTacToe() {
		if(check) {
			if(counter <= 9) {
				if(player == 0) {
					display(); 
					getPlayer();
					ticTacToe();
				} else if(player == 1) {
					player();
					check('X');
					player = 2; 
					counter++; 
					ticTacToe();
				} else if(player == 2) {
					computer();
					check('O');
					player = 1; 
					counter++; 
					ticTacToe();
				}
			} else { 
				display();
				System.out.println("Draw Match.");
			} 
		}
	}
	
	public void check(char c) {
		if((game[0][0]==c && game[0][1]==c && game[0][2]==c) 
			|| (game[1][0]==c && game[1][1]==c && game[1][2]==c)
			|| (game[2][0]==c && game[2][1]==c && game[2][2]==c)
			|| (game[0][0]==c && game[1][0]==c && game[2][0]==c)
			|| (game[0][1]==c && game[1][1]==c && game[2][1]==c)
			|| (game[0][2]==c && game[1][2]==c && game[2][2]==c)
			|| (game[0][0]==c && game[1][1]==c && game[2][2]==c)
			|| (game[0][2]==c && game[1][1]==c && game[2][0]==c)) {
			if(c=='X') {
				System.out.println("player won.");
			} else {
				System.out.println("Computer player won.");
			}
			display();
			check = false;
		}
	}
}