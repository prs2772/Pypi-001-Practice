import random

#settings
gameMode = 0
optionsPossible = 'paper, scissors, stone' if(gameMode == 0) else 'laser_gun, sword, the_force, escape'
rounds = 1
possible = optionsPossible.split(', ')

# Inits
computer_wins = 0
user_wins = 0
rules = 'In this game the rules are:\n'

indx = 0
while indx < len(possible):
  if (indx > 0):
    rules += "->" + possible[indx].capitalize() + " wins against " + possible[indx - 1].capitalize() + " but losses against "
    rules += possible[0].capitalize() if(indx + 1 == len(possible)) else possible[indx + 1].capitalize() + "\n"
  else:
    rules += "->" + possible[indx].capitalize() + " wins against " + possible[-1].capitalize() + " but losses against "
    rules += possible[indx + 1].capitalize() + "\n"
  indx += 1
rules += '\nOtherwise, is a tie'

exit = False

# Returns the nearest index next or previous
def near(list, indexList, next):
  if(next):
    return indexList + 1 if(indexList + 1 < len(list)) else 0
  else:
    return indexList - 1 if(indexList - 1 >= 0) else len(list) - 1

while not exit:
    print(rules)
    print('*' * 33)
    print()
    print('ROUND ', rounds, '. Figth!')
    print('*' * 33)

    user_option = input(optionsPossible + ' => ')
    user_option = user_option.lower()

    if not user_option in possible:
      print('\n\n\nThat is not a valid option, it must be ' + optionsPossible)
      continue

    computer_option = random.choice(possible)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    # 0 losses against 1 but wins against 2, 1 losses against 2 but wins against the following (could be 0 or if an option is added, 3) otherwise, ties
    indxUsr = possible.index(user_option)
    indxCom = possible.index(computer_option)
    result = ''

    # Tie if both are equal or if none is near of the other
    tie = indxUsr == indxCom or not (abs(indxUsr - near(possible, indxCom, True)) == 0 or abs(indxUsr - near(possible, indxCom, False)) == 0)

    if tie:
        result = '\n---Tie!---\n'
    elif(near(possible, indxCom, False) == indxUsr):
      result = 'You loose this one bud'
      computer_wins += 1
    else:
      result = 'You won this one!'
      user_wins += 1
    result += f'\nScoreboard ({rounds} rounds): Computer: {computer_wins} You: {user_wins}'

    print(result)
    
    if(input('Continue? (y/n)').lower() == 'n'):
      exit = True
    else:
      rounds += 1

