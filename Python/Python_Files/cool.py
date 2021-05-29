import random
import time
secret = random.randint(1,99)
guess = 0
tries = 0
print("Ahoy matey, I'm the Dreaded Pirate Blackbeard, and I have a secret for you!")
print("It is a number from 1 to 99. This number is what unlocks my treasure, worth more than a king's ransom! I will give you 6 tries.")
while guess != secret and tries <6:
    guess = input("What's yer guess landlubber? ")
    guess = int(guess)
    if guess < secret:
        print("Too low, ye scurvy dog!")
        tries = tries + 1
    elif guess > secret:
        print("Too high, ye stinking landlubber!")
        tries = tries + 1
    if guess == secret:
        print("Avast! Ye got it! Found my treasure, ye did!")
        time.sleep(5)
    else:
        print("No treasure for ye! Better luck next time matey!")