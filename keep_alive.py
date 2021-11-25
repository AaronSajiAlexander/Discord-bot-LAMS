#creating a web server for our bot to continuously ping the web server using uptime Robot 
from flask import Flask
from threading import Thread #the server will run on a separate thread from our bot


app = Flask('') #creating a flask app

@app.route('/')
def home():
  return "Hello . I am alive ehehe" #returns this to anyone who visits the server

def run(): #runs the web server
  app.run(host="0.0.0.0",port = 8080)

def keep_alive():
  t = Thread(target = run)
  t.start()
      
