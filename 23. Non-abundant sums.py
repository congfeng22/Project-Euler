abunlist = []
def abundancy(n):
    result = 1

    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            result+=i
            if i!=n//i:
                result+=n//i
        
    if result>n:
        return True
    else:
        return False

allsum=24
for i in range(25,28124):
    for j in range(1,i//2+1):
        if abundancy(j) and abundancy(i-j):
            allsum+=i
            
            break
print(allsum)

