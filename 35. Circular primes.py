primelist=[2]
number = 3
while primelist[-1]<1000:
    counter=0
    for i in primelist:
        if number%i==0:
            counter+=1
    if counter==0:
        primelist.append(number)
    number+=1
    
def isprime(num):
    if num<2:
        return False
    count=0
    if num in primelist:
        return True
    else:
        for i in primelist:
            if num%i==0:
                count+=1
    if count==0:
        return True
    else:
        return False

circcount=0
for i in range(2,1000000):
    if isprime(i):
        istring = str(i)
        rotated = str(i)
        rotated=rotated+rotated[0]
        rotated=rotated[1:]
        count=1
        if istring == rotated:
            circcount+=1
        else:
            while istring!=rotated:
                if isprime(int(rotated)):
                    count+=1
                rotated=rotated+rotated[0]
                rotated=rotated[1:]
            if count==len(istring):
                circcount+=1
print(circcount)
        
        
