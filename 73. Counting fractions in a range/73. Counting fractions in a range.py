from time import time
from math import gcd

start = time()

limit = 12000
count=0
for den in range(2,limit+1):
    for num in range(den//3,den//2+1):
        quo = num/den
        if quo<=1/3:
            continue
        if quo>=1/2:
            continue
        if gcd(den,num)==1:
            count+=1

print(count)

print(f"Time taken: {time()-start}")
