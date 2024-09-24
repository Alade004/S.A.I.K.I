state = "generalchat"

def testIfIn(listOfPhrases, response):
  for phrase in listOfPhrases:
    if phrase in response:
      return True

  return False

#PUNCTUATION
punctuation = ["!", "&", "''", "?", "(", ")", ";", ":", ".", "/", "~", "[", "]", "{", "}", "%", "$", "#", "$", "@", "*", "-", "_", ",", "=" , "+"]
def removePunctuation(string):
  final = ""
  for i in range(len(string)):
    if string[i] not in punctuation:
      final = final + string[i]
  return final

#OPENING
opening = input("Hello my name is Saiki Kusuo. Here you can talk to me about food, hobbies, or being normal(or not). Just don't annoy me. How are you?\n")
opening = removePunctuation(opening)
feeling = ["im good", "im sad", "im mad", "im fine", "im tired", "im hungry", "im annoyed", "good", "bad", "tired", "sad", "fine", "im bored", "bored"]


if opening.lower() in feeling:
  print("Why are you feeling this way?")

else: 
  print("Why?")

reason = input()
print("Ok then...Well I'm definitely not a certified therapist, but I think you should go see one.")

#GENERAL
def general():
  global state
  question = input("What do you want to talk about?\n")

  if "food" in question:
    state = "foodtalk"
  elif "hobbies" in question or "hobby" in question:
    state = "hobbytalk"
  elif "psychic" in question or "powers" in question or "psychic powers" in question:
    state = "normaltalk"
  #BYE
  elif "bye" in question or "quit" in question or "goodbye" in question:
    state = "quit"

#FOOD
def food():
  global state
  response = input("What is your favorite food? Mine's coffee jelly ♡\n")
  response = input("That's nice. I recently bought a coffee jelly machine. Have you ever had it before?\n")
  if response.lower() == "yes" or response.lower() == "yea":
    print("It's so good, right?")
    reply = input()
    if reply == "no" or reply =="nah" or reply == "maybe" or reply == "idk" or reply == "i dont know":
      print("You must like it.")

  else:
    print("Well you should try it.")

  response = input("You should bring me some food.\n")
  while True:
    if response == "coffee jelly" or response == "I will bring coffee jelly":
      print("I love that")
      break
    elif response == "no" or response == "nah":
      break
    else: 
      response = input("No, something else.\n")

  if testIfIn(["hi", "bored", "no", "nah", "idk", "i dont know"], response):
    
    state = "generalchat"
  elif "hobbies" in response or "hobby" in response:
    state = "hobbytalk"
  elif "psychic" in response or "powers" in response or "psychic powers" in response:
    state = "normaltalk"

#HOBBIES
def hobbies():
  global state
  response = input("What are your hobbies?\n")
  print("That sounds like fun. I like to read manga, watch anime, watch TV, and watch movies.")

  if "food" in response:
    state = "foodtalk"
  elif "psychic" in response or "powers" in response or "psychic powers" in response:
    state = "normaltalk"
  else:
    state = "generalchat"


#NORMAL
def normal():
  global state
  response = input("Are you normal?\n")
  if response == "yes" or response == "yea" or response == "yeah" or response == "yep":
    print("✨That's so cool✨")
  else:
    print("Ewwww leave")
  
  state = "generalchat"


#FUNCTIONS
while state != "quit":
  if state == "generalchat":
    general()
  elif state == "foodtalk":
    food()
  elif state == "hobbytalk":
    hobbies()
  elif state == "normaltalk":
    normal()
  