allfractions = [0 for i in range(1001)]
allfractions[1]=[3,2]
allfractions[2]=[7,5]
counter=0
for i in range(3,1001):
    numden=allfractions[i-1]
    newnum = 2*numden[1]+numden[0]
    newden = numden[0]+numden[1]
    allfractions[i] = [newnum,newden]
    if len(str(newnum))>len(str(newden)):
        counter+=1
print(counter)
