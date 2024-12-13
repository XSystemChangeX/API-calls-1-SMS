import urllib.request
import json
import random

# get random Harry Potter character and their details
def get_char():
  url='https://hp-api.herokuapp.com/api/characters'
#Make a request to the API and get the data
  request= urllib.request.urlopen(url)
  result = json.loads(request.read())

# create random index to select a character (assuming there are at least 40 characters)

  char = random.randint(1,40) 
  print(char)

#Check if the selected character is a wizard and create follow up response

  if result[char]["wizard"] == True:
    return f"{result[char]['name']} is in the house Wizard and the name of the actor {result[char]['actor']} and the image of the character is {result[char]['image']}"
  else:
    return f"{result[char]['name']} is not in the house Wizard and the name of the actor {result[char]['actor']} and the image of the character is {result[char]['image']}"