def primes1(n): #returns list of primes <=n
    primelist=[True for i in range(n+1)]
    for i in range(2,int(n**0.5+1)):
        if not primelist[i]:
            continue
        for j in range(i,n//i+1):
            primelist[j*i]= False

    primes=[i for i in range(2,len(primelist)) if primelist[i]]
    return primes

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
print(primefactors(100))
