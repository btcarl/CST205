inventory =[]

def game():
    printNow("*** Welcome to The CSIT Guys’ House of Horrors! ***")
    printNow("In each room you will be told which directions you can go.")
    printNow("You'll be able to go north, south, east or west by typing that direction.")
    printNow("Type help to redisplay this introduction.")
    printNow("Type exit to quit at any time.")
    userInput = ""
    currentRoom = "porch"
    global inventory
    rooms = initializeRooms()
    while userInput!="exit":
        printNow("you are now in/on %s" % currentRoom)
        #get list of rooms available to travel to from current room
        roomOptions = rooms[currentRoom]
        #if more than one is available
        if isinstance(roomOptions[0],list):
            for i in range(0,len(roomOptions)):
                #list available room options from current room and the direction
                printNow("go %s to the %s" % (roomOptions[i][0],roomOptions[i][1]))
        #else only one available
        else:
            printNow("go %s to the %s" % (roomOptions[0],roomOptions[1]))
        userInput = requestString("Choose a direction")
        userInput = parse(userInput)
        if len(userInput)>0:
            if(userInput!="exit" and userInput!="help" and userInput!= "i"):
                validDirection = false
                for i in range(0,len(roomOptions)):
                   if isinstance(roomOptions[0],list):
                       #check if userinput direction is valid
                       if userInput == roomOptions[i][0]:
                           validDirection = true
                           currentRoom = roomOptions[i][1]
                   else:
                       if userInput == roomOptions[0]:
                           validDirection = true 
                           currentRoom = roomOptions[1]
                if not validDirection:
                    printNow("Direction is unavailable")    
        else:
            printNow("I don't understand what you are saying")
        printNow("")    
    printNow("goodbye")
    
def initializeRooms():
    porch = ["north","entry way"]
    entryway = [["north","kitchen"],["south","porch"],["east","living room"]]
    diningroom = ["east","kitchen"]
    kitchen = [["south","entry way"],["west","dining room"]]
    livingroom = [["north","bathroom"],["west","entry way"],["east","bedroom"]]
    bathroom = ["south","living room"]
    bedroom = ["west","living room"]
    rooms = {"kitchen":kitchen, "porch":porch, "entry way":entryway, "dining room":diningroom, "living room":livingroom,"bathroom":bathroom,"bedroom":bedroom}
    return rooms
    
def parse(userInput):
    if userInput is not None:
        userInput = userInput.lower()
    #error checking 
    if (userInput == "north" or userInput == "south" or userInput == "east" or userInput == "west"):
        return userInput
    elif (userInput == "help" or userInput == "?" or userInput == "h"):
        displayHelp()
        return "help"
    elif (userInput == "exit"):
        return userInput
    elif (userInput == "inventory" or userInput=="i"):
        displayInventory( inventory)
        return "i"
    else: 
        return ""

def displayHelp():
    printNow("You have choosen to display the Help Menu")
    printNow("")
    printNow("*** Welcome to The CSIT Guys’ House of Horrors! ***")
    printNow("In each room you will be told which directions you can go.")
    printNow("You'll be able to go north, south, east or west by typing that direction.")
    printNow("Type help to redisplay this introduction.")
    printNow("Type exit to quit at any time.")
    userInput = ""
    choice = userInput
    return choice
 
def displayInventory(inventory):
    printNow("Inventory:")
    printNow(inventory) 
       
def roomdescription(room):
    printNow("scaryRoom")

