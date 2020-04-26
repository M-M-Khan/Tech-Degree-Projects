# TODO Create an empty list to maintain the player names

player = []

# TODO Ask the user if they'd like to add players to the list.
ask = input("would you like to add players? \n[Y/N]")
# If the user answers "Yes", let them type in a name and add it to the list.

while ask.lower() != "n":
    player_add = input("Enter is the player's name: ")
    player.append(player_add)
    ask = input("Enter more player's name: \n[Y/N] ")

# If the user answers "No", print out the team 'roster'
for x in range(len(player)-1):
    player[x]
    print(player)
    print(", ".join(player))

# # TODO print the number of players on the team

# print("No of players on the team is {}".format(len(player)))


# # TODO Print the player number and the player name
# # The player number should start at the number one

# player_num = 1
# for players in player:
#     print("Player {}: {}".format(player_num,players))
#     player_num += 1


# # TODO Select a goalkeeper from the above roster

# goal = input("Select the goalkeeper using number \n(1-{}): ".format(len(player)))

# goal = int(goal)

# # TODO Print the goal keeper's name
# # Remember that lists use a zero based index

# print("The goal keeper's name is: {}".format(player[goal-1]))



