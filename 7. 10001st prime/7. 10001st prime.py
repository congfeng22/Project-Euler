primelist=[2]
number = 3
while len(primelist)<10001:
    counter=0
    for i in primelist:
        if number%i==0:
            counter+=1
    if counter==0:
        primelist.append(number)
    number+=1
print (primelist[-1])
