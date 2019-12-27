import time
start=time.time()

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
'''
Note that we only need to test for consecutive primes of length 22 and above.
If none exists, then 953 is the answer.
Note that 1 000 000 / 22 = 45454.
The next lowest prime, 45439, x 22 = 999658
Create a prime list up to 45439, then with the next 21 primes.
45439, ... , 45691
4714th, ..., 4735th prime
This way, the answer MUST be a sequence in this list.

'''


listofprimes = primes1(45691) #list of primes up to 45691 = 4735th prime

primeseries = [0 for i in range(4736)]
primeseries[1]=2
primeseries[2]=5
for i in range(3,4736):
    primeseries[i]=primeseries[i-1]+listofprimes[i-1]

#primeseries[x] = sum of 1st prime to (x)th prime.
#primeseries[b]-primeseries[a] = (a+1)th prime + (a+2)th prime +...+ (b)th prime
#b-a = length of sequence of primes
    
found=False

for difference in range(4734,0,-1):
    for first in range(1,4736-difference):
        diffinsum = primeseries[first+difference]-primeseries[first]
        if diffinsum<1000000 and isprime(diffinsum):
            print(diffinsum)
            found=True
            break
    if found == True:
        break


print(f"Time taken: {time.time()-start}")
