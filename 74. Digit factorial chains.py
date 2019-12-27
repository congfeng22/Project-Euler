from time import time
starting = time()

factorial = [1,1,2,6,24,120,720,5040,40320,362880]

test = 10**6

nextdict = {}
nextdict[169]=3
nextdict[363601]=3
nextdict[1454]=3
nextdict[871]=2
nextdict[872]=2
nextdict[45362]=2
nextdict[45361]=2

count=0
listof60 = []
for i in range(test):
    
    ph = i
    alist = []
    if i in nextdict:
        continue
    else:
        while ph not in nextdict:
            alist.append(ph)
            num = 0
            for j in str(ph):
                num+=factorial[int(j)]
            if num == ph:
                nextdict[num]=1
            ph = num
        lastloop = nextdict[ph]
        for j in alist[::-1]:
            lastloop+=1
            nextdict[j]=lastloop
        if lastloop == 60:
            listof60.append(sorted(str(i)))
            count+=1
        
        

print(count)

print(f"Time taken: {time()-starting}")
