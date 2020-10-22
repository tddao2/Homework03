#Tri Dao
#1954347
#11.27 CIS 2348 LAB*: Program: Soccer team roster (Dictionaries)

def printRoster():
  keys = list(players.keys())
  keys.sort()

  print("ROSTER")
  for key in keys:
    print("Jersey number: {}, Rating: {}".format(key,players[key]))

players = {}

for i in range(5):
  goal = int(input("Enter player {}'s jersey number:\n".format(i+1)))
  players[goal] = int(input("Enter player {}'s rating:\n".format(i+1)))
  print("")

printRoster()

while True:
  print("\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n")
  option = input("Choose an option:\n")

  if option == 'o':
    printRoster()

  elif option == 'a':
    goal = int(input("Enter a new player's jersey number:\n"))
    rating = int(input("Enter the player's rating:\n"))
    players[goal] = rating

  elif option == 'd':
    goal = int(input("Enter a jersey number:\n"))
    if goal in list(players.keys()):
      del players[goal]

  elif option == 'u':
    goal = int(input("Enter a jersey number:\n"))
    rating = int(input("Enter a new rating for player:\n"))
    players[goal] = rating

  elif option == 'r':
    rating = int(input("Enter a rating:\n"))
    keys = list(players.keys())
    keys.sort()
    print("\nABOVE {}".format(rating))
    for key in keys:
      if players[key] > rating:
        print("Jersey number: {}, Rating: {}".format(key,players[key]))
    
  if option == "q":
    break

