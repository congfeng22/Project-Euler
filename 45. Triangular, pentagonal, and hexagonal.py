hexagonal = [n*(2*n-1) for n in range(1,100)]
print(hexagonal)

found = False
index=1
while not found:
    hexnum=index*(2*index-1)
    pennum=(1+(1+24*hexnum)**0.5)/6
    trinum = (-1+(1+8*hexnum)**0.5)/2
    if pennum - int(pennum)==0:
        if trinum - int(trinum)==0:
            print(hexnum)
    index+=1
