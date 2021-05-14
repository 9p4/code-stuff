import exifread
import time

f = open("C:\\Users\\smsag_000\\Pictures\\IMG.jpg", "rb")
n = open("thing.txt", "w")

tags = exifread.process_file(f, details=False)

lat = tags.get("GPS GPSLatitude", None)

d = lat[0]
m = lat[1]
s = lat[2]

if lat != None:
    try:
        d1, d2 = d.split("/")
        d1 = float(d1)
        d2 = float(d2)
        d = d1 / d2
    except:
        d = lat[0]
        d = float(d)

    try:
        m1, m2 = m.split("/")
        m1 = float(m1)
        m2 = float(m2)
        m = m1 / m2
    except:
        m = lat[1]
        m = float(m)

    try:
        s1, s2 = s.split("/")
        s1 = float(d1)
        s2 = float(d2)
        s = s1 / s2
    except:
        s = lat[2]
        s = float(s)

    latdd = d + m/60 + s/3600

"----------------------------------------------------"

long = tags.get("GPS GPSLongitude", None)

d = long[0]
m = long[1]
s = long[2]

if long != None:
    try:
        d1, d2 = d.split("/")
        d1 = float(d1)
        d2 = float(d2)
        d = d1 / d2
    except:
        d = long[0]
        d = float(d)
    try:
        m1, m2 = m.split("/")
        m1 = float(m1)
        m2 = float(m2)
        m = m1 / m2
    except:
        m = long[1]
        m = float(m)

    try:
        s1, s2 = s.split("/")
        s1 = float(s1)
        s2 = float(s2)
        s = s1 / s2
    except:
        s = long[2]
        s = float(s)

    longdd = d + m / 60 + s / 3600

"----------------------------------------------------"

print(latdd)
print(longdd)
input()

tags = str(tags)
n.write(tags)
n.close()