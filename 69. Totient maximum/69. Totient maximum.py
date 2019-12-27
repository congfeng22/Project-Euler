from time import time
start = time()
def isprime(n): #returns True if n is prime, and False otherwise
    if n%2==0 and n!=2 or n==1:
        return False
    for i in range(3,int(n**0.5+1),2):
        if n%i==0:
            return False
    return True


def primefactors(n):#Uses isprime(n). Returns a list of lists of distinct prime factors of numbers <n
    
    allprimefactorlist = [[] for i in range(n)]
    allprimefactorlist[2]=[2]

    for i in range(3,n):
        if isprime(i):
            allprimefactorlist[i].append(i)
        else:
            for factor in range(2,int(i**0.5+1)):
                if i%factor == 0:
                    divisor = allprimefactorlist[i//factor]
                    if factor not in divisor: # remove this condition if repeated prime factors allowed
                        allprimefactorlist[i].append(factor)
                    allprimefactorlist[i]+=divisor                
                    break
    return allprimefactorlist
allfactors = primefactors(1000001)
maxquo = 0
maxn =0
for i in range(len(allfactors[2:])):
    totient = i+2
    for j in allfactors[i+2]:
        totient/= j
        totient*=j-1
    quo = (i+2)/totient
    if maxquo<quo:
        maxquo=quo
        maxn = i+2
print(maxquo)
print(maxn)

print(f"Time taken: {time()-start}")
