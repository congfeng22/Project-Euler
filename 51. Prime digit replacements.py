import time
start=time.time()

def primes1(n): #returns list of primes 56003 <= p <= n
    primelist=[True for i in range(n+1)]
    for i in range(2,int(n**0.5+1)):
        if not primelist[i]:
            continue
        for j in range(i,n//i+1):
            primelist[j*i]= False

    primes=[i for i in range(56003,len(primelist)) if primelist[i]]
    return primes

def isprime(n): #returns True if n is prime, and False otherwise
    if n%2==0 and n!=2 or n==1:
        return False
    for i in range(3,int(n**0.5+1),2):
        if n%i==0:
            return False
    return True

listofprimes = primes1(1000000)
for j in listofprimes:
    found=False
    for i in range(2,64):
        binary = int(bin(i)[2:])
        indexlist = [len(str(binary))-x for x in range(len(str(binary))) if str(binary)[x]=="1"]
    
        if len(str(j))<len(str(binary)):
            continue

        relevantdigits = [int(str(j)[-x]) for x in indexlist]
        digitset = set(relevantdigits)
        if digitset == {0} or digitset == {1} or digitset == {2}:
            count = 0
            for k in range(10-int(relevantdigits[0])):
                if isprime(j+k*binary):
                    count+=1
            if count==8:
                print(j)
                print(binary)
                print("--------")
                found=True
                break
    if found==True:
        break
        

        
print(f"Time taken: {time.time()-start}")

'''
print(bin(123))
'''
