def isprime(n):
    if n==1:
        return False
    if n%2==0 and n != 2:
        return False
    for i in range(3,int(n**0.5+1),2):
        if n%i==0:
            return False
    return True
oddcomplist = []
for i in range(9,50000,2):
    if not isprime(i):
        oddcomplist.append(i)
found = False

for i in oddcomplist:
    
    count=0
    for j in range(1,int(((i-3)//2)**0.5)+1):
        prime=i-2*(j)**2
        if isprime(prime):

            count=1
            break
    if count==0:
        found=True
    if found == True:
        print(i)
        break
            


