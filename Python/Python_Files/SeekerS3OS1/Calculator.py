#The Calculator
#Version 0.0.3
#Created by xxxxxx Saggi
#Made for Seeker S3 OS1
version = "0.0.3"
import time
import os
def calculator():
    while True:
        problem = input("Enter problem> ")
        if " " in problem:
            try:
                num1, operator, num2 = problem.split( )
            except:
                print("Error while unpacking values. Please try again.")
            try:
                num1 = float(num1)
                num2 = float(num2)
                if operator == "+":
                    print(num1 + num2)
                elif operator == "-":
                    print(num1 - num2)
                elif operator == "*":
                    print(num1 * num2)
                elif operator == "/":
                    print(num1 / num2)
                elif operator == "**":
                    print(num1 ** num2)
                elif operator == "//":
                    print(num1 // num2)
                elif operator == "%":
                    print(num1 % num2)
                else:
                    print("Enter a valid problem.")
            except:
                print("Error while calculationg. Please try again.")
        elif problem == "quit":
            break
        elif problem == "help":
            print("Coming soon.")
        else:
            print("Enter a valid problem.")