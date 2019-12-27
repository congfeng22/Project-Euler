import time
start=time.time()

def isprime(n):
    if n%2==0 and n!=2 or n==1:
        return False
    for i in range(3,int(n**0.5+1),2):
        if n%i==0:
            return False
    return True

upperbound = 1000000

allprimefactorlist = [[] for i in range(upperbound)]
allprimefactorlist[2]=[2]

for i in range(3,upperbound):
    if isprime(i):
        allprimefactorlist[i].append(i)
    else:
        for factor in range(2,int(i**0.5+1)):
            if i%factor == 0:
                divisor = allprimefactorlist[i//factor]
                if factor not in divisor:
                    allprimefactorlist[i].append(factor)
                allprimefactorlist[i]+=divisor                
                break

    if len(allprimefactorlist[i])==4 and len(allprimefactorlist[i-1])==4 and len(allprimefactorlist[i-2])==4 and len(allprimefactorlist[i-3])==4:
        print(i-3)
        break

print(f"Time taken: {time.time()-start}")
