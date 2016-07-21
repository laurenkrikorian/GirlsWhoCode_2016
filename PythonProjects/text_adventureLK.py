start = '''
You wake up one morning and find that you aren\'t in your bed; you aren't even in your room.
You\'re in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don\'t touch the walls."
There is a hallway to your right and to your left.
'''


print(start)

done = False

x = 0

user_input = input("Type left or right. ")


while not done: 

	while user_input is not "left" or "right":
		
		if user_input == "left":
			print("There is a lake.") 
			user_input4 = input("Swim or run around? ")
		
			while user_input4 is not "swim" or "run around":
	
				if user_input4 == "swim":
					print("Luckly it was a short and safe swim, and you are on the other side. Now there is a castle in front of you, and the only option is to go inside. You are now in a hallway.")
					user_input5 = input("Left or right? ")
				
					while user_input5 is not "left" or "right":
		
						if user_input5 == "left":
							print("There is a giant buffett of food. The question is whether or not the food is safe to eat.")
							user_input6 = input("Eat food or leave it? ")
						
							while user_input6 is not "eat food" or "leave it":
		
								if user_input6 == "eat food":
									print("Yay! The food was for you and the people of the castle were expecting you. A party has started in you honor and you have won the game!")
		
								elif user_input6 == "leave it":
									print("Bad call. The food was actually for you, but now you and the food will be fead to the beasts. Game Over :(")
									done = True
								
								else:
									user_input6 = input("Eat food or leave it? ")
			
						elif user_input5 == "right":
							print("There is a guard that captures you immediatly. Game Over :(")
							done = True
			
						else:
							user_input5 = input("Left or right? ")
		
				elif user_input4 == "run around":
					print("You start to run, but about a half mile around, there are bears with wings that eat you. Game Over :(")
					done = True
	
				else:
					user_input4 = input("Swim or run around? ")
					
		elif user_input == "right":
			print("You find a dragon") 
			user_input2 = input("Fight or run? ")
		
			while user_input2 is not "run" or "fight":
	
				if user_input2 == "run":
					print("The dragon tries to breath fire on you but misses! You are now past the dragon and need to open a door to the left or right.")
					user_input3 = input("Left or right? ")
				
					while user_input3 is not "right" or "left":
						
						if user_input3 == "right":
							print("You made a complete cirle and are back wear you started")
							user_input = input("Type left or right. ") # make a circle back to the beginning
		
						elif user_input3 == "left":
							print("You stroll right into the room before realizing that there is a giant hole in the ground. You fall for ten seconds, hit the ground, and are now trapped. Game Over :(")
							done = True
						
						else:
							user_input3 = input("Left or right? ")
			
				elif user_input2 == "fight":	
					print("The dragon breathes fire, and now you are dead. Game Over :(")
					done = True
	
				else:
					user_input2 = input("Fight or run? ")
		
		else:
			user_input = input("Type left or right. ")