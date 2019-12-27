
def recurring(r,d):
    global extracount
    while r<d:
        r*=10
        
    
    remainder = r-d*(r//d)
    if remainder == 0:
        return 0
    if remainder in remlist:
        return len(remlist[remlist.index(remainder):])

    remlist.append(remainder)
    ph=0
    testremainder=remainder
    while testremainder<d:
        testremainder*=10
        ph+=1
    if ph>1:
        for i in range(1,ph):
            remlist.append(0)

    
    return recurring(remainder,d)


maxcount=0
for i in range(1,1000):
    extracount=0
    remlist=[]
    thecount=recurring(1,i)
    if thecount>maxcount:
        maxcount=thecount
    
print(maxcount)
