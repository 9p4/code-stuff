import time
Secs = input("Please enter the amout of seconds you want the loading sign to go. ")
try:
    Secs = int(Secs)
except:
    print("Please enter an integer.")
    time.sleep(5)
    quit()
while True:  
    b = "Loading" + "."
    print (b, end="\r")
    time.sleep(0.5)
    b = "Loading" + ".."
    print (b, end="\r")
    time.sleep(0.5)
    b = "Loading" + "..."
    print (b, end="\r")
    time.sleep(0.5)