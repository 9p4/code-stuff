import base64
import Image
file = os.getcwd()
file = file.replace("\\" , "/")
file = file + input("Copy image into same location as this program and type the full name of the picture. Note: It has to be a .png file, or it won't work. ")

option1 = input("Type 1 to code the file, type 2 to decode the file, and type anything else to quit. ")
if option1 == "1":
    with open(file, "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
        print(str)
        input("Press enter when you are done.")
        
elif option1 == "2":
    pic = open("outputImage.png", "wb")
    pic.write(str.decode("base64")
    pic.close()
    
else:
    quit()