import time
start=time.time()

plist = [0 for i in range(1000)]
for a in range(4,500):
    for b in range(3,a):
        c=(a**2+b**2)**0.5
        p=int(a+b+c)
        if c.is_integer() and p<1000:
            plist[p]+=1
        
print(plist.index(max(plist)))

print(f"Time taken: {time.time()-start}")
