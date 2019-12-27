from time import time

start = time()

#a/b<3/7
#3b-7a=1
#3b-1 /7
alist = []
for b in range(1000000,6,-1):
    a=(3*b-1)/7
    if a.is_integer():
        alist.append([a/b,int(a),b])
alist.sort(reverse=True)
print(alist[0])

print(f"Time taken: {time()-start}")
