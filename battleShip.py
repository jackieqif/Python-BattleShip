# BattleShip board Game
# by jackieq
# reviewed by Yunzhang's Budda power

from random import randint
from urllib2 import Request, urlopen, URLError

BOARD = [['O' for i in xrange(5)] for j in xrange(5)]

LEVEL = {
  1: 10,
  2: 6,
  3: 3
  }

HIT_MARK = "X"


class StoryLine:
  def __init__(self, name=None):
    self.ASCII_URL = {
      'leg': ['http://www.ascii-art.de/ascii/jkl/leg.txt', (270, 2000)],
      'marriage': ['http://www.ascii-art.de/ascii/mno/marriage.txt', (700, 2500)]
    }
    self.name = name

  def PrintRemote(self, picture, message = None):
    url = self.ASCII_URL[picture][0]
    start, end = self.ASCII_URL[picture][1][0], self.ASCII_URL[picture][1][1]
    request = Request(url)
    response = urlopen(request)
    content = response.read()[start:end]
    print content
    print '\n'
    if message:
      print message

  def PrintOpening(self):
    print '''
                                                   ,:
                                                 ,' |
                                                /   :
                                             --'   /
                                             \/ />/
                                             / <///
                                          __/   /
                                          )'-. /
                                          ./  :\ 
                                           /.' '
                                         '/'
                                         +
                                        '
                                      `.
                                  .-"-     
                                 (    |
                              . .-'  '.
                             ( (.   )8:
                         .'    / (_  )
                          _. :(.   )8P  `
                      .  (  `-' (  `.   .
                       .  :  (   .a8a)
                      /_`( "a `a. )"'  '
                  (  (/  .  ' )=='') ` a `
                 (   (    )  .8"   +)) `) ` `
______       _   _   _        _____ _     _         _____  _____  __    ___ 
| ___ \     | | | | | |      /  ___| |   (_)       / __  \|  _  |/  |  /   |
| |_/ / __ _| |_| |_| | ___  \ `--.| |__  _ _ __   `' / /'| |/' |`| | / /| |
| ___ \/ _` | __| __| |/ _ \  `--. \ '_ \| | '_ \    / /  |  /| | | |/ /_| |
| |_/ / (_| | |_| |_| |  __/ /\__/ / | | | | |_) | ./ /___\ |_/ /_| |\___  |
\____/ \__,_|\__|\__|_|\___| \____/|_| |_|_| .__/  \_____/ \___/ \___/   |_/
                                           | |                              
                                           |_|             jackieq@
    '''

    Continue()
    print '\n' * 5
    print '''

________________________________________________________________________________
 ,    _, ___,'_,    ,_, _     ,  ,     __  _  ___,___,    _, _, , ,  ___, ,_! 
 |   /_,' |  (_,    |_)'|\    \_/     '|_)'|\' | ' | |   /_,(_, |_|,' |   |_) 
'|__'\_   |   _)   '|'|_|-\  , /`     _|_) |-\ |   |'|__'\_  _)'| |  _|_,'|   
   '   `  '  '      '   '  `(_/      '     '  `'   '   '   `'   ' ` '     '   
________________________________________________________________________________

    '''
    print '''
A invading alian flagship has been detected.
Your goal is to save your nation by sinking the enemy ship as a commander.





  "We need to eliminate  
   all species here,         "... people working for Google, 
  where should we start       they are the ones most likely could stop us..."
      from?"               
             \  _.-'~~~~'-._   /
      .      .-~ \__/  \__/ ~-.         .
           .-~   (oo)  (oo)    ~-.
          (_____//~~ O//~~ O______)
     _.-~`                         `~-._
    /O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O\     *
    \___________________________________/
               \\x x x x x x x/
       .  *     \\x_x_x_x_x_x/


'''
    Continue()
    print '''







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


   '''
    print '''

This is your ship, Commander.
It is equipped with advanced shield and guided missle.



    '''

  def print_entering(self):
    print '''
_____________________________________________

         Entering into battle area... 
_____________________________________________
                    
           |        |
         |-|-|      |
           |        |
           | {O}    |
           '--|     |
             .|]_   |
       _.-=.' |     |
      |    |  |]_   |
      |_.-='  |   __|__
       _.-='  |\   /|\\
      |    |  |-'-'-'-'-.
      |_.-='  '========='
           `   |     |
            `. |    / \\
              ||   /   \____.
              ||_.'--=='    |       //  //   / /
              ||  |    |    |\\\    //  //   / /                      ___
 ____         ||__|____|____| \||_/ |_/ |__/  \ __________________/|   |
|    |______  |===.---. .---.========''=-./// |     |     |     / |   |
|    ||     |\| |||   | |   |      '===' ||  \|_____|_____|____/__|___|
|-.._||_____|_\___'---' '---'______....---===''======//=//////========|
|--------------\------------------/-----------------//-//////---------/
|               \                /                 // //////         /
|                \______________/                 // //////         /
|                                        _____===//=//////=========/
|==============================================================   /
'----------------------------------------------------------------`
    
Remember, you just need to provide row and colum number 
as coordinate for your missle to hit the hidden alien ship.
    '''
    Continue()

  def PrintRadar1(self):
    print """
                  .-  _           _  -.
                 /   /             \   .
                (   (  (` (-o-) `)  )   )
                 \   \_ `  -+-  ` _/   /
                  `-       -+-       -`
              __  _   ___  _|_  ___   __ ___"""

  def PrintRadar2(self):
    print """
                   O
                   |
                   |  
             ______|
          /______  |
         |       | |      
         | ===== | |     
         | ===== | |    
         |       | |         
         |  .-.  | |       o    
         | ' . ' | |    ~-       
      ..'| '._.' | |  o
    .'   |_______|/ """

  def PrintRadar3(self):
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
            ||||  ``-...__..-` """

  def PrintDefected(self):
    print '''

    You base was destroyed,
    and you become homeless...


                                 ____
                     __,-~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  \___
- ------===;;;'====------------------===;;;===----- -  -
                  \/  ~"~"~"~"~"~\~"~)~"/
                  (_ (   \  (     >    \)
                   \_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ")
------------------------------------------------------------------



  ______                       _____                   
 / _____)                     / ___ \                  
| /  ___  ____ ____   ____   | |   | |_   _ ____  ____ 
| | (___)/ _  |    \ / _  )  | |   | | | | / _  )/ ___)
| \____/( ( | | | | ( (/ /   | |___| |\ V ( (/ /| |    
 \_____/ \_||_|_|_|_|\____)   \_____/  \_/ \____)_|    



'''
    Continue()

    print '''
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



    You managed to escape though...

                                    
                                      \   O,
                            \___________\/ )_________/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      '''

  def PrintVictory(self):
    print '''

      I can\'t believe it, you just sank my ship!
      Congratilations, you Win!

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
      '''# end of Story class


def PrintBoard(BOARD):
  print '''
     N
   W-|-E
     S
  '''
  print '   ' +' '.join([str(i) for i in xrange(1,6)])
  print '   ' + '-'.join(['-' for i in xrange(5)])
  for row in xrange(5):
    print str(row + 1) + '| ' + ' '.join(BOARD[row])


def SelectLevel():
  while True:
    try:
      user_input = int(raw_input('Please select game level (1~3): '))
    except:
      user_input = ''
    if user_input not in [1,2,3]:
      print 'Please input a number from 1 to 3'
    else:
      print '\n' * 11
      print '__________________________________________________________________'
      print 'You selected level %s, you have total of %s rounds to sink \
the alien ship.'%(user_input, LEVEL[user_input])
      print '__________________________________________________________________'
      print '\n'*2
      print 'Alian Ship detetcted! Missile waiting for target coordinate..'
      print '\n' * 11
      raw_input('Press Enter to continue...')
      return user_input, LEVEL[user_input]


def RandomRow(BOARD):
  return randint(0, len(BOARD) - 1)


def RandomCol(BOARD):
  return randint(0, len(BOARD[0]) - 1)


def RadarOfficior(story, ship_row, ship_col, guess_col, guess_row):
  if ship_row - guess_row < 0:
    story.PrintRadar1()
    print '((( Radar station1: Commander, enemy is up north )))'
  elif ship_row - guess_row > 0:
    story.PrintRadar1()
    print '((( Radar station1: Commander, enemy is down south )))'
  else:
    story.PrintRadar2()
    print '((( Radar station1: Commander, we are on the right row! )))'

  if ship_col - guess_col < 0:
    print '((( Radar station2: Commander, enemy is further west )))'
  elif ship_col - guess_col > 0:
    print '((( Radar station2: Commander, enemy is further east )))'
  else:
    print '((( Radar station2: Commander, we are on the right column! )))'

  if abs(ship_col - guess_col) == 1 and abs(ship_row - guess_row) == 1:
    story.PrintRadar3()
    print '((((( Beep... Beep... radar station3 detected that enemy is one \
coodinate away from your last hit point!!! ))))'


def Guess(story, ship_row, ship_col):
  PrintBoard(BOARD)
  result = False
  try:
    guess_row = int(raw_input('Target Row (1~5):')) - 1
    guess_col = int(raw_input('Target Col (1_5):')) - 1
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
      RadarOfficior(story, ship_row, ship_col, guess_col, guess_row)
      BOARD[guess_row][guess_col] = HIT_MARK
    return result


def StartOver():
  while True:
    user_input = raw_input('Play again? (y/n): ')
    if user_input == 'y':
      return True
    elif user_input == 'n':
      return False
    else:
      print 'Sorry Commander, I can not understand your instruction... \n'

def Continue():
  raw_input('Press Enter to continue...')

def Main():  

  while True:
    story = StoryLine()
    story.PrintOpening()
    ship_row = RandomRow(BOARD)
    ship_col = RandomCol(BOARD)
    user_input, rounds = SelectLevel()
    story.print_entering()

    for i in xrange(rounds):
      print 'Round: ' + str(i+1)
      result = Guess(story, ship_row, ship_col)
      if result:
        story.PrintVictory()
        break
      elif i == rounds - 1 and result == False:
        story.PrintDefected()

    if not StartOver():
      break

if __name__ == '__main__':
  Main()
