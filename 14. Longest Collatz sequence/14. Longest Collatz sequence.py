def collatz(n):
    count=1
    while n!=1:
        if n%2==0:
            n=n//2
            count+=1
        else:
            n=3*n+1
            count+=1
    return count

countlist = [1]
numlist = []
for i in range(1000000,500000,-1):
    if collatz(i)>max(countlist):
        countlist.append(collatz(i))
        numlist.append(i)

print(countlist[-1])
print(numlist[-1])


