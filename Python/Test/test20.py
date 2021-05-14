#encoding=utf-8

import time, webbrowser, exifread

f = open("C:\Users\smsag_000\Pictures\Camera\DSC04056.JPG", "r")

tags = exifread.process_file(f, details=False, stop_tag='GPS')
    
url = "https://www.maps.google.com/place/" + tags

print(tags)
print(url)

input()