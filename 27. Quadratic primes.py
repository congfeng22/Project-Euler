import time
start_time=time.time()

primelist=[2]
number = 3
while primelist[-1]<1414:
    counter=0
    for i in primelist:
        if number%i==0:
            counter+=1
    if counter==0:
        primelist.append(number)
    number+=1

bprimelist=[2]
bnumber = 3
while bprimelist[-1]<1000:
    bcounter=0
    for i in bprimelist:
        if bnumber%i==0:
            bcounter+=1
    if bcounter==0:
        bprimelist.append(bnumber)
    bnumber+=1


def quadratic(n,a,b):
    return n**2+a*n+b
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
maxvar=0
maxa=0
maxb=0
for b in bprimelist:
    for a in range(-b,1000):
        var =0
        while isprime(quadratic(var,a,b)):
            var+=1
        if var>maxvar:
            maxvar=var
            maxa=a
            maxb=b
print(maxvar)
print(maxa)
print(maxb)

end_time=time.time()
print (f"Total time: {end_time-start_time}")

