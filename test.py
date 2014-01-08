from urllib2 import Request, urlopen, URLError


class Story:
  def __init__(self):
    self.ASCII_URL = {
     'leg': ['http://www.ascii-art.de/ascii/jkl/leg.txt', (270, 2000)],
     'marriage': ['http://www.ascii-art.de/ascii/mno/marriage.txt', (700, 2500)]
    }

  def print_page(self, picture, message = None):
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
Your ship is equipped with advanced shield and guided missle.

You will need to provide row and colum coodinates to 
and colum number as coodinates for your missle.

    '''
    name = raw_input('Ready? Enter your name here:')
    print '''




_____________________________________________

         Entering into battle area... 
_____________________________________________



    '''


if __name__ == '__main__':
  story = Story()
  story.print_opening()
