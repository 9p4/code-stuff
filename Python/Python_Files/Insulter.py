import random
import time

def theEnd:
	#Defines the function "end"
	time.sleep(5)#sleeps 5 seconds
	quit()

name = raw_input("What is your name? ")

type123 = random.randint(0, 10)

if type123 == 0:
	print("You suck," + name)
	end()
	
elif type123 == 1:
	print("See you NEVER" + name)
	end()