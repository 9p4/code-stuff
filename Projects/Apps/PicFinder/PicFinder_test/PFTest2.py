import exifread
name = open("C:\\Users\\smsag_000\Pictures\IMG.jpg", "rb")
tags = exifread.process_file(name, details=False)
zoop = open("Log.txt", "w")
tags = str(tags)
zoop.write(tags)
zoop.close()
name.close()