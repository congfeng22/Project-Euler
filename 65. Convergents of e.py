def convergents(numlist,index): #takes in a list and an index, and returns a numerator and denominator
    if index==1:
        return numlist[0]
    
    else:
        a=numlist[index-2]
        b=1
        c=numlist[index-1]
        fracnum = a*c+b
        fracden = c
        for i in range(index-3,-1,-1): #index=4 i = 1,0
            a=numlist[i]
            
            newfracnum = a*fracnum+fracden
            newfracden = fracnum
            fracnum = newfracnum
            fracden = newfracden
    return [fracnum,fracden]

econv = [2]
for i in range(1,100):
    if i%3==1 or i%3==0:
        econv.append(1)
    else:
        econv.append((i+1)//3*2)
numdigit = [int(x) for x in str(convergents(econv,100)[0])]
print(sum(numdigit))
print(convergents([2,1,1,1,4],4))
        
            
