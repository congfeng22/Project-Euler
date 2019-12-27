import math
primelist = []
n=600851475143
for i in range(2,math.floor(math.sqrt(n))+1):
    
    while n%i==0:
        n=n//i
        primelist.append(i)
        
print(primelist)
