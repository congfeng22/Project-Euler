import time
start = time.time()

posnums=[]

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        digitlist = [a,b,c,d,e,f]
                        n=a**5+b**5+c**5+d**5+e**5+f**5
                        if len(str(n))>6:
                            break
                        for letter in str(n):
                            if int(letter) in digitlist:
                                digitlist.remove(int(letter))
                        
                        if digitlist==[] and n not in posnums:
                            posnums.append(n)


for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    digitlist = [a,b,c,d,e]
                    n=a**5+b**5+c**5+d**5+e**5
                    if len(str(n))>5:
                        break
                    for letter in str(n):
                        if int(letter) in digitlist:
                            digitlist.remove(int(letter))
                    
                    if digitlist==[] and n not in posnums:
                        posnums.append(n)
                        
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                
                digitlist = [a,b,c,d]
                n=a**5+b**5+c**5+d**5
                if len(str(n))>4:
                    break
                for letter in str(n):
                    if int(letter) in digitlist:
                        digitlist.remove(int(letter))
                
                if digitlist==[] and n not in posnums:
                    posnums.append(n)

print(sum(posnums))

end=time.time()
print(f"Time taken: {end-start}")
