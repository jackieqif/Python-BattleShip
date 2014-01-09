# BattleShip board Game
# by jackieq
# reviewed by Yunzhang's Budda power

from random import randint
from urllib2 import Request, urlopen, URLError

BOARD = [['O' for i in xrange(5)] for j in xrange(5)]

LEVEL = {
  1: 12,
  2: 8,
  3: 4
  }

HIT_MARK = "X"


class StoryLine:
  def __init__(self, name = None):
    self.ASCII_URL = {
     'leg': ['http://www.ascii-art.de/ascii/jkl/leg.txt', (270, 2000)],
     'marriage': ['http://www.ascii-art.de/ascii/mno/marriage.txt', (700, 2500)]
    }
    self.name = name

  def print_remote(self, picture, message = None):
    url = self.ASCII_URL[picture][0]
    start, end = self.ASCII_URL[picture][1][0], self.ASCII_URL[picture][1][1]
    request = Request(url)
    response = urlopen(request)
    content = response.read()[start:end]
    print content
    print '\n'
    if message:
      print message

  def print_opening(self):
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
                      /_`( "a `a. )"'
                  (  (/  .  ' )=='
                 (   (    )  .8"   +
                   (`'8a.( _(   (
                ..-. `8P    ) `  )  +
              -'   (      -ab:  )
______       _   _   _        _____ _     _         _____  _____  __    ___ 
| ___ \     | | | | | |      /  ___| |   (_)       / __  \|  _  |/  |  /   |
| |_/ / __ _| |_| |_| | ___  \ `--.| |__  _ _ __   `' / /'| |/' |`| | / /| |
| ___ \/ _` | __| __| |/ _ \  `--. \ '_ \| | '_ \    / /  |  /| | | |/ /_| |
| |_/ / (_| | |_| |_| |  __/ /\__/ / | | | | |_) | ./ /___\ |_/ /_| |\___  |
\____/ \__,_|\__|\__|_|\___| \____/|_| |_|_| .__/  \_____/ \___/ \___/   |_/
                                           | |                              
                                           |_|                              
    @jackieq
    '''

    enter = raw_input('Press Enter to continue...')
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
An alian flagship has been deployed in the board below.
Your goal is to save your nation by sinking the enemy ship as a commander.







  "We need to eliminate  
   all species here,         "Let us start from people working for Google, 
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

    enter = raw_input('Press Enter to continue...')
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

You just need to provide row and colum number 
as coodinates for your missle to hit target.




    '''
    self.name = raw_input('Ready? Enter your name here:')
    print '''




_____________________________________________

         Entering into battle area... 
_____________________________________________


                    |
                    |
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


    '''

  def print_radar1(self):
    print """
                  .-  _           _  -.
                 /   /             \   .
                (   (  (` (-o-) `)  )   )
                 \   \_ `  -+-  ` _/   /
                  `-       -+-       -`
                           -+-
              __  _   ___  _|_  ___   __ ___"""

  def print_radar2(self):
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
    .'   |_______|/ """

  def print_radar3(self):
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
           // ||||| """

  def print_defected(self):
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
  def print_victory(self):
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
       """# end of Story class


def print_board(BOARD):
  print '''
     N
   W-|-E
     S
  '''
  print '   ' +' '.join([str(i) for i in xrange(1,6)])
  print '   ' + '-'.join(['-' for i in xrange(5)])
  for row in xrange(5):
    print str(row + 1) + '| ' + ' '.join(BOARD[row])


def select_level():
  while True:
    try:
      user_input = int(raw_input('Please select game level: 1~3: '))
    except:
      user_input = ''
    if user_input not in [1,2,3]:
      print 'Please input a number from 1 to 3'
    else:
      return user_input, LEVEL[user_input]


def random_row(BOARD):
  return randint(0, len(BOARD) - 1)


def random_col(BOARD):
  return randint(0, len(BOARD[0]) - 1)


def radar_officer(story, ship_row, ship_col, guess_col, guess_row):
  if ship_row - guess_row < 0:
    story.print_radar1()
    print '((( Radar station1: Commander, enemy is up north )))'
  elif ship_row - guess_row > 0:
    story.print_radar1()
    print '((( Radar station1: Commander, enemy is down south )))'
  else:
    story.print_radar2()
    print '((( Radar station1: Commander, we are on the right row! )))'

  if ship_col - guess_col < 0:
    print '((( Radar station2: Commander, enemy is further west )))'
  elif ship_col - guess_col > 0:
    print '((( Radar station2: Commander, enemy is further east )))'
  else:
    print '((( Radar station2: Commander, we are on the right column! )))'

  if abs(ship_col - guess_col) == 1 and abs(ship_row - guess_row) == 1:
    story.print_radar3()
    print '((((( Beep... Beep... radar station3 detected that enemy is one \
coodinate away from your last hit point!!! ))))'


def guess(story, ship_row, ship_col):
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
      radar_officer(story, ship_row, ship_col, guess_col, guess_row)
      print '\n'
      BOARD[guess_row][guess_col] = HIT_MARK

    return result


def main():  
  story = StoryLine()
  story.print_opening()
  ship_row = random_row(BOARD)
  ship_col = random_col(BOARD)
  user_input, rounds = select_level()

  print 'You selected level %s, you have total of %s rounds to sink the alien ship.'\
        %(user_input, rounds)

  for i in xrange(rounds):
    print 'Round: ' + str(i+1)
    result = guess(story, ship_row, ship_col)
    if result:
      print '\n'
      print 'I can\'t believe it, you just sank my ship!'
      print 'Congratilations, you Win!'
      print '\n'
      story.print_victory()
      break
    elif i == rounds - 1 and result == False:
      print '\n'
      print 'Game Over'
      print 'Your base is destryed by my ship...'
      print 'You are now homeless'
      story.print_defected()



if __name__ == '__main__':
  main()
