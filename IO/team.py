# TODO Create an empty list to maintain the player names
player_list = []

# TODO Ask the user if they'd like to add players to the list.
while input("Would you like to add a player to the list?(Yes/No) ").lower() == "yes":
	# If the user answers "Yes", let them type in a name and add it to the list.
	name = input("Enter the name of the player to add to the team: ")
	player_list.append(name)
	
# If the user answers "No", print out the team 'roster'
# TODO print the number of players on the team
print("There are {} people on the team:".format(len(player_list)))  
# TODO Print the player number and the player name
# The player number should start at the number one
i = 0
while i < len(player_list):
	print("Player {}: {}".format(i+1, player_list[i]))
	i += 1

# TODO Select a goalkeeper from the above roster
goalkeeper = int(input("Please, select goalkeeper by selecting one of the following numbers(1-{}) ".format(len(player_list)))) - 1

# TODO Print the goal keeper's name
print("Great! Goalkeeper for the game will be {}!".format(player_list[goalkeeper]))

# Remember that lists use a zero based index

