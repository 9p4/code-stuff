import exifread

f = open("C:\\Users\\smsag_000\\Downloads\\pics\\IMG_3848.JPG", "rb")

tags = exifread.process_file(f, details=False)

latitudeRef = tags.get("LatitudeRef", None)
longitudeRef = tags.get("LongitudeRef", None)

print(latitudeRef)
print(longitudeRef)