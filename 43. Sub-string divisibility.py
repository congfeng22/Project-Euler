import itertools
digits = "1234567890"
perms = itertools.permutations(digits)

permsum = 0
for perm in perms:
    if perm[0]=="0":
        continue
    numstr = "".join(perm)
    if int(numstr[7:10])%17==0:
        if int(numstr[6:9])%13==0:
            if int(numstr[5:8])%11==0:
                if int(numstr[4:7])%7==0:
                    if int(numstr[3:6])%5==0:
                        if int(numstr[2:5])%3==0:
                            if int(numstr[1:4])%2==0:
                                permsum+=(int(numstr))
print(permsum)
