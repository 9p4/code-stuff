from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import exifread
import webbrowser
from tkinter import messagebox
import os
import sys
import time
import platform
import getpass
#from geopy.geocoders import Nominatim
from tkinter import PhotoImage
#from geolocation.main import GoogleMaps
#import re
#gmaps = GoogleMaps(api_key="AIzaSyCqR38gBJKTtOSKBbnjOxYVmh9dBw_KJKI")
latitude = None
longitude = None
location = ""
daError = ""
url = ""
zzzzz = 1
global dZipCodePics
dZipCodePics = []
nameOfFile = "PicFinder"
global history
history = {}
root = Tk( )
global openMap
openMap = Button(root, text="", command = None, bg="#FDD9B5")
global label4
label4 = ttk.Label(root, text = "", foreground = "black", font = ("Helvetica", 12), background="white")
aboutThis = """
Version: 1.0
Realeased on July 22, 2016
Made by: xxxxxx M. Saggi
"""

def error():
    messagebox.showerror("Error!", "No coordinates detected.")

#Reads the picture and creates the coordinates.
def readPic(name):
    tags = exifread.process_file(name, details=False)

    lat = tags.get("GPS GPSLatitude", None)
    lat = str(lat)
    lat = lat.strip("[]")
    try:
        a, b, c = lat.split(", ")
    except:
        print("Error: No coordinates detected")
        a, b, c = 0, 0, 0

    try:
        a1, a2 = a.split("/")
        a1 = int(a1)
        a2 = int(a2)
        a = a1 / a2
    except:
        a = int(a)
        time.sleep(0)
    
    try:
        b1, b2 = b.split("/")
        b1 = int(b1)
        a2 = int(b2)
        b = b1 / b2
    except:
        b = int(b)
        time.sleep(0)
    
    try:
        c1, c2 = c.split("/")
        c1 = int(c1)
        c2 = int(c2)
        c = c1 / c2
    except:
        c = int(c)
        time.sleep(0)

    latitude = a + b/60 + c/3600

    "--------------------------------------------------------------------------------------------------------"

    long = tags.get("GPS GPSLongitude", None)
    long = str(long)
    long = long.strip("[]")
    try:
        a, b, c = long.split(", ")
    except:
        error()

    try:
        a1, a2 = a.split("/")
        a1 = int(a1)
        a2 = int(a2)
        a = a1 / a2
    except:
        a = int(a)
        time.sleep(0)

    try:
        b1, b2 = b.split("/")
        b1 = int(b1)
        a2 = int(b2)
        b = b1 / b2
    except:
        b = int(b)
        time.sleep(0)

    try:
        c1, c2 = c.split("/")
        c1 = int(c1)
        c2 = int(c2)
        c = c1 / c2
    except:
        c = int(c)
        time.sleep(0)

    longitude = a + b/60 + c/3600

    "--------------------------------------------------------------------------------------------------------"

    latitudeRef = tags.get("GPS GPSLatitudeRef", None)
    longitudeRef = tags.get("GPS GPSLongitudeRef", None)

    latitudeRef = str(latitudeRef)
    longitudeRef = str(longitudeRef)

    if latitudeRef == "S":
        latitude = str(latitude)
        latitude = "-" + latitude
    
    else:
        latitude = str(latitude)
    
    
    if longitudeRef == "W":
        longitude = str(longitude)
        longitude = "-" + longitude
    
    else:
        longitude = str(longitude)
    
    print("Latitude: " + latitude + ", Ref: " + latitudeRef)
    print("Longitude: " + longitude + ", Ref: " + longitudeRef)


    location = latitude + ", " + longitude
    
    if latitudeRef != "None":
        address = geolocator.reverse(location)
        address = str(address)
        print("Address: " + address)
        global zipCode
        spam1, zipCode, spam2 = address.rsplit(", ", 2)
        print("Zipcode: " + zipCode)

        fileLocation = str(name.name)
        history[fileLocation] = location
        print(history)


    "--------------------------------------------------------------------------------------------------------"

    #Opens the Map
    def openTheMap():
        url = "http://www.maps.google.com/maps/place/" + location
        webbrowser.open(url)

    locationtext = "Location: " + location
    
    global label4
    label4.pack_forget()
    label4 = ttk.Label(root, text = locationtext, foreground = "black", font = ("Helvetica", 12), background="white")
    label4.pack(side="bottom")
    
    global openMap
    openMap.pack_forget()
    openMap = Button(root, text="Open in Google Maps", command = openTheMap, bg="#FDD9B5")
    openMap.pack(side="bottom")
      

#OpenFile
def OpenFile():
    global name
    current_user = getpass.getuser()
    print("Current User: " + current_user)
    print("Current OS: " + platform.system())

    if platform.system() == "Windows":
        startingDir = "C:/Users/" + current_user + "/Pictures"
    elif platform.system() == "Mac":
        startingDir = "/Users/" + current_user + "/Photos"
    else:
        startingDir = "C:/"

    name = askopenfilename(initialdir=startingDir,
                           filetypes =(("JPG Files", "*.jpg"),("All Files","*.*")),
                           title = "Open File - PicFinder"
                           )
    print(name)
    try:
        with open(name,'rb') as f:
            try:
                readPic(f)
            except:
                print("Error: ")
                print(sys.exc_info())
            
    except:
        print("Error: ")
        print(sys.exc_info())

def readPicWithoutOutput(name):
    tags = exifread.process_file(name, details=False)

    lat = tags.get("GPS GPSLatitude", None)
    lat = str(lat)
    lat = lat.strip("[]")
    try:
        a, b, c = lat.split(", ")
    except:
        print("Error: No coordinates detected")
        a, b, c = 0, 0, 0

    try:
        a1, a2 = a.split("/")
        a1 = int(a1)
        a2 = int(a2)
        a = a1 / a2
    except:
        a = int(a)
        time.sleep(0)
    
    try:
        b1, b2 = b.split("/")
        b1 = int(b1)
        a2 = int(b2)
        b = b1 / b2
    except:
        b = int(b)
        time.sleep(0)
    
    try:
        c1, c2 = c.split("/")
        c1 = int(c1)
        c2 = int(c2)
        c = c1 / c2
    except:
        c = int(c)
        time.sleep(0)

    latitude = a + b/60 + c/3600

    "--------------------------------------------------------------------------------------------------------"

    long = tags.get("GPS GPSLongitude", None)
    long = str(long)
    long = long.strip("[]")
    try:
        a, b, c = long.split(", ")
    except:
        pass

    try:
        a1, a2 = a.split("/")
        a1 = int(a1)
        a2 = int(a2)
        a = a1 / a2
    except:
        a = int(a)
        time.sleep(0)

    try:
        b1, b2 = b.split("/")
        b1 = int(b1)
        a2 = int(b2)
        b = b1 / b2
    except:
        b = int(b)
        time.sleep(0)

    try:
        c1, c2 = c.split("/")
        c1 = int(c1)
        c2 = int(c2)
        c = c1 / c2
    except:
        c = int(c)
        time.sleep(0)

    longitude = a + b/60 + c/3600

    "--------------------------------------------------------------------------------------------------------"

    latitudeRef = tags.get("GPS GPSLatitudeRef", None)
    longitudeRef = tags.get("GPS GPSLongitudeRef", None)

    latitudeRef = str(latitudeRef)
    longitudeRef = str(longitudeRef)

    if latitudeRef == "S":
        latitude = str(latitude)
        latitude = "-" + latitude
    
    else:
        latitude = str(latitude)
    
    
    if longitudeRef == "W":
        longitude = str(longitude)
        longitude = "-" + longitude
    
    else:
        longitude = str(longitude)
    
    print("Latitude: " + latitude + ", Ref: " + latitudeRef)
    print("Longitude: " + longitude + ", Ref: " + longitudeRef)


    location = latitude + ", " + longitude
    
    if latitudeRef != "None":
        address = gmaps.search(lat=latitude, lng=longitude).first()
        address = str(address)
        print("Address: " + address)
        """
        global zipCode
        spam1, zipCode, spam2 = address.rsplit(", ", 2)
        zipCode = str(zipCode)
        print("Zipcode: " + zipCode)
        global dZipCodePics
        if zipCode == searchPic.get():
            dZipCodePics.insert(0, name)
            """

def pics():
    current_user = getpass.getuser()
    if platform.system() == "Windows":
        startingDir = "C:/Users/" + current_user + "/Pictures"
    elif platform.system() == "Mac":
        startingDir = "/Users/" + current_user + "/Photos"
    else:
        startingDir = None
        
    allDPics = []
    rootDir = startingDir
    for dirName, subdirList, fileList in os.walk(rootDir):
        print("Found directory: " + dirName)
        for fname in fileList:
            print("\tFound file: " + fname)
            dRealFname = dirName + "/" + fname
            allDPics.insert(0, dRealFname)
    print(allDPics)
    global i
    for i in allDPics:
        with open(i, "rb") as n:
            readPicWithoutOutput(n)
    global dZipCodePics
    global dZipCodePicsStr
    global piczs
    piczs = []
    for piczzz in dZipCodePics:
        dZipCodePicsStr = str(piczzz)
        dZipCodePicsStr = dZipCodePicsStr[:-2]
        dZipCodePicsStr = dZipCodePicsStr[27:]
        piczs.insert(0, dZipCodePicsStr)
    piczs = str(piczs)
        
    dZipCodeMessage = "Done finding all images with the zipcode \"" + searchPic.get() + "\". The images are: " + piczs + "."
    messagebox.showinfo("Zip Code images: ", piczs)
    dZipCodePics = []


def extraInformation():
    print("Extra Info")
    messagebox.showinfo("About this Program", aboutThis)

def viewHistory():
    global history
    print(history)
    messagebox.showinfo("History", history)

def clearHistory():
    clearHistoryMessage = messagebox.askokcancel("Clear History", "Are you sure you want to clear history?")
    print(clearHistoryMessage)
    if clearHistoryMessage == True:
        global history
        history = {}
        print("Cleared History")
        print(history)
    else:
        pass

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="\u2630", menu=filemenu)
historyMenu = Menu(filemenu)

filemenu.add_cascade(label="History", menu=historyMenu)
historyMenu.add_command(label="View history", command=viewHistory)
historyMenu.add_command(label="Clear history", command=clearHistory)

filemenu.add_command(label="About", command=extraInformation)

Title = root.title("PicFinder")
label = ttk.Label(root, text =nameOfFile, foreground="black", font=("Helvetica", 18), background="white")
label.pack(side="top")

space = ttk.Label(root, text ="",foreground="black",font=("Helvetica", 12), background="white")
space.pack(side="top")

openbutton = Button(root, text = 'Open', command = OpenFile, width=5, height=1, bg="red", fg="white")
openbutton.pack(side="top")

space = ttk.Label(root, text ="",foreground="black",font=("Helvetica", 6), background="white")
space.pack(side="top")

labelOr = ttk.Label(root, text ="Or:", foreground="black", font=("Helvetica", 12), background="white")
labelOr.pack(side="top")

space = ttk.Label(root, text ="",foreground="black",font=("Helvetica", 6), background="white")
space.pack(side="top")

searchPic = Entry(root, width="30", justify='center')
searchPic.pack(side="top")
searchPic.insert(0, "Search local images by zip code")
okbutton = Button(root, text = 'Go', command = pics, width=3, height=1, bg="#89CFF0", fg="white")
okbutton.pack(side="top")

space = ttk.Label(root, text ="",foreground="black",font=("Helvetica", 6), background="white")
space.pack(side="top")


root.configure(background='White')
root.config(menu=menubar)
root.iconbitmap("PicFinderIco.ico")
root.geometry("400x300")
root.resizable(0,0)
root.mainloop()