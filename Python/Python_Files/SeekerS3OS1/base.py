from Shell import shell
from Calculator import calculator
from Settings import settings
from Python import python
import time
import os
import getpass
user1 = open("user1.txt", "r")
user1name = user1.read()
user1.close()
user2 = open("user2.txt", "r")
user2name = user2.read()
user2.close()
loginyn = 0
while True:
    while loginyn == 0:
        username = input("Username> ")
        if username == user1name:
            user1pass = open("user1pass.txt", 'r')
            password = input("Password> ")
            realpassword = user1pass.read()
            user1pass.close()
            if password == realpassword:
                time.sleep(1)
                print("Login successful")
                user1pass = None
                realpassword = None
                loginyn = 1
            else:
                print("Incorrect password.")
        elif username == user2name:
            user2pass = open("user2pass.txt", 'r')
            password = input("Password> ")
            realpassword = user2pass.read()
            user2pass.close()
            if password == realpassword:
                time.sleep(1)
                print("Login successful")
                user1pass = None
                realpass = None
                loginyn = 1
            else:
                print("Incorrect password.")
        else:
            print("Please enter a valid username")
    while loginyn == 1:
        operation = input("What would you like me to do? If you don't know what to do, type 'idk'. ")
        if operation == "idk":
            print("""
            Applications:
            shell: opens the shell
            calculator: runs the calculator.
            python: Runs the interactive Python shell
            settings: Manages this OS.
            
            Commands:
            logout: logs out of your account
            shutdown: Shuts down the program.
            """)
        elif operation == "shell":
            shell()
        elif operation == "logout":
            time.sleep(0.5)
            print("Logging out...")
            time.sleep(0.5)
            loginyn = 0
        elif operation == "shutdown":
            time.sleep(0.5)
            print("Shutting down...")
            time.sleep(0.5)
            quit()
        elif operation == "calculator":
            calculator()
        elif operation == "python":
            python()
        elif operation == "settings":
            settings()
        else:
            print("Please enter a valid command.")