import os
import discord
import requests
import json
from keep_alive import keep_alive #the code for this file is given in another separate file

client = discord.Client()


#user defined function to get quotes from that particular site
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -"+ json_data[0]['a']
  return quote


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  #upon finding the exact phrase in any channel , the bot will send a random enouragement quote from zenquotes site
  if message.content.find("say a quote") != -1:
    quote = get_quote()
    await message.channel.send(quote)
  
  #to receive that particular word from a specific person and respond in that channel 
  elif (message.content.find("lams") != -1) and message.author.id ==784130619054872878:
    await message.channel.send(" Hello Guest 1 !")

 #to receive a particular word in any channel frm any user and respond 
  elif message.content.find("hello") != -1:
    await message.channel.send("hello there !")
    
#to receive a particular word from any user in any channel and reply with an img . The img must be available in that project
  elif message.content.find("me?") != -1:
    await message.channel.send(file = discord.File('me.jpg'))

  
#the password if the bot is stored in a key called TOKEN and that is mapped using os.environ and stored in a variable called my_secret
my_secret = os.environ['TOKEN']

keep_alive() #keeps the bot alive . the code for this function is given in another file
client.run(my_secret) #runs the bot
