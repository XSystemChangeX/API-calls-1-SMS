import urllib.request
import json

#get the number of people currently in space

def people_space():
  url = 'http://api.open-notify.org/astros.json'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())

#string of the number of people in space
  return f"The number of people in the space are {result['number']}"
