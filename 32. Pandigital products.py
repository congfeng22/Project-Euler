import time
start=time.time()

digits=[1,2,3,4,5,6,7,8,9]
anslist = []
for j in range(123,988):
    for i in range(12,99):
        prod = i*j
        
        prodlist = [int(a) for a in str(prod)]
        jlist = [int(b) for b in str(j)]
        ilist= [int(c) for c in str(i)]
        if len(prodlist)!=4:
            break
        
        digitcount=[]
        for k in digits:
            count=0
            if k in ilist:
                count+=1
            if k in jlist:
                count+=1
            if k in prodlist:
                count+=1
            digitcount.append(count)
        if digitcount==[1,1,1,1,1,1,1,1,1] and prod not in anslist:          
            anslist.append(prod)


for j in range(1234,9877):
    for i in range(2,9):
        prod = i*j
        
        prodlist = [int(a) for a in str(prod)]
        jlist = [int(b) for b in str(j)]
        ilist= [int(c) for c in str(i)]
        if len(prodlist)!=4:
            break
        
        digitcount=[]
        for k in digits:
            count=0
            if k in ilist:
                count+=1
            if k in jlist:
                count+=1
            if k in prodlist:
                count+=1
            digitcount.append(count)
        if digitcount==[1,1,1,1,1,1,1,1,1] and prod not in anslist:          
            anslist.append(prod)
print(sum(anslist))

end=time.time()
print(f"Time taken: {end-start}")
