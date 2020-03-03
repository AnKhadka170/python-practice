#This is a Python code for rock, scissors and paper game.
import random
space = " "
print ("\nWelcome to the game of Rock, Scissors and Paper \n")
print("Winning instructions for Rock, Scissors and Paper are: \n"
	+ 3*space + "Rock v/s Scissors --> Rock Wins \n" +
	3* space + "Rock v/s Papers --> Paper Wins \n" +
	3* space + "Paper v/s Scissors --> Scissors Wins \n")
while True:
	#Computer chooses a random number among 1,2 and 3 using randiant method of random module
	comp_Choice =random.randint(1, 3)
	#choices
	print("Enter your option \n 1) 1 for Rock \n 2) 2 for Scissors \n 3) 3 for Paper\n")
	def inputfloat():
	#Taking user input
		while True:
			try:
				global myChoice 
				myChoice = input("Entered Value: ")
				while myChoice >3 or myChoice < 1:
					print"You entered a invalid option."
					myChoice = input("Enter you choice (A number between 1 and 3): ")
				userChoice = float(myChoice)
				print'User chooses: ', + userChoice
				break
			except NameError:
				print ("Inavlid option: NONE \n")
	#initializing what each number represents to
		if (myChoice == 1 ):
			choice = 'Rock'
		elif (myChoice == 2):
			choice = 'Scissors'
		else:
			choice = 'Paper'
		print("User's choice is " + choice + "\n")
	inputfloat()

	#computer's choice
	if (comp_Choice == 1 ):
		choiceName = 'Rock'
	elif (comp_Choice == 2):
		choiceName = 'Scissors'
	else:
		choiceName = 'Paper'

	print("Computer's choice is " + choiceName + "\n")

	#evaluating the results i.e. who won the game
	if (myChoice == 1):
		if(comp_Choice ==1):
			print("\033[1m" +"It's a tie. Let's try again \n" + "\033[0m")
		elif (comp_Choice == 2):
			print ("\033[1m" +"User is the winner \n"+ "\033[0m")
			print ("Game Over")	
			break
		else:
			print ("\033[1m" +"Computer is the winner\n"+ "\033[0m")
	elif (myChoice == 2):
		if (comp_Choice == 1):
			print("\033[1m" +"Computer is the winner\n"+ "\033[0m")
		elif (comp_Choice == 2):
			print("\033[1m" +"It's a tie. Let's try again\n"+ "\033[0m")
		else:
			print("\033[1m" +"User is the winner\n"+ "\033[0m")
			print ("Game Over")
			break
	elif (myChoice == 3):
		if (comp_Choice == 1):
			print("\033[1m" +"User is the winner\n"+ "\033[0m")
			print ("Game Over")
			break
		elif (comp_Choice == 2):
			print("\033[1m" +"Computer is the winner\n"+ "\033[0m")
		else:
			print("\033[1m" +"It's a tie. Let's try again\n"+ "\033[0m")
	





	


