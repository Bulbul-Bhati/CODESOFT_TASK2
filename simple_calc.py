"""Design a simple calculator with basic arithmetic operations. Prompt the user to input two numbers 
and an operation choice. Perform the calculation and display the result."""


a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))


print("---Choose the operation for calculation---")
print(" Enter:\n 1-Addition\n 2-Subtraction\n 3-Multiplication\n 4-Division\n")
choice = float(input(" Enter Your choice from 1 - 4:  "))

if choice == 1:
    print("Addition of first and second number is :", a+b)
elif choice == 2:
    print(" Subtraction of first and second number is:", a-b)    
elif choice == 3:
    print(" Multiplication of first and second number is:", a*b) 
elif choice == 4:
    print(" Division  of first and second number is:", a/b)           