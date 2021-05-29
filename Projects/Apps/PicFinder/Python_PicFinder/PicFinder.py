#Begin setup code
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import exifread
import webbrowser
from tkinter import messagebox
import os
import sys
import time
import platform
import getpass
from geopy.geocoders import Nominatim
from tkinter import PhotoImage
import socket
from tkinter.colorchooser import *
#from geolocation.main import GoogleMaps
#import re
#gmaps = GoogleMaps(api_key="AIzaSyCqR38gBJKTtOSKBbnjOxYVmh9dBw_KJKI")
REMOTE_SERVER = "www.google.com"
f = None
latitude = None
longitude = None
location = ""
daError = ""
url = ""
zzzzz = 1
jingleBells = 0
global dZipCodePics
global zipCode
zipCode = 0
dZipCodePics = []
nameOfFile = "PicFinder"
geolocator = Nominatim()
global startingZipCodeImagesDir
startingZipCodeImagesDir = os.path.expanduser('~') + "/Pictures"
print(startingZipCodeImagesDir)
startingZipCodeImagesDir = startingZipCodeImagesDir.replace("\\", "/")
print("Current image path: " + startingZipCodeImagesDir)
global history
history = {}
root = Tk( )
global openMap
openMap = Button(root, text="", command = None, bg="#FDD9B5", borderwidth=0)
openMap.bind("<Enter>", lambda event, h=openMap: h.configure(bg="dark gray"))
openMap.bind("<Leave>", lambda event, h=openMap: h.configure(bg="#FDD9B5"))
global label4
label4 = ttk.Label(root, text = "", foreground = "black", font = ("Helvetica", 12), background=None)
aboutThis = """
Version: 1.1.3.1
Realeased on September 6, 2016
Made by: xxxxxx M. Saggi
"""
background_color = "white"
root.configure(background="white")
root.title("PicFinder")
root.iconbitmap("PicFinderIco.ico")
root.geometry("400x300")
root.resizable(0,0)


def is_connected():
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        return False

def exitDApp(event=None):
    sys.exit()

def error():
    messagebox.showerror("Error!", "No coordinates detected.")

def startingDir():
    global startingZipCodeImagesDir
    startingZipCodeImagesDir = askdirectory(initialdir='.')

while True:
    if is_connected() == True:
        break
    else:
        connectionretry = messagebox.askretrycancel("Connection Error", "We could not connect to the server. Please check your connection and try again.")
        if connectionretry == True:
            pass
        else:
            print("Closing app...")
            exitDApp()

def chooseColor():
    color = askcolor()
    print(color)
    background_color = color[1]
    root.configure(background=background_color)
    space.configure(background=background_color)
    space1.configure(background=background_color)
    space2.configure(background=background_color)
    space3.configure(background=background_color)
    label.configure(background=background_color)
    label4.configure(background=background_color)
    labelOr.configure(background=background_color)

#Begin Logic code
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
        if is_connected() == True:
            try:
                address = geolocator.reverse(location)
                address = str(address)
                print("Address: " + address)
                global zipCode
                spam1, zipCode, spam2 = address.rsplit(", ", 2)
                print("Zipcode: " + zipCode)
                fileLocation = str(name.name)
                history[fileLocation] = location
                print(history)
            except:
                print("Error:")
                print(sys.exc_info())
                errormessagepieiscool = "Something's not right. Please try again later. Details: " + str(sys.exc_info())
                messagebox.showerror("Error!", errormessagepieiscool)
                address = "Not available"
        else:
            messagebox.showwarning("Connection", "We are not able to connect to the server, check your internet connection and try again.")
            address = "Not available"



    "--------------------------------------------------------------------------------------------------------"

    #Opens the Map
    def openTheMap():
        url = "http://www.maps.google.com/maps/place/" + location
        webbrowser.open(url)

    locationtext = "Location: " + location + ". Address: " + address

    if latitudeRef != "None":
        global label4
        label4.pack_forget()
        label4 = ttk.Label(root, text = locationtext, foreground = "black", font = ("Helvetica", 12), background=background_color, wraplength=400, justify="center")
        label4.pack(side="bottom")
        global openMap
        openMap.pack_forget()
        openMap = Button(root, text="Open in Google Maps", command = openTheMap, bg="#FDD9B5", borderwidth=0)
        openMap.bind("<Enter>", lambda event, h=openMap: h.configure(bg="dark gray"))
        openMap.bind("<Leave>", lambda event, h=openMap: h.configure(bg="#FDD9B5"))
        openMap.pack(side="bottom")
      

#OpenFile
def OpenFile(event=None):
    global name
    startingDir = startingZipCodeImagesDir

    name = askopenfilename(initialdir=startingDir,
                           filetypes =(("JPG Files", "*.jpg"),("All Files","*.*")),
                           title = "Open File - PicFinder"
                           )
    print(name)
    try:
        f = open(name,'rb')
        print(f)
        if f != "":
             try:
                readPic(f)
             except:
                 print("Error: ")
                 print(sys.exc_info())
        else: pass   
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
        if is_connected() == True:
            try:
                address = geolocator.reverse(location)
                address = str(address)
                print("Address: " + address)
                global zipCode
                spam1, zipCode, spam2 = address.rsplit(", ", 2)
                print("Zipcode: " + zipCode)
                return zipCode
            except:
                print("Error:")
                print(sys.exc_info())
                errormessagepieiscool = "Something's not right. Please try again later. Details: " + str(sys.exc_info())
                messagebox.showerror("Error!", errormessagepieiscool)
        else: messagebox.showwarning("Internet Connection", "We are not able to connect to the server, check your internet connection and try again.")



def readPicWithoutAddress(name):
    f = open(name, "rb")
    tags = exifread.process_file(f, details=False)

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

    location = latitude + ", " + longitude
    url = "http://www.maps.google.com/maps/place/" + location
    webbrowser.open(url)



def pics(event=None):
    startingDir = startingZipCodeImagesDir
    global piczs
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
    piczs = []
    global zipCode
    for i in allDPics:
        with open(i, "rb") as n:
            diddlyZipCode = readPicWithoutOutput(n)
            if diddlyZipCode == searchPic.get():
                piczs.insert(0, str(n.name))
    zipPics = piczs
    piczs = str(piczs)
    dZipCodeMessage = "Done finding all images with the zipcode \"" + searchPic.get() + "\". The images are: " + piczs + "."
    print(dZipCodeMessage)
    jingleBells = 0
    herpADerpCode = """
def popupmsg():
    popup = Tk()
    popup.iconbitmap('PicFinderIco.ico')
    popup.wm_title("Zip code images")
"""
    for diddlyDoot in zipPics:
        herpADerpCode = herpADerpCode + "    ttk.Label(popup, text='" + diddlyDoot + "').grid(column=0, row=" + str(jingleBells) + ")" + """
"""
        herpADerpCode = herpADerpCode + """
    ttk.Button(popup, text='Open in Google Maps', command=lambda: readPicWithoutAddress('""" + diddlyDoot + """')).grid(column=1, row=""" + str(jingleBells) + """)
"""
        jingleBells = jingleBells + 1
        print(diddlyDoot)
    herpADerpCode = herpADerpCode + """    ttk.Button(popup, text="Okay", command = popup.destroy).grid()
    popup.mainloop()
popupmsg()"""
    print(herpADerpCode)
    print("The zip code pics are " + str(zipPics))
    exec(herpADerpCode)
    dZipCodePics = []


def extraInformation(event=None):
    print("Extra Info")
    messagebox.showinfo("About this Program", aboutThis)

def viewHistory(event=None):
    global history
    print(history)
    messagebox.showinfo("History", history)

def clearHistory(event=None):
    clearHistoryMessage = messagebox.askokcancel("Clear History", "Are you sure you want to clear history?")
    print(clearHistoryMessage)
    if clearHistoryMessage == True:
        global history
        history = {}
        print("Cleared History")
        print(history)
    else:
        pass

def exit(event=None):
    closeAppMessage = messagebox.askokcancel("Close", "Are you sure you want to close this app?")
    if closeAppMessage == True:
        print("Closing app...")
        exitDApp()
    else: pass
    
#Begin GUI Code
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="\u2630", menu=filemenu)
historyMenu = Menu(filemenu)
settingsMenu = Menu(filemenu)

filemenu.add_cascade(label="History", menu=historyMenu)
historyMenu.add_command(label="View history", command=viewHistory, accelerator="Ctrl+H")
root.bind("<Control-h>", viewHistory)
root.bind("<Control-H>", clearHistory)
root.bind("<Control-o>", OpenFile)
root.bind("<Control-q>", exit)
historyMenu.add_command(label="Clear history", command=clearHistory, accelerator="Ctrl+Shift+H")

filemenu.add_cascade(label="Settings", menu=settingsMenu)
settingsMenu.add_command(label="Change Background Color", command=chooseColor)
settingsMenu.add_command(label="Change Zipcode Image Directory", command=startingDir)

filemenu.add_command(label="About", command=extraInformation)
filemenu.add_command(label="Exit", command=exit)


Title = root.title("PicFinder")
label = ttk.Label(root, text =nameOfFile, foreground="black", font=("Helvetica", 18), background="white")
label.pack(side="top")

space = ttk.Label(root, text ="",foreground="black",font=("Helvetica", 12), background="white")
space.pack(side="top")

openbutton = Button(root, text = 'Open Image', command = OpenFile, width=9, height=1, bg="red", fg="white", borderwidth=0)
openbutton.bind("<Enter>", lambda event, h=openbutton: h.configure(bg="dark gray"))
openbutton.bind("<Leave>", lambda event, h=openbutton: h.configure(bg="red"))
openbutton.pack(side="top")

space1 = ttk.Label(root, text ="",foreground="black",font=("Helvetica", 6), background="white")
space1.pack(side="top")

labelOr = ttk.Label(root, text ="Or:", foreground="black", font=("Helvetica", 12), background="white")
labelOr.pack(side="top")

space2 = ttk.Label(root, text ="",foreground="black",font=("Helvetica", 2), background="white")
space2.pack(side="top")

searchPic = Entry(root, width="30", justify='center', borderwidth="0")
searchPic.insert(0, "Search local images by zip code")
searchPic.pack(pady=10)
okbutton = Button(root, text = 'Go', command = pics, width=3, height=1, bg="#89CFF0", fg="white", borderwidth=0)
okbutton.bind("<Enter>", lambda event, h=okbutton: h.configure(bg="dark gray"))
okbutton.bind("<Leave>", lambda event, h=okbutton: h.configure(bg="#89CFF0"))
okbutton.pack(side="top")

space3 = ttk.Label(root, text ="",foreground="black",font=("Helvetica", 6), background="white")
space3.pack(side="top")

root.protocol("WM_DELETE_WINDOW", exit)

root.configure(background="white")
root.config(menu=menubar)
root.iconbitmap("PicFinderIco.ico")
root.geometry("400x300")
root.resizable(0,0)
root.mainloop()