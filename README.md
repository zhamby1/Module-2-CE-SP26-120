# Notes for Module 2

## Constants

Constants are named values that do NOT change throughout the running of a program

A variable can change

```
x = 7
x = 10 // the value of x is now 10
```

Constant values should not or do not change after declaration... some programming languages do not use constants or cannot prevent constants from being changed...instead constants are defined by a naming convention.

Why use constants? Preventing what we call a 'magic number' problem

A magic number is a raw value (numerical) that does not have a name and can be confusing on what it's purpose is

Sales tax is a good example of using a constant.  Let's say we have a program that calculates sales tax at the end of a transaction

```
total = 80.00
total_with_tax = total + (total * 0.06)  
// 0.06 is our magic number 
```
A better way to calculate this would be the following:

```
SALES_TAX = 0.06
total = 80.00
total_with_tax = total + (total * SALES_TAX)
```
Declaring a variable does not always require a value

```
string x or x
x = 0
x = ""
```

When you add value to a variable upon declaration, this is known as initializing

```
x = 10 //intializing
```

## Type Safety and Data Types
All data in programming have types.  They are usually divided between numerical and string types.  Numerical types are then futher divided into different types of data.

They numerical data types we will need to know for this class are the following:

- integer(int) - Numerical type that is a whole number

- float - Numerical type that contains a decimal

- string - non-numerical data or text

- boolean(bool) - True or False

Some languages employ type safety or "strongly-typed" data types.  This means that you must declare the type of data before naming the variable

Example

```
int x = 7
// x is a whole number, so we use the integer data type
```
```
float x = 8.9
// 8.9 is a float because it contains a decimal
```
```
string name = "Zach"
````

inputs (more about this is a minute) must take into consideration what type of value we are EXPECTING from a user in a strongly typed language

```
input string name
//I am expecting text...so we declare the type as string
```

## Inputs 
Inputs are a special case when it comes to type safety and data types.  In most (if not all) programming languages, data comes in as a string for inputs

```
input first_number - this would come in as a string
```

When working in pseduocode or flowcharting this is not much of a problem because we make some assumptions.  (ie the first_number variable comes in as a float or a integer)

However, when working with an actual language, it is important because strings cannot be calculated or be used by arithmetic.

Thus, we have to convert our inputs into other data types, like floats or ints.

Often times, languages have some type of built-in function or keyword that allow to convert

Here is an example in python to convert input into a integer

```python
first_number = input("What is your first number?")
first_number_conv = int(first_number)

#this will take the first_number and convert it to something that can be calculated aka an int
```

Often we just do this in one step like the example below

```python
first_number = int(input("What is your first number?"))
```



