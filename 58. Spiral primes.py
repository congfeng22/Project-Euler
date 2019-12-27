layers = [3,5,7,9]
primes = [3,5,7]

def isprime(n): #returns True if n is prime, and False otherwise
    if n%2==0 and n!=2 or n==1:
        return False
    for i in range(3,int(n**0.5+1),2):
        if n%i==0:
            return False
    return True

while len(primes)/(len(layers)+1)>=0.1:
    layerno = len(layers)//4
    difference = 2*layerno+2
    lastno=layers[-1]
    for i in range(4):
        newnum = lastno+difference*(i+1)
        layers.append(newnum)
        if isprime(newnum):
            primes.append(newnum)

print((len(layers)//4)*2+1)
