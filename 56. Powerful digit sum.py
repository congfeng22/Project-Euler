maxsum = 0
for a in range(2,100):
    for b in range(2,100):
        sumdigit = 0
        for i in str(a**b):
            sumdigit+=int(i)
        if sumdigit>maxsum:
            maxsum=sumdigit
print(maxsum)
