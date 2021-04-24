# Basic Calculator in four versions 

This is a personal project constaining four versions of a basic calculator. It aims to present different approaches to perform the four basic arithmetic operations: addition, subtraction, multiplication and division, depending upon the user input. Next, I describe each version. 


## VERSION 1 -> Basic Calculator 1A.py

In this versions, user is asked to choose the desired operation and only two numbers are taken to perform the four basic arithmetic operations. User can also choose to see the history of previous calculations.

### Approach:

The code is divided in two parts: 

#####   Part 1: Functions
    1 -  Function to add two numbers
    2 -  Function to subtract two numbers
    3 -  Function to divide two numbers
    4 -  Function to multiply two numbers
    5 -  Function to store results and see previous calculations

 #####   Part 2: Interacting with user
    1 -  Infinite loop which will end with the break statement
    2 -  Taking input from user 

## VERSION 2 -> Basic Calculator 1B.py 

This is the refactored version of Basic Calculator 1A.   

## VERSION 3 -> Basic Calculator Version 2A.py 

This is an upgraded version with two new features: a) possibility to perform basic arithmetic operations with multiple numbers; b) history of previous calculations with date and time.
  
## VERSION 3 -> Basic Calculator 2B.py

This last version in a calculator in Python using Tkinter to build an interface. The code is divided in two parts: 

### Approach:

The code is divided in two parts:

####   Part 1: Functions
    1 -  Update mathematical expressions when user presses a button
    2 -  Evaluate the final expression using Try/Except for error handling
    3 -  Clear up the content in the Text Box


####   Part 2: Driver code 
    1 - Creating GUI window and setting configuration
    2 - Instanciating class StringVar to construct a string variable
    3 - Creating an entry box to show the mathematical expressions
    4 - Expression_box.grid (columnspan=4, ipadx=70)
    5 - Placing widgets at respective positions in table like structure
    6 - Creating buttons and defining their positions in the window
    7 - Starting GUI with a main loop


#### Demo

![print](BasicCalculator.PNG)

