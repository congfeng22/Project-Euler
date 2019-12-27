import itertools

def primes1(n): #returns list of primes <=n
    primelist=[True for i in range(n+1)]
    for i in range(2,int(n**0.5+1)):
        if not primelist[i]:
            continue
        for j in range(i,n//i+1):
            primelist[j*i]= False

    primes=[i for i in range(2,len(primelist)) if primelist[i]]
    return primes
listofprimes=primes1(3163)

digits = [1,2,3,4,5,6,7,8,9]

for i in [4,7]:
    pandigits=digits[:i]
    numberlist = list(itertools.permutations(pandigits))
    
    for j in numberlist:
        jint = sum([k*(10**(len(j)-j.index(k)-1)) for k in j])
        if jint in listofprimes:
            print(jint)
        else:
            counter = 0
            for primes in listofprimes:
                if jint%primes==0:
                    counter+=1
            if counter==0:
                print(jint)
            
