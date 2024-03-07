// Author: Richard Remo Emmanuel
// ID: 20220862
// File name: CS112_T5_A1_20220862.cpp
//Program: 100 number game
// Version: 0.5
//Date: 1/march/2024
#include <iostream>
using namespace std;



int main() {
	// printing out message that welcome the users
	cout<<"Welcome to a 100 game"<<endl;
	// define two variable
	int total = 0;
	int player = 1;

    // while loop that allow how multiple time the program allow the users to enter number
	while (total < 100){
		int num;
		//print out message that indicate what player turn to enter a number
		cout<<"Player"<<player<<", enter a number from 1 to 10: ";
		// allow player to input a num
		cin>>num;
       
	    // check if the num input is less than 1 or greater than 10 , then print out the invalid input ----
		if(num < 1 || num > 10){
			cout<<"Invalid inout. Enter a number from 1 to 10."<<endl;
			continue;
		}
		// total takes the number of the input and add it self to itself, everytime the user enter a number
		total += num;

		// check if the total number reach 100 or more the print the out indicate which player wins
		if (total >= 100){
			cout<<"Player "<< player <<" wins!"<<endl;
			break;
		}
		// allow player turn by naming them player1 or player2
		player =(player == 1) ? 2 : 1;
	}
	return 0;
	
}    