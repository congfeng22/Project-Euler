import itertools, time
start = time.time()
def permgenerator(num):
    digitlist = [int(i) for i in str(num)]
    perms = itertools.permutations(digitlist)
    permslist = []
    for i in perms:
        permnum = sum([i[k]*(10**(len(i)-k-1)) for k in range(len(i))])
        permslist.append(permnum)
    return list(set(permslist))

def isprime(n):
    if n%2==0 and n!=2 or n==1:
        return False
    for i in range(3,int(n**0.5+1),2):
        if n%i==0:
            return False
    return True

for i in range(1001,10000,2):
    if not isprime(i):
        continue
    listofperms = permgenerator(i)
    for j in listofperms:
        if len(str(j))!=4:
            continue
        if i>=j:
            continue
        if not isprime(j):
            continue
        thirdnum = j-i+j
        if thirdnum in listofperms:
            if isprime(thirdnum):
                print(f"{i}, {j}, {thirdnum}")

print(f"Time taken: {time.time()-start}")
