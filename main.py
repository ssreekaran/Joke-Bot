import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

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

  custom_jokes = ["Why did the programmer cross the road? - To get to the other side."]
  all_jokes = ["Why did the programmer cross the road? - To get to the other side.", get_joke(), get_prog_joke(), get_misc_joke(), get_pun_joke(), get_spok_joke(), get_xmas_joke()]
  sad_words = ["sad", "unhappy", "sorrowful", "dejected", "regretful", "depressed", "downcast", "miserable", "downhearted", "despondent", "despairing", "disconsolate", "out of sorts"]

  if message.content.startswith('$commands'):
    await message.channel.send("$joke: prints any joke from the joke API or custom ones\n$prog: prints programming jokes from the joke API\n$misc: prints miscellaneous jokes from the joke API\n$dark: prints dark jokes from the joke API\n$pun: prints punny jokes from the joke API\n$spok: prints halloween themed jokes from the joke API\n$xmas: prints christmas themed jokes from the joke API\n$cust: prints custom jokes that can be added by users\n$new: used to add custom jokes, by adding the joke after the command\n$del: deletes custom jokes, by adding the index of the joke after the command")
  
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

  options = all_jokes
  if "jokes" in db.keys():
    options.extend(db["jokes"])

  if message.content.startswith('$cust'):
    joke = custom_jokes
    joke.extend(db["jokes"])
    await message.channel.send(random.choice(joke))

  if any(word in msg for word in sad_words):
    await message.channel.send("Don\'t be sad, here\'s a joke. \n" + random.choice(options))

  if msg.startswith("$new"):
    all_jokes = msg.split("$new ",1)[1]
    update_cust_joke(all_jokes)
    await message.channel.send("New joke added.")

  if msg.startswith("$del"):
    jokes = []
    if "jokes" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_joke(index)
      jokes = db["jokes"]
    await message.channel.send(jokes)

keep_alive()
client.run(os.getenv('TOKEN'))