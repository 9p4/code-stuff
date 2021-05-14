import exifread
import time
pics = open("C:/Users/smsag_000/Pictures/Camera/DSC04056.jpg", 'rb')
tags = exifread.process_file(pics, details=False)
pics.close()
print(tags)
time.sleep(5)