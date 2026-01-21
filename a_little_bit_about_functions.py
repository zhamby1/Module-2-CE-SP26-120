#functions can also be used like modules or to summarize/repeat code
#we can take code, and stick it with a function name, and when we want to use a function, we can then call it by it's name
#for instance, we can create a function that sings happy birthday

#we have used functions that python has provided us so far, but we can make our own!
#we call this defining or creating a function
#after we give the function a name, we then put the code we want in it under the functions name indented
#we call this the function body

def happy_birthday():
    print("Happy Birthday To You")
    print("Happy Birthday To You")
    print("Happy Birthday Dear Zach")
    print("Happy Birthday To You")

#calling or using the function
happy_birthday()
happy_birthday()

#create a function that calculates total with tax
def cal_tax_total():
    SALES_TAX = 0.06
    total = float(input("Please give me the total of your transaction "))
    total_with_tax = total + (total * SALES_TAX)
    print("Your total with tax is",total_with_tax)

cal_tax_total()


# you can use module/functions to calculate a value and return it into a variable... then you can use it as other parts of your program

#to do this we use a keyword called return to return data outside of the function to a different variable
def cal_tax_total_return():
    SALES_TAX = 0.06
    total = float(input("Please give me the total of your transaction "))
    total_with_tax = total + (total * SALES_TAX)
    return total_with_tax

total_with_tax_var = cal_tax_total_return()
print(total_with_tax_var)