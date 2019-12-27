import time
start=time.time()
count=0
for a in range(0,5):
    for b in range(0,11):
        for c in range(0,21):
            for d in range(0,41):
                for e in range(0,101):
                    if 50*a+20*b+10*c+5*d+2*e<201:
                        count+=1
print(count)

count2=0
for a in range(0,3):
    for b in range(0,6):
        for c in range(0,11):
            for d in range(0,21):
                for e in range(0,51):
                    if 50*a+20*b+10*c+5*d+2*e<101:
                        count2+=1
print(count2)
print(count+count2+2)

end=time.time()
print(f"Time taken: {end-start}")
