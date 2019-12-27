from time import time
from math import gcd, sqrt

start = time()
limit = 1000000


def isprime(n): #returns True if n is prime, and False otherwise
    if n%2==0 and n!=2 or n==1:
        return False
    for i in range(3,int(n**0.5+1),2):
        if n%i==0:
            return False
    return True



def totient(n):#Uses isprime(n). Returns a list of totient(n) up to n-1
    
    totientlist = [0]*n
    totientlist[1]=1
    
    for i in range(2,n):
        if isprime(i):
            totientlist[i]=i-1
        else:
            for factor in range(2,int(i**0.5+1)):
                if i%factor == 0:
                    divisor = i//factor
                    if gcd(factor,divisor)==1:
                        totientlist[i]=totientlist[factor]*totientlist[divisor]
                        break
                    else:
                        totientlist[i]=totientlist[divisor]*factor
                        break
    return totientlist
print(sum(totient(limit+1))-1)





print(f"Time taken: {time()-start}")
