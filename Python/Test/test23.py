import exifread
import time

f = open("C:\\Users\\smsag_000\\Pictures\\IMG.JPG", "rb")

tags = exifread.process_file(f, details=False)

"--------------------------------------------------------------------------------------------------------"

lat = tags.get("GPS GPSLatitude", None)
lat = str(lat)
lat = lat.strip("[]")
a, b, c = lat.split(", ")

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

dd1 = a + b/60 + c/3600
print("Latitude")
if c > 1:
    dd1 = str(dd1)
    dd1 = "-" + dd1
    print(dd1)
else:
    print(dd1)

"--------------------------------------------------------------------------------------------------------"

long = tags.get("GPS GPSLongitude", None)
long = str(long)
long = long.strip("[]")
a, b, c = long.split(", ")

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

dd = a + b/60 + c/3600
print("Longitude")
if c > 1:
    dd = str(dd)
    dd = "-" + dd
    print(dd)
else:
    print(dd)

dd1 = str(dd1)
dd = str(dd)
print(dd1 + ", " + dd)