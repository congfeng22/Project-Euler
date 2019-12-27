factorials = [1,1,2,6,24,120,720,5040,40320,362880]
for i in range(10,2999999):
    ilist = [int(j) for j in str(i)]
    sumfact = 0
    for k in ilist:
        sumfact+=factorials[k]
    if sumfact==i:
        print(i)
