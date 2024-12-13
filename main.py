from flask import Flask,render_template

app = Flask('app')

# Route for the homepage
@app.route('/')
def hello_world():
  return render_template("index.html")

#Route for sending SMS messages
@app.route('/sms')
def send_sms():
  import os
  from twilio.rest import Client
  import random
  from space import people_space
  from weather import get_weather
  from hp import get_char
  import json

    #Load Twilio creds and add them to "secrete"

  account_sid = os.environ["TWILIO_ACCOUNT_SID"]
  auth_token = os.environ["TWILIO_AUTH_TOKEN"]
  client = Client(account_sid, auth_token)

#Send sms to student, aka me! I tried sending to another number but it didnt work... and location details

  student = {
      "Binder": {
          "name":"Arvinder",
          "course":"BAPG",
          "number":"+16475298710",#My number
          "location":"Kingston"
      }
  }
#personalized sms with api's

  for key,value in student.items():
      msg=f'Hello {value["name"].title()} The number of people in space are {people_space()} and the city {value["location"]} weather in your location {value["location"]} is:{get_weather(value["location"])} and the Harry Potter character  {get_char()}'

      print(msg)
      message = client.messages.create(
          body=msg,
          from_="+17433305202", # is my virtual number
          to=value["number"], #Receiver number 
      )
      with open('message.json','w') as outfile: # saving the file
          json.dump(message.sid,outfile)
      print(message.body)
# show the success page after sending the SMS
  return render_template("success.html")

app.run(host='0.0.0.0', port=8080)