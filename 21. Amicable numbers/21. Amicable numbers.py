def factors(n):
    result = []

    for i in range(1, int(n//2 + 1)):
        if n % i == 0:
            result.append(i)
    return sum(result)
sumnum=0
for i in range(1,10001):
    if factors(factors(i))==i and factors(i)!=i:
        sumnum+=i
print(sumnum)
