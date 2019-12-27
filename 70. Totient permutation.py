from time import time
from math import sqrt
start = time()

def primes1(n): #returns list of primes <=n
    primelist=[True for i in range(n+1)]
    for i in range(2,int(n**0.5+1)):
        if not primelist[i]:
            continue
        for j in range(i,n//i+1):
            primelist[j*i]= False

    primes=[i for i in range(2,len(primelist)) if primelist[i]]
    return primes

listofprimes = primes1(10000)
minprod = 0
minquo = 999
for i in listofprimes:
    if i<3162:
        continue
    for j in listofprimes[::-1]:
        if j>3162:
            continue
        prod = i*j
        if prod>=10**7:
            continue
        totient = (i-1)*(j-1)
        if sorted(str(prod)) == sorted(str(totient)):
            quo = prod/totient
            if quo<minquo:
                minquo=quo
                minprod = prod
print(minquo)
print(minprod)

print(f"Time taken: {time()-start}")
