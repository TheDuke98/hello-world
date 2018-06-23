# Author: John Dukewich  |  jdukewich@gmail.com
# This is code to simulate the Monty Hall problem.

import random

def main():

	# Initiliaze win counts for the switch and stay instances
	switchWins = 0      
	stayWins = 0

	# Prompt user for how many simulations to run
	totalRuns = int(input("Enter how many times you want this to run: "))
	
	# Run a for loop of the "switch" instance
	# The loop works by generating a random number between 1 and 3 both for the car's location and the simulated
	# user's guess. Then it checks the doors to find the first door that wasn't chosen by the user and doesn't have
	# the car to reveal that the door contains a goat. Then checks to see if the switching of the remaining doors
	# yields a win.
	for x in range(totalRuns):
		carDoor = random.randint(1,3)
		chosenDoor = random.randint(1,3)
		if chosenDoor != 1 and carDoor != 1:
			if (5 - chosenDoor) == carDoor:
				switchWins += 1
		elif chosenDoor != 2 and carDoor != 2:
			if (4 - chosenDoor) == carDoor:
				switchWins += 1				
		else:
			if (3 - chosenDoor) == carDoor:
				switchWins += 1
	print("Switch win percentage: %f" % (float(switchWins/totalRuns)))

	# Run a for loop of the "stay" instance
	# This works the same way as the switch instance loop, but at the end it checks if staying with the 
	# same door yields a win. Don't have to reveal a goat door because you are staying with same door
	# anyway. 
	for x in range(totalRuns):
		carDoor = random.randint(1,3)
		chosenDoor = random.randint(1,3)
		if chosenDoor == carDoor:
			stayWins += 1

	print("Stay win percentage: %f" % (float(stayWins/totalRuns)))

# Puts entire code on a user controlled loop and calls the main function
stuff = input("Press any key to continue or type 'exit' to quit . . .")
while(stuff != "exit"):
	main()
	stuff = input("Press any key to continue or type 'exit' to quit . . .")