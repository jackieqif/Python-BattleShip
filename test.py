from urllib2 import Request, urlopen, URLError


ASCII_URL = {
  'leg': ['http://www.ascii-art.de/ascii/jkl/leg.txt', (270, 2000)],
  'marriage': ['http://www.ascii-art.de/ascii/mno/marriage.txt', (700, 2500)]
}

def print_story(part, message = None):
  url = ASCII_URL[part][0]
  start, end = ASCII_URL[part][1][0], ASCII_URL[part][1][1]
  request = Request(url)
  response = urlopen(request)
  content = response.read()[start:end]
  print content
  print '\n'
  if message:
    print message



if __name__ == '__main__':
  print_story('leg')
  print_story('marriage')
