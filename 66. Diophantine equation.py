from math import sqrt, floor
from itertools import count
from time import time

start = time()


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

def convergents(alist,n): #takes in a convergent list and returns h,k
    h1=0
    h2=1
    k1=1
    k2=0
    length = len(alist)-1
    for i in count():
        a=alist[((i-1)%length)+1]
        if i==0:
            a=alist[0]
        newh = a*h2+h1
        newk = a*k2+k1
        h1=h2
        k1=k2
        h2=newh
        k2=newk
        if h2**2-n*k2**2==1:
            return h2,k2

x = [x for x in range(1001) if not sqrt(x).is_integer()]
largestx = 0
correspondingd = 0
for i in x:
    smallx = convergents(something(i),i)[0]
    if smallx>largestx:
        largestx=smallx
        correspondingd = i
print(largestx)
print(correspondingd)


print(f"Time taken: {time()-start}")

