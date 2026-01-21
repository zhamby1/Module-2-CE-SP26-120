# this is a comment
# variables in python are declared by saying variable_name = value
#python is not strongly typed, so when assigning a value, we do not worry about the data type
#this is a bit different when we talk about inputs later

#assignment/input
x = 7
y = 9

#processing
sum = x + y

# just like when flowcharting we can use the IPO (input-processing-output) to organize our program.
# when we have used raptor or pseudocode, we have used built in actions like output and input for our program
# in python we use functions - are actions that do something..where variables are the data that the function acts upon
# the functions we will use for now, are built into Python
#you can tell something is a function because they use ()

# x = 7 ..this a variable
# myfunction() ..this is a function

#one built in function that we will use is the print() function
#the print function is like the output symbol in flowcharting, as it displays something on screen.
#what you put in between the () is what gets printed on screen
# any data/variables that are put in the () are called arguments

#output
print(x)
print(y)
print(sum)
#you can also print raw values or strings
print("Hello")

#another function we will use is the input functions.  This is like the input action in flowcharting
#the argument/data in the input function describes the prompt that will be shown to the user with "" around it
# a prompt is a message to the user giving instruction on what data the program is asking for
#an input function must have a variable to return the data into that the user gives

#example
my_name = input("Give me your name ")
print(my_name)

#the issue with inputs is that they come in as strings
#If we need a calculable value, we have to convert the input data into a numerical type (parsing)

#HOW? There are two other functions we can use to convert data from one type to another
# int() - converts data into an integer
# float() - converts data into a float

#examples

#add two numbers together from input...these are whole numbers
first_number = int(input("Please give me your first number "))
second_number = int(input("Please give me your second number "))
mysum = first_number + second_number
print(mysum)

#floats work the same way but can convert decimals
#take two items using money and giving it a total
item1 = float(input("Please give me the amount of your first item "))
item2 = float(input("Please give me the amount of your second item "))
total = item1 + item2
print(total)

#just like with the output symbol in flowcharts, we can "flavor text" within the print statment to describe it better
#in python we use a comma to separate the flavor text and variable values
print("Your total is", total)