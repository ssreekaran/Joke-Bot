import discord
import os
import requests
import json
import random
from replit import db

client = discord.Client()

def get_joke():
  response = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit")
  json_data = json.loads(response.text)
  if(json_data['type'] == "single"):
    quote = json_data['joke']
  else:
    quote = json_data["setup"] + " -" + json_data["delivery"]
  return(quote)
  
def get_prog_joke():
  response = requests.get("https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit")
  json_data = json.loads(response.text)
  if(json_data['type'] == "single"):
    quote = json_data['joke']
  else:
    quote = json_data["setup"] + " -" + json_data["delivery"]
  return(quote)

def get_misc_joke():
  response = requests.get("https://v2.jokeapi.dev/joke/Miscellaneous?blacklistFlags=nsfw,religious,political,racist,sexist,explicit")
  json_data = json.loads(response.text)
  if(json_data['type'] == "single"):
    quote = json_data['joke']
  else:
    quote = json_data["setup"] + " -" + json_data["delivery"]
  return(quote)

def get_dark_joke():
  response = requests.get("https://v2.jokeapi.dev/joke/Dark?blacklistFlags=nsfw,religious,political,racist,sexist,explicit")
  json_data = json.loads(response.text)
  if(json_data['type'] == "single"):
    quote = json_data['joke']
  else:
    quote = json_data["setup"] + " -" + json_data["delivery"]
  return(quote)

def get_pun_joke():
  response = requests.get("https://v2.jokeapi.dev/joke/Pun?blacklistFlags=nsfw,religious,political,racist,sexist,explicit")
  json_data = json.loads(response.text)
  if(json_data['type'] == "single"):
    quote = json_data['joke']
  else:
    quote = json_data["setup"] + " -" + json_data["delivery"]
  return(quote)

def get_spok_joke():
  response = requests.get("https://v2.jokeapi.dev/joke/Spooky?blacklistFlags=nsfw,religious,political,racist,sexist,explicit")
  json_data = json.loads(response.text)
  if(json_data['type'] == "single"):
    quote = json_data['joke']
  else:
    quote = json_data["setup"] + " -" + json_data["delivery"]
  return(quote)

def get_xmas_joke():
  response = requests.get("https://v2.jokeapi.dev/joke/Christmas?blacklistFlags=nsfw,religious,political,racist,sexist,explicit")
  json_data = json.loads(response.text)
  if(json_data['type'] == "single"):
    quote = json_data['joke']
  else:
    quote = json_data["setup"] + " -" + json_data["delivery"]
  return(quote)

#def get_quote():
#  response = requests.get("https://zenquotes.io/api/random")
#  json_data = json.loads(response.text)
#  quote = json_data[0]['q'] + " -" + json_data[0]['a']
#  return(quote)

custom_jokes = ["Why did the programmer cross the road? - To get to the other side.", get_joke(), get_prog_joke(), get_misc_joke(), get_pun_joke(), get_spok_joke(), get_xmas_joke()]
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

def update_cust_joke(cust_joke):
  if "jokes" in db.keys():
    jokes = db["jokes"]
    jokes.append(cust_joke)
    db["jokes"] = jokes
  else:
    db["jokes"] = [cust_joke]

def delete_joke(index):
  jokes = db["jokes"]
  if len(jokes) > index:
    del jokes[index]
  db["jokes"] = jokes

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
    
  if message.content.startswith('$joke'):
    joke = get_joke()
    await message.channel.send(joke)

  if message.content.startswith('$prog'):
    joke = get_prog_joke()
    await message.channel.send(joke)
    
  if message.content.startswith('$misc'):
    joke = get_misc_joke()
    await message.channel.send(joke)
        
  if message.content.startswith('$dark'):
    joke = get_dark_joke()
    await message.channel.send(joke)
        
  if message.content.startswith('$pun'):
    joke = get_pun_joke()
    await message.channel.send(joke)
        
  if message.content.startswith('$spok'):
    joke = get_spok_joke()
    await message.channel.send(joke)
        
  if message.content.startswith('$xmas'):
    joke = get_xmas_joke()
    await message.channel.send(joke)

  options = custom_jokes
  if "jokes" in db.keys():
    options = options + db["jokes"]

  if any(word in msg for word in sad_words):
    await message.channel.send("Don\'t be sad, here\'s a joke. \n" + random.choice(custom_jokes))

client.run(os.getenv('TOKEN'))