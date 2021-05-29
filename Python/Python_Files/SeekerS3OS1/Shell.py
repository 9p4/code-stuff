#The Seeker S3 OS shell
#Made for Seeker S3 OS1
#Version 0.0.3
#For more information, read the "README" file.
#Created by: xxxxxx Saggi
version = "0.0.3"
import os
import time
import admin
def shell():
    time.sleep(0.5)
    print("Loading shell")
    time.sleep(0.5)
    print("""The Seeker S3 PowerShell
Created by: xxxxxx Saggi.
(c) Seeker S3
Version 0.0.3

Type "help" to acsess the help menu.""")
    os.chdir(os.getcwd())
    while True:
        command1 = None
        command2 = None
        directory = os.getcwd()
        command = input(directory + "> ")
        command3 = command
        if ' ' in command:
            command1, command2 = command.split(" ", 1)
        if command1 == "cd":
            try:
                os.chdir(command2)
            except:
                print("Please enter a valid path.")
        elif command3 == "cd":
            print(directory)
        elif command1 == "run":
            try:
                os.startfile(command2)
            except:
                print("Please enter a valid file.")
        elif command3 == "help":
            print("""
Commands:
cd: Changes the working directory. How to use: type "cd", then, type the name of the directory you want to enter.
example: "cd C:\" sends you to the "C:\" drive.

run: Runs a file using the default program. How to use: type "run", then, type the name of the file you want to run.
example: "run test.txt" runs the file "test.txt" using the default program

mkdir: Creates a folder in the current directory. How to use: type "mkdir", then, type the name of the new folder you want to make.
example: "mkdir poop" makes a folder called "poop" in the current directory.

list: Lists the files and folders in current directory. How to use: type "listdir".
    
quit: closes the program. How to use: type "quit".

help: Opens the help menu. How to use: type "help".
    
delete: deletes a file. How to use: type delete, then type the file you want to delete.
example: "delete test1.txt" deletes the file called "test1.txt".

admin: runs next command(s) ad admin.

    """)
        elif command1 == "mkdir":
            try:
                os.mkdir(command2)
            except:
                print("""
Directory creation failed. Please try again. If problem persists, try running this application as administator.
                """)
        elif command3 == "list":
            print(os.listdir())
        elif command3 == "quit":
            os.chdir(os.getcwd())
            break
        elif command1 == "delete":
            try:
                os.remove(command2)
            except:
                print("""
Deleting failed. Please try again. If problem persists, try running this application as administator.
                """)
        elif command == "admin":
            if not admin.isUserAdmin():
                admin.runAsAdmin(True)
            else:
                print("You are already admin.")
        else:
            print("""
Please enter a valid command
    """)