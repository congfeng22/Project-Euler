def factors(n):
    result = 1

    for i in range(1, int(n//2 + 1)):
        if n % i == 0:
            result+=1
    return result


ph=0
index=1
while ph<500:
    if index%2==1:
        ph=factors(index)*factors((index+1)//2)
    else:
        ph=factors(index//2)*factors(index+1)
    index+=1
print(index*(index-1)//2)



