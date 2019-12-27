from itertools import combinations

valuelist = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
suitlist = ["C","D","H","S"]
straightlist = [[valuelist[i+j] for j in range(5)] for i in range(9)]+[["2","3","4","5","A"]]

def vsort(val):
    return valuelist.index(val)

def isstraightflush(hand):#returns a list containing highest card
    value = [card[0] for card in hand]
    value.sort(key=vsort)
    suit = set([card[1] for card in hand])
    if value in straightlist and len(suit)==1:
        return list(value[-1])
    return False
#print(isstraightflush(["9S","QS","KS","TS","JS"]))

def is4oak(hand):#returns a list containing the 4oak value, and last card
    value = [card[0] for card in hand]
    value.sort(key=vsort)
    if len(set(value))==2 and value.count(value[2])==4:
        remaining = [x for x in value if x!= value[2]]
        return [value[2]]+remaining
    return False
#print(is4oak(["9S","9S","KS","9S","9S"]))

def isfullhouse(hand):#returns a list containing the trip value, then pair value
    value = [card[0] for card in hand]
    value.sort(key=vsort)
    if len(set(value))==2 and value.count(value[2])==3:
        remaining = [x for x in [value[0],value[4]] if x!= value[2]]
        return [value[2]]+remaining
    return False
#print(isfullhouse(["9S","9S","KS","KS","9S"]))

def isflush(hand):#returns descending order
    value = [card[0] for card in hand]
    value.sort(key=vsort,reverse=True)
    suit = set([card[1] for card in hand])
    if len(suit)==1:
        return value
    return False
#print(isflush(["9S","2S","KS","3S","7S"]))

def isstraight(hand):#returns a list with highest card
    value = [card[0] for card in hand]
    value.sort(key=vsort)
    if value in straightlist:
        return list(value[-1])
    return False
#print(isstraight(["9S","8S","7S","5S","6S"]))

def is3oak(hand):#returns a list of the trip value and remaining descending
    value = [card[0] for card in hand]
    value.sort(key=vsort)
    if value.count(value[2])==3:
        remaining =[x for x in value if x!= value[2]]
        remaining.sort(key=vsort,reverse=True)
        return [value[2]]+remaining
    return False
#print(is3oak(["9S","5S","9S","JS","9S"]))

def is2pair(hand):#returns a list of the pair values descending and lone card
    value = [card[0] for card in hand]
    value.sort(key=vsort)
    if value.count(value[1])==2 and value.count(value[3])==2:
        pairs = [value[1],value[3]]
        pairs.sort(key=vsort,reverse=True)
        remaining = [x for x in value if x!= value[1] and x!=value[3]]
        return pairs+remaining
    return False
#print(is2pair(["9S","JS","AS","JS","9S"]))

def ispair(hand):#returns a list of the pair value + the others decreasing (2)
    value = [card[0] for card in hand]
    value.sort(key=vsort)
    if value.count(value[1])==2:
        remaining = [x for x in value if x!= value[1]]
        remaining.sort(key=vsort,reverse=True)
        return [value[1]]+remaining
    if value.count(value[3])==2:
        remaining = [x for x in value if x!= value[3]]
        remaining.sort(key=vsort,reverse=True)
        return [value[3]]+remaining
    return False
#print(ispair(["AS","2S","AS","JS","9S"]))

def highcard(hand): #returns descending values
    value = [card[0] for card in hand]
    value.sort(key=vsort,reverse=True)
    return value
#print(highcard(["3S","QS","QS","5H","3D"]))



handlist = [highcard, ispair, is2pair, is3oak, isstraight, isflush, isfullhouse, is4oak, isstraightflush] #functions list

def comparehands(listoffives):#takes in a list of hands, and returns the best hand. Returns a list of best hands if there is a tie
    imptlist = [] #imptlist contains all info of all the hands to be tested
    higheststrength = 0
    
    for combi in listoffives:#iterates through the list. combi is a particular 5-card hand
            
        for hand in handlist[::-1]:
            if hand(combi)!=False:
                speciallist=hand(combi)
                handindex = handlist.index(hand)
                break
        imptlist.append([handindex, speciallist])
        #handindex = 0 for highcard, 8 for straight flush
        #speciallist = the list needed to compare strength
        higheststrength = max(handindex, higheststrength)

    winners = [listoffives[imptlist.index(x)] for x in imptlist if x[0]==higheststrength]
    biggesthands = [x[1] for x in imptlist if x[0]==higheststrength]
    if len(biggesthands)==1:
        return winners
    else:
        for i in range(len(biggesthands[0])):
            listcompare = [biggesthands[x][i] for x in range(len(biggesthands))]
            listcompare.sort(key=vsort,reverse=True)
            maxlistcompare = listcompare[0]
            biggesthands = [x for x in biggesthands if x[i]==maxlistcompare]
            winners = [winners[biggesthands.index(x)] for x in biggesthands if x[i]==maxlistcompare]
        if len(biggesthands)==1:
            return winners
        else:
            return winners


#---------------FOR INTERACTION-----------------#
''' FOR INTERACTIVE GAMEPLAY
p1input = input("Enter Player 1 cards, separated by a space: ")
p2input = input("Enter Player 2 cards, separated by a space: ")
tableinput = input("Enter Table cards, separated by a space: ")
p1list = p1input.split(" ")
p2list = p2input.split(" ")
tablelist = tableinput.split(" ")
'''
#-----------------------------------------------#


#---------------FOR CODE TESTING----------------#
p1list = ["9S","JS"]
p2list = ["3D","4S"]
tablelist = ["KH","TH","JH","AH","QH"]
#-----------------------------------------------#


p1choices = p1list + tablelist
p2choices = p2list + tablelist
p1combis = [list(i) for i in list(combinations(p1choices, 5))]
p2combis = [list(i) for i in list(combinations(p2choices, 5))]

bestp1hand = comparehands(p1combis)
bestp2hand = comparehands(p2combis)
ultimatebest = comparehands(bestp1hand + bestp2hand)

#Presentation below
print(f"Player 1 hand: {p1list}")
print(f"Player 2 hand: {p2list}")
print(f"Table cards: {tablelist}")
print("")

print(f"Player 1 best hand: {bestp1hand}")
print(f"Player 2 best hand: {bestp2hand}")

if ultimatebest == bestp1hand:
    print("Player 1 wins!")

elif ultimatebest == bestp2hand:
    print("Player 2 wins!")
else:
    print("Players tie!")


