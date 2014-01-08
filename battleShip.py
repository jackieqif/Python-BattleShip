# BattleShip board Game
# by jackieq
# reviewed by Yunzhang's Budda power

from random import randint

BOARD = [['O' for i in xrange(5)] for j in xrange(5)]

LEVEL = {
  1: 12,
  2: 8,
  3: 4
  }

HIT_MARK = "X"

def print_board(BOARD):
  for row in BOARD:
    print ' '.join(row)
dfs

def print_ship():
  print """
                                       # #  ( )
                                  ___#_#___|__
                              _  |____________|  _
                       _=====| | |            | | |==== _
                 =====| |.---------------------------. | |====
   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
     \                                                             /
      \_______________________________________________WWS_________/
  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
   wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
   """

def print_victory():
  print """
                                     |__
                                     |\/
        [[     *********       ]]    |--  
        [[ We are proud of you!]]--/ |
        [[ *****         ***** ]]   | || 
                            _/|     _/|-++'
                        +  +--|    |--|--|_ |-
                     { /|__|  |/\__|  |--- |||__/
                    +---------------___[}-_===_.'____                 /
                ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _
 __..._____--==/___]_|__|_____________________________[___\==--____,------' .7
|                                                                   You Win /
 \_________________________________________________________________________|
  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
   wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                                                                                                    
  """


def print_radar1():
  print """
 
              .-  _           _  -.
             /   /             \   .
            (   (  (` (-o-) `)  )   )
             \   \_ `  -+-  ` _/   /
              `-       -+-       -`
                       -+-
          __  _   ___  _|_  ___   __ ___
  
  """


def print_radar2():
  print """
               O
               |
               |
               |  
         ______|
      /______  |
     |       | |      
     | ===== | |     
     | ===== | |    
     |       | |         
     |  .-.  | |       o    
     | ' . ' | |   |~       
  ..'| '._.' | |  o
.'   |_______|/ 

  """


def print_radar3():
  print """
         ,-.
        / \  `.  __..-,O
       :   \ --''_..-'.'
       |    . .-' `. '.
       :     .     .`.'
        \     `.  /  ..
         \      `.   ' .
          `,       `.   .
         ,|,`.        `-..
        '.||  ``-...__..-`
         |  |
         |__|
       // |||||
    __//__||__|||__
   '--------------'
  """


def print_defected():
  print """
                ,a_a
               {/ ''\_
               {\ ,_oo)
               {/  (_^_____________________
     .=.      {/ \___)))*)----------;=====;`
    (.=.`\   {/   /=;  ~~           |||::::
        \ `\{/(   \/\               |||::::
         \  `. `\  ) )              |||||||
     You  \    // /_/_              |||||||
           '==''---))))             |||||||




                                
                                  \   O,
                        \___________\/ )_________/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  """


def print_instruction():
  print 'Let\'s play Battleship!'
  print """My ship has been deployed in the board below, \
your goal is to sink my ship by providing target row \
and colum number as coodinates for your missle."""
  print 'Entering battle area...'
  print '======================'
  print_ship()


def select_level():
  while True:
    try:
      user_input = int(raw_input('Please select game level: 1~3: '))
    except:
      pass
    if user_input not in [1,2,3]:
      print 'Please input a number from 1 to 3'
    else:
      return user_input, LEVEL[user_input]


def random_row(BOARD):
  return randint(0, len(BOARD) - 1)


def random_col(BOARD):
  return randint(0, len(BOARD[0]) - 1)


def radar_officer(ship_row, ship_col, guess_col, guess_row):
  if ship_row - guess_row < 0:
    print_radar1()
    print '((( Radar station1: Commander, enemy is up north )))'
  elif ship_row - guess_row > 0:
    print_radar1()
    print '((( Radar station1: Commander, enemy is down south )))'
  else:
    print_radar2()
    print '((( Radar station1: Commander, we are on the right row! )))'

  if ship_col - guess_col < 0:
    print '((( Radar station2: Commander, enemy is further west )))'
  elif ship_col - guess_col > 0:
    print '((( Radar station2: Commander, enemy is further east )))'
  else:
    print '((( Radar station2: Commander, we are on the right column! )))'

  if abs(ship_col - guess_col) == 1 and abs(ship_row - guess_row) == 1:
    print_radar3()
    print '((((( Beep... Beep... radar station3 detected that enemy is one \
coodinate away from your last hit point!!! ))))'


def guess(ship_row, ship_col):
  print_board(BOARD)
  result = False
  try:
    guess_row = int(raw_input('Guess Row:')) - 1
    guess_col = int(raw_input('Guess Col:')) - 1
  except:
    print 'Commander, we can not understand coodinate you\'ve provided...'
    return result
  
  if guess_row == ship_row and guess_col == ship_col:
    print 'Bang... Bang...'
    print 'Bang...'
    print 'Target down! Target down!'
    result = True
    return result
  else:
    if guess_row < 0 or guess_row > 4 or guess_col < 0 or guess_col > 4:
      print 'Oops, that\'s not even in the ocean.'
    elif BOARD[guess_row][guess_col] == HIT_MARK:
      print 'You guessed that one already.'
    else:
      print 'You missed the battleship!'
      radar_officer(ship_row, ship_col, guess_col, guess_row)
      print '-------------------------'
      BOARD[guess_row][guess_col] = HIT_MARK

    return result


def main():  
  print_instruction()
  print_board(BOARD)
  ship_row = random_row(BOARD)
  ship_col = random_col(BOARD)
  user_input, rounds = select_level()

  print 'You selected level %s, you have total of %s rounds to sink my ship.'\
        %(user_input, rounds)

  for i in xrange(rounds):
    print 'Round: ' + str(i+1)
    result = guess(ship_row, ship_col)
    if result:
      print '\n'
      print 'I can\'t believe it, you just sank my ship!'
      print 'Congratilations, you Win!'
      print '\n'
      print_victory()
      break
    elif i == rounds - 1 and result == False:
      print '\n'
      print 'Game Over'
      print 'Your base is destryed by my ship...'
      print 'You are now homeless'
      print_defected()



if __name__ == '__main__':
  main()
