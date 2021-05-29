import time
f = open("spam.txt", "a")
spammed_stuff = input("How much bytes do you want to add to the harddrive? ")
if spammed_stuff == "clear":
    f.close()
    f = open("spam.txt", "w")
    f.close()
    print("Deleted all extra spam. Closing app.")
    time.sleep(5)
    quit()
stuff = ""
try:
    spammed_stuff = int(spammed_stuff)
except:
    print("Enter an integer.")
    time.sleep(5)
    quit()
n = 0
print("Working...")
for i in range(int(spammed_stuff)):
    n = n + int(i)
    stuff = stuff + "z"
    print("Bytes added: " + str(i))
f.write(stuff)
print("added " + str(spammed_stuff) + " bytes of spam in the file spam.txt")