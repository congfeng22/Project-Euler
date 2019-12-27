numerator = 1
denominator = 1
for b in range(11,100):
    for a in range(10,b):
        newq=0
        if a%10==0 and b%10==0:
            break
        alist=[int(c) for c in str(a)]
        blist=[int(d) for d in str(b)]
        
        if alist[0] == blist[0]:
            if alist[1]/blist[1] == a/b:
                numerator*=alist[1]
                denominator*=blist[1]
        if alist[0] == blist[1]:
            if alist[1]/blist[0] == a/b:
                numerator*=alist[1]
                denominator*=blist[0]
        if alist[1] == blist[0]:
            if alist[0]/blist[1] == a/b:
                numerator*=alist[0]
                denominator*=blist[1]
        if alist[1] == blist[1]:
            if alist[0]/blist[0] == a/b:
                numerator*=alist[0]
                denominator*=blist[0]
print(numerator)
print(denominator)
