cubelist = [int("".join(sorted(str(x**3),reverse=True))) for x in range(0,10000)]

for i in cubelist:
    if cubelist.count(i)==5:
        print(cubelist.index(i)**3)
        break
