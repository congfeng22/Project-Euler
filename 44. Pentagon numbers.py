import time
start=time.time()

pentagon = [i*(3*i-1)//2 for i in range(1,3000)]
for a in pentagon:
    for b in pentagon[pentagon.index(a)+1:]:
        if b-a in pentagon:
            if b+a in pentagon:
                print(f"{b}, {a}, {b-a}")




print(f"Time taken: {time.time()-start}")
