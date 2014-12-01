def warmupA():
  kitchen = [["south", "entry"],["west", "dining"]]
  dict = {"kitchen":kitchen}
  print dict
  print dict["kitchen"]
def warmupB():
  word =""
  while word!= "stop":
     word = requestString("Enter Word: type stop to end")
  
def game():
    printNow( "*** Welcome to The CSIT Guys’ House of Horrors! ***")
    printNow( "In each room you will be told which directions you can go.")
    printNow( "You'll be able to go north, south, east or west by typing that direction.")
    printNow( "Type help to redisplay this introduction.")
    printNow( "Type exit to quit at any time.")
    userInput = ""
    currentRoom = "entry way"
    rooms = initializeRooms()
    while userInput!="exit":
        printNow("you are now in/on %s" % currentRoom)
        roomOptions = rooms[currentRoom]
        printNow(roomOptions)
        for i in range(0,len(roomOptions)):
            printNow("direction %s room %s" % (roomOptions[i][0],roomOptions[i][1]))
        
        userInput = requestString("Choose a direction")
    printNow("goodbye")
def initializeRooms():
    porch = ["north","entry way"]
    entryway = [["north","kitchen"],["south","porch"],["east","living room"]]
    diningroom = [["north","kitchen"],["east","entry way"]]
    kitchen = [["south","entry way"],["west","dining room"]]
    livingroom = [["north","bathroom"],["west","entry way"],["east","bedroom"]]
    bathroom = ["south","living room"]
    bedroom = ["west","living room"]
    rooms = {"kitchen":kitchen, "porch":porch, "entry way":entryway, "dining room":diningroom, "living room":livingroom,"bathroom":bathroom,"bedroom":bedroom}
    return rooms       
 
def parse(userInput):
    userInput = userInput.lower()
    #error checking 
    if (userInput == "north" or userInput == "south" or userInput == "east" or userInput == "west"):
        return userInput
    elif (userInput == "help" or userInput == "?" or userInput == "h"):
        return "help"
    elif (userInput == "exit"):
        return userInput
    else: 
        return ""

                                                                                  
def hangman():
  import random
  dict = ["happening", "falcon", "spaghetti", "outward", "awesome", "french", "toxic", "equestrian", "pool", "nuisance"]
  word = dict[random.randint(0, len(dict)-1)]
  guesses = 0
  solved = false
  displayWord = ""
  incorrect = "" #string for incorrectly guessed letters
  correct = "" #string for correctly guessed letters
  while guesses<6 and not solved:
    letter = requestString("Enter Letter")
    #if not a letter
    if len(letter)>1 or (letter[0]<"A" or (letter[0]>"Z" and letter[0]<"a") or letter[0]>"z"):
      printNow("Letters only please!")
    #it is a letter
    else:
      letter = letter.lower() 
      
      if letter in word: #if it is a letter in the word
        if letter in correct:#already guessed
          printNow("Already Guessed")
        else:
          correct = correct+letter
          for i in range(0, len(word)):
            if word[i] not in correct:
              solved = false
              break
            else:
              solved = true
          printNow("Correct guess!")
      
      else: #it is an incorrect letter
        if letter in incorrect:#already guessed
          printNow("Already Guessed")
        else:
          incorrect = incorrect + letter 
          printNow("Incorrect")
          guesses += 1
      printNow("Word so far:")
      displayWord = ""
      for i in range(0, len(word)):
        if word[i] in correct:
          displayWord = displayWord + " " + word[i]
        else:
          displayWord = displayWord + " _"
      printNow(displayWord)
      printNow(incorrect)
      printNow("You have used %s out of 6 guesses"  % guesses)
      printNow("")
  if solved:
    printNow("Congratulations you win!")
  else:
    printNow("Sorry, you lose.  Better luck next time!")