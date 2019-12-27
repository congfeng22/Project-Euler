import time
from math import sqrt

start=time.time()

def primes1(n): #returns list of primes <=n, not 2, not 5
    primelist=[True for i in range(n+1)]
    for i in range(2,int(n**0.5+1)):
        if not primelist[i]:
            continue
        for j in range(i,n//i+1):
            primelist[j*i]= False

    primes=[3]+[i for i in range(7,len(primelist)) if primelist[i]]
    return primes

def isprime(n): #returns True if n is prime, and False otherwise
    if n%2==0 and n!=2 or n==1:
        return False
    for i in range(3,int(sqrt(n)+1),2):
        if n%i==0:
            return False
    return True

masterlist = primes1(10000)

def createlist(n): #takes in a prime, and returns a list of bigger primes such that concatenation is a prime
    thelist = []
    for prime in masterlist:
        if n>=prime:
            continue
        if isprime(int(str(n)+str(prime))) and isprime(int(str(prime)+str(n))):
            thelist.append(prime)
    return thelist

masterdict = {}
minsum = 0

for i in masterlist: 
    masterdict[i]=createlist(i)

for i in masterdict: #first one 3
    if masterdict[i]==[]:
        continue
    for j in masterdict[i]: #first one 7
        if masterdict[j]==[]:
            continue
        if i%3!=j%3:
            continue
        twoprimelist=sorted(list(set(masterdict[i]).intersection(masterdict[j])))
        for k in twoprimelist: #first one 109
            if masterdict[k]==[]:
                continue
            if j%3!=k%3:
                continue
            threeprimelist = sorted(list(set(twoprimelist).intersection(masterdict[k])))
            for l in threeprimelist: #first one 673
                if masterdict[l]==[]:
                    continue
                if k%3!=l%3:
                    continue
                fourprimelist = sorted(list(set(threeprimelist).intersection(masterdict[l])))
                if fourprimelist!=[]:
                    anslist = [i,j,k,l,fourprimelist[0]]
                    thesum = sum(anslist)
                    print(f"{i} + {j} + {k} + {l} + {fourprimelist[0]} = {thesum}")
                    
                    if minsum == 0:
                        minsum = thesum
                    elif thesum<minsum:
                        minsum = thesum
print(minsum)        
                    


print(f"Time taken: {time.time()-start}")
