import random

# Defines roll function with n sides
def roll(n):
	# Prints a random integer between 1 and n
	print(random.randint(1, n))
	# Asks to repeat roll
	again = raw_input("Would you like to roll again? YES or NO")
	if again == "YES":
		roll(sides)

# Asks for n
sides = input("How many sides should the die have?")
sides = int(sides)
# Initiates
roll(sides)




