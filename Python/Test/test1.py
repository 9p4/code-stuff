import time

word = input("Enter the Word ")
letterOrWord = input("Enter word lor letter that is supposed to be in this. ")

if letterOrWord in word:
	print ("Yes, it is in it")
	time.sleep(5)

else:
	print("No, it is not in it.")
	time.sleep(5)