def isLychrel(n):
    iterations = 0
    for i in range(50):
        n=int(str(n))+int(str(n)[::-1])
        iterations+=1
        if str(n)==str(n)[::-1] and iterations<50:
            
            return False
    else:
        return True
howmany = 0
for i in range(10000):
    if isLychrel(i):
        howmany+=1
print(howmany)
