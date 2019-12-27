import time
start=time.time()

count=0
factlist = [1 for x in range(101)]
for i in range(1,101):
    factlist[i] = i*factlist[i-1]
for x in range(23,101):
    for j in range(3,x):
        combi = factlist[x]//(factlist[j]*factlist[x-j])
        if combi>1000000:
            count+=1
print(count)

print(f"Time taken: {time.time()-start}")
