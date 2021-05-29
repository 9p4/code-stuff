import time #Setup the timing function

def YouLose():#defines the function "YouLose"
	print("You Lose") #prints "you Lose"
	time.sleep(5) #Waits 5 seconds before quitting
	quit(); # quits

def YouAreAwesome():
	print ("You are AWESOME!! :) ")

name = raw_input ("What is your name? ")

if name == "xxxxxx": #Replace the "xxxxxx" for your name
	YouAreAwesome();
	bad = 0

elif name == "xxxxxx Saggi":#Replace the "xxxxxx Saggi" with another option for a name
	YouAreAwesome();
	bad = 0

#add #'s at the beggening of these lines below to deactivate this cheat.
elif name == "I Want To Win":
	print ("You Win!")
	time.sleep(5)
	
elif name == "Dhruv":
	print ("Hello, Bubby McDubberson.")
	YouLose();
	
elif name == "Mommy":
	print ("Hi Mom.")
	YouLose();

else:
	print ("Did you really have the nerve to show up here?")
	bad = 1
	
time.sleep(0.5)

if bad == 0:
	print ("You can eat a chocolate!")
	time.sleep(1)
	print ("Or a Mento, if you want one.")
	time.sleep(1)
	MentoOrChocolate = raw_input ("What do you want? A Chocolate, or a Mento? ")
	
	if MentoOrChocolate == "Chocolate":
		print ("We're out of chocolate. Sorry.")
		YouLose();
	
	elif MentoOrChocolate == "Mento":
		print ("What are you waiting for? Go get one!")
		time.sleep(1)
		print ("You Win!")
		time.sleep(5)
	
	else:
		print ("Try typing in 'Mento' or 'Chocolate' next time.")
		YouLose();

else:
	print ("If you are not xxxxxx The Great, I don't recommend trying this again")#replace "xxxxxx The Great" with whatever you want.
	YouLose();