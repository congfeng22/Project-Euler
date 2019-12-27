from time import time
from math import sqrt, floor

start= time()
nonsquarelist = [x for x in range(1,10001) if sqrt(x).is_integer() == False]

def split(surdlist): #split (sqrt(a)+b)/c into an integer and (sqrt(a)+newb)/c<1
    a=surdlist[0]
    b=surdlist[1]
    c=surdlist[2]
    floored = int(floor(sqrt(a)))
    integer = (floored+b)//c
    newb=b-integer*c
    return [integer, a, newb, c]
#print(split(23,0,1))

def reciprocal(surdlist): #(sqrt(a)+b)/c becomes c/(sqrt(a)+b, then rationalise
    a=surdlist[0]
    b=surdlist[1]
    c=surdlist[2]
    denominator = int((a-b**2)/c)
    insurd = a
    newb = -b
    return [insurd,newb,denominator]
#print(reciprocal(23,-3,2))
    


def something(n): #takes in 7, and outputs [2,1,1,1,4]
    alist = []
    b=0
    c=1
    stoplist = []
    while True:
        splitlist = split([n,b,c])
        alist.append(splitlist[0])
        recilist = reciprocal(splitlist[1:])
        if recilist in stoplist:
            break
        stoplist.append(recilist)
        n=recilist[0]
        b=recilist[1]
        c=recilist[2]
    return alist
        
count=0
for irrational in nonsquarelist:
    thelist = something(irrational)[1:]
    if len(thelist)%2==1:
        count+=1
print(count)

print(f"Time taken: {time()-start}")
