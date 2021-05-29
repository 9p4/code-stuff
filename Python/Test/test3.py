def exit():
	exit = input("Press enter when you are done.")
	quit()

file = input ("Enter EXACT file location and file name. EX:C:/users/user/Documents/File.txt. ")

g = open(file, "r+")

option = input ("Type '1' to view the file. Type '2' to write to the file. Type '3' to open the file. Type anything else to close this program. ")
	
if option == 1:
	g.read()
	exit()
	
elif option == 2:
	writeToFile = input("Enter Text and press enter.")
	g.write(writeToFile + "\n")
	exit()
	
elif option == 3:
	open(file, "t")
	exit()
		
else:
	quit()