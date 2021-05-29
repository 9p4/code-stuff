#Seeker S3 OS Settings application
#Made by: xxxxxx Saggi
#Made for Seeker S3 OS1
#Version 0.0.1
version = "0.0.1"
user1 = open("user1.txt", "r")
user1name = user1.read()
user1.close()
user2 = open("user2.txt", "r")
user2name = user2.read()
user2.close()
def settings():
    while True:
        settingscommand = input("Settings menu. Type in a command or help> ")
        if settingscommand == "change password":
            whopass = input("Who's password would you like to change? 1 for " + user1name + ", or 2 for " + user2name + "> ")
            if whopass == "1":
                password = ("Enter " + user1name + "'s current password> ")
                user1pass = open("user1pass.txt", "r")
                realpass = user1pass.read()
                if password == realpass:
                    newpass = input("Enter new password> ")
                    user1pass.close()
                    user1pass = open("user1pass.txt", "w")
                    user1pass.write(newpass)
                    user1pass.close()
                    newpass = None
                    password = None
                    realpass = None
                    print("Restart is required to save changes. Restarintg in 5 seconds.")
                    time.sleep(5)
                    quit()
                else: 
                    print("Incorrect password.")
            
            elif which == "2": 
                password = ("Enter " + user2name + "'s current password> ")
                user2pass = open("user2pass.txt", "r")
                realpass = user2pass.read()
                if password == realpass:
                    newpass = input("Enter new password> ")
                    user2pass.close()
                    user2pass = open("user2pass.txt", "w")
                    user2pass.write(newpass)
                    user2pass.close()
                    newpass = None
                    password = None
                    realpass = None
                    print("Restart is required to save changes. Restarintg in 5 seconds.")
                    time.sleep(5)
                    quit()
                
            else:
                print("Please enter a value from 1 to 2.")
        elif settingscommand == "quit":
            break
        else:
            print("Please enter a valid command.")
