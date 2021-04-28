from tkinter import *

#declaring global variable called mathematical expressions with an empty string
mathematical_expression= ""

###############################################################################
#
#   PART 1 - FUNCTIONS
#   1 -  Update mathematical expressions when user presses a button
#   2 -  Evaluate the final expression using Try/Except for error handling
#   3 -  Clear up the content in the text box
#
###############################################################################

#Function to update mathematical expressions
def updating_mathematical_expressions(number):
    global mathematical_expression #bringing the global variable so it can be used inside the function
    mathematical_expression= mathematical_expression + str(number) #string concatenation
    mathematical_equation.set(mathematical_expression) #using set method to set the value of the string

#Function to evaluate the final expression using Try/Except for error handling
def evaluating_mathematical_expressions():
    global mathematical_expression #bringing the global variable so it can be used inside the function
    try:
        total=str(eval(mathematical_expression)) #takes the expression, evaluates it and converts it to a string
        mathematical_equation.set(total) #shows the mathematical expression on the box
        mathematical_expression= "" #resets mathematical expression

    except: # If an error happens, then the except block will handle it
        mathematical_equation.set("Error")
        mathematical_expression="" #resets mathematical expression

#Function to clear up the content in the Text Box
def clearing_text_box():
    global mathematical_expression #bringing the global variable so it can be used inside the function
    mathematical_expression="" #resets mathematical expression
    mathematical_equation.set("") #deleting content from Text Box


###############################################################################
#
#   DRIVER CODE
#   1 - Creating GUI window and setting configuration
#   2 - Instanciating class StringVar to construct a string variable
#   3 - Creating an entry box to show the mathematical expressions
#   4 - Expression_box.grid (columnspan=4, ipadx=70)
#   5 - Placing widgets at respective positions in table-like structure
#   6 - Creating buttons and defining their positions in the window
#   7 - Starting GUI with a main loop
#
###############################################################################


if __name__ == "__main__":
    # creating GUI window
    gui = Tk()
    # Setting background colour
    gui.configure(background="pink")

    # Set the title
    gui.title("Basic Calculator")

    # Set the configuration
    gui.geometry("340x250")

    # Windows pad
    gui.config(padx=40,pady=40)

    # Preventing user from resizing the window
    gui.resizable(False,False)

    # Instanciating class StringVar to construct a string variable
    mathematical_equation = StringVar()

    # Creating an entry box to show the mathematical expressions
    expression_box=Entry(gui,textvariable=mathematical_equation)

    # The method grid will be used for placing widgets at respective positions in table-like structure
    expression_box.grid( columnspan=6, ipadx=56)

    # Creating buttons and defining their positions in the window

    button1 = Button(gui, text=' 1 ', font="lucida 8 bold", fg='black', bg='white',
                     command=lambda: updating_mathematical_expressions(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', font="lucida 8 bold", fg='black', bg='white',
                     command=lambda: updating_mathematical_expressions(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', font="lucida 8 bold", fg='black', bg='white',
                     command=lambda: updating_mathematical_expressions(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', font="lucida 8 bold", fg='black', bg='white',
                     command=lambda: updating_mathematical_expressions(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', font="lucida 8 bold", fg='black', bg='white',
                     command=lambda: updating_mathematical_expressions(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', font="lucida 8 bold", fg='black', bg='white',
                     command=lambda: updating_mathematical_expressions(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', font="lucida 8 bold", fg='black', bg='white',
                     command=lambda: updating_mathematical_expressions(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', font="lucida 8 bold", fg='black', bg='white',
                     command=lambda: updating_mathematical_expressions(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', font="lucida 8 bold", fg='black', bg='white',
                     command=lambda: updating_mathematical_expressions(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', font="lucida 8 bold", fg='black', bg='white',
                     command=lambda: updating_mathematical_expressions(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', font="lucida 8 bold", fg='black', bg='light gray',
                  command=lambda: updating_mathematical_expressions("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', font="lucida 8 bold", fg='black', bg='light gray',
                   command=lambda: updating_mathematical_expressions("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', font="lucida 8 bold", fg='black', bg='light gray',
                      command=lambda: updating_mathematical_expressions("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', font="lucida 8 bold", fg='black', bg='light gray',
                    command=lambda: updating_mathematical_expressions("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', font="lucida 8 bold", fg='black', bg='light gray',
                   command=evaluating_mathematical_expressions, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', font="lucida 8 bold", fg='black', bg='light gray',
                   command=clearing_text_box, height=1)
    clear.grid(row=6, column=0,columnspan=4,sticky="we")

    decimal = Button(gui, text='.', font="lucida 8 bold", fg='black', bg='light gray',
                     command=lambda: updating_mathematical_expressions('.'), height=1, width=7)

    decimal.grid(row=5, column=1)


    # starting GUI with a main loop, which will only break when the user closes the window

    gui.mainloop()
