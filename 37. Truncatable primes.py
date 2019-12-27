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
listofprimes=primes1(1000000)


'''
def isprime(num):
    if num<2:
        return False
    count=0
    if num in primelist:
        return True
    if count==0:
        return True
    else:
        return False
        '''
truncprime = []
for i in range(11,1000000,2):
    if "2" in str(i)[1:] or "4" in str(i) or "5" in str(i)[1:] or "6" in str(i) or "8" in str(i) or "0" in str(i) or "1" == str(i)[0] or "1" == str(i)[-1] or "9" == str(i)[0] or "9" == str(i)[-1]:
        continue
    if i not in listofprimes:
        continue
    count=0
    for j in range(1,len(str(i))):
        if int(str(i)[:j]) in listofprimes and int(str(i)[j:]) in listofprimes:
            count+=1
    if count==len(str(i))-1:
        print(i)
        truncprime.append(i)
    if len(truncprime)==11:
        break

print(sum(truncprime))
    
            
print(f"Time taken: {time.time()-start}")


