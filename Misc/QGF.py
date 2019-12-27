def gameended():

    global ended
    ended = True
    
def printans():

    print("")
    for i in range(strength):
        print (players[i]+": "+str(alllist[i])+", Banned: " + str(banlist[i]))

def round(playerno):
    
    index = playerno-1
    print("")
    print(players[index]+", it is your turn.")
    takefrom = input("Which player are you taking from? ")
    
    if takefrom == players[index]:
        print("You can't take cards from yourself. Everyone loses.")
        gameended()
        return
    if takefrom not in players:
        print("That player doesn't exist. Everyone loses.")
        gameended()
        return
    
    takewhat = input("Which card are you taking? ")
    
    if 0 not in alllist[index] and takewhat not in alllist[index]:
        print("You don't have that card. Everyone loses.")
        gameended()
        return
    if takewhat in banlist[index]:
        print("You don't have that card. Everyone loses.")
        gameended()
        return
    if takewhat not in alllist[index]:
        alllist[index].remove(0)
        alllist[index].append(takewhat)
    if takewhat not in suits:
        if len(suits) <strength:
            suits.append(takewhat)
        else:
            print("This suit doesn't exist. Everyone loses.")
            gameended()
            return
    
    yesno = input(takefrom+", do you have the card? ")
    if yesno == "yes":
        if takewhat in alllist[players.index(takefrom)]:
            alllist[players.index(takefrom)].remove(takewhat)
        elif takewhat in banlist[players.index(takefrom)]:
            print ("No you don't. Everyone loses.")
            gameended()
            return
        elif 0 in alllist[players.index(takefrom)]:
            alllist[players.index(takefrom)].remove(0)
        else:
            print ("No you don't. Everyone loses.")
            gameended()
            return
        
        alllist[index].append(takewhat)


    if yesno == "no":
        if takewhat in alllist[players.index(takefrom)]:
            print("Yes you do. Everyone loses.")
            gameended()
            return
        banlist[players.index(takefrom)].append(takewhat)

    def checkstate():

        unknowncards = 0
        for i in alllist:
            unknowncards += i.count(0)
        if unknowncards == 0:
            print("")
            print("")
            print (players[index] + " wins the game! ")
            gameended()
            return True
        else:
            return False

    def check4oak():

        for index in range(strength):
            for j in suits:
                if alllist[index].count(j)>3:
                    print("")
                    print("")
                    print (players[index] + " wins the game! ")
                    gameended()
                    return

    def statesolver():

        initial = alllist
        for suit in suits:
            possibleno=0
            for index in range(strength):
                possibleno += alllist[index].count(suit)
                if suit not in banlist[index]:
                    possibleno += alllist[index].count(0)
            
        
            for index in range(strength):
                playerzero=0
                if suit not in banlist[index]:
                    playerzero = alllist[index].count(0)
                
                if possibleno - playerzero<4 and 0 in alllist[index]:
                    alllist[index].remove(0)
                    alllist[index].append(suit)
        if initial != alllist:
            statesolver()

    statesolver()
    if checkstate() == False:
        check4oak()
    
    printans()
    return
    

def game():

    turns = 0
    while not ended:
        round(turns%strength+1)
        turns += 1
        if ended:
            break



playerstr = input("Welcome to Quantum Go Fish. Enter the players' names, separated by commas:  ")
alllist = []
banlist = []
suits = []
players = playerstr.split(",")
strength = len(players)
ended = False

for i in range(strength):
    alllist.append([0, 0, 0, 0])
    banlist.append([])

printans()

game()
