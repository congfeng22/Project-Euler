import time
start=time.time()


f = open("p054_poker.txt","r")
message = f.read()
listofhands = message.split("\n")[:-1]

valuelist = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
suitlist = ["C","D","H","S"]
straightlist = [[valuelist[i+j] for j in range(5)] for i in range(9)]

def vsort(val):
    return valuelist.index(val)

def isroyalflush(hand):#returns true if is royal flush
    value = [card[0] for card in hand]
    value.sort(key=vsort,reverse=True)
    suit = set([card[1] for card in hand])
    if value == ["A", "K", "Q", "J", "T"] and len(suit)==1:
        return True
    return False
#print(isroyalflush(["AS","QS","KS","TS","JS"]))

def isstraightflush(hand):#returns a list containing highest card
    value = [card[0] for card in hand]
    value.sort(key=vsort)
    suit = set([card[1] for card in hand])
    if value in straightlist and len(suit)==1:
        return list(value[-1])
    return False
#print(isstraightflush(["9S","QS","KS","TS","JS"]))

def is4oak(hand):#returns a list containing the 4oak value
    value = [card[0] for card in hand]
    value.sort(key=vsort)
    if len(set(value))==2 and value.count(value[2])==4:
        return list(value[2])
    return False
#print(is4oak(["9S","9S","KS","9S","9S"]))

def isfullhouse(hand):#returns a list containing the trip value
    value = [card[0] for card in hand]
    value.sort(key=vsort)
    if len(set(value))==2 and value.count(value[2])==3:
        return list(value[2])
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




handlist = [highcard, ispair, is2pair, is3oak, isstraight, isflush, isfullhouse, is4oak, isstraightflush, isroyalflush]
def whowon(p1list, p2list): #returns True if p1list wins
    for hand in handlist[::-1]:
        if hand(p1list)!=False:
            special1list=hand(p1list)
            hand1index = handlist.index(hand)
            break
    
    for hand in handlist[::-1]:
        if hand(p2list)!=False:
            special2list=hand(p2list)
            hand2index = handlist.index(hand)
            break
    
    if hand1index<hand2index:
        return False
    elif hand1index>hand2index:
        return True
    else:
        for i in range(len(special1list)):
            if special1list[i] == special2list[i]:
                continue
            strangelist = [special1list[i], special2list[i]]
            strangelist.sort(key=vsort,reverse=True)
            if strangelist[0]==special1list[i]:
                return True
            elif strangelist[0]==special2list[i]:
                return False
            
        
            

count=0
whichgame=0
for game in listofhands:
    cardlist = game.split(" ")
    p1list = cardlist[:5]
    p2list = cardlist[5:]
    if whowon(p1list,p2list):
        count+=1
print(count)

print(f"Time taken: {time.time()-start}")
