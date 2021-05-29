passwordlist = []
textlist = []
finallist = []
global magenumber
magenumber = 1
def encrypt(password, text):
    global magenumber
    textlength = -1
    passwordlength = -1
    for i in password:
        n = ord(i)
        passwordlist.append(n)
        passwordlength = passwordlength + 1
    for i in text:
        n = ord(i)
        textlist.append(n)
        textlength = textlength + 1
    passwordlength = passwordlength + 1
    for i in range(0, passwordlength):
        magenumber = magenumber * passwordlist[i]
    for i in range(0, textlength):
        finallist.append(textlist[i] * magenumber)
    print(finallist)
def decrypt(password, text):
    text.strip("[]")
    text = text.split(", ")
    passwordlength = -1
    global magenumber
    magenumber = 1
    for i in password:
        n = ord(i)
        passwordlist.append(n)
        passwordlength = passwordlength + 1
    for i in range(-1, passwordlength):
        magenumber = magenumber * passwordlist[i]
    textlistlength = len(textlist)
    twamp = []
    for i in range(0, textlistlength):
        twamp.append(textlist[i] / magenumber)
    twamplength = len(twamp)
    for i in range(0, twamplength):
        d = chr(i)
        finallist.append(d)
    finalstuff = str(finallist)
    finalstuff.strip("[")
    finalstuff.strip("]")
    finalstuff.strip(", ")
    print(finalstuff)
password = input("Enter password: ")
text = input("Enter message: ")
what = input("Do you want to (e)ncrypt or (d)ecrypt? ")
if what == "e":
    encrypt(password, text)
elif what == "d":
    decrypt(password, text)