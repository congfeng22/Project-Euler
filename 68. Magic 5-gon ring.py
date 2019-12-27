from itertools import combinations, permutations
from time import time
start=time()

digits = [1,2,3,4,5,6,7,8,9]
pentagon = list(combinations(digits,5))
penlist = [list(x) for x in pentagon if sum(x)%5==0]
nodelist = []
anslist = []
for i in penlist:
    nodelist.append([10]+[x for x in digits if x not in i])
for index in range(len(penlist)):
    pennums = penlist[index]
    nodenums = nodelist[index]
    k=sum(pennums)//5
    l=sum(nodenums)//5
    m = 2*k+l
    for i in pennums:
        j = 1+k-i
        if j==i or j not in pennums:
            continue
        remdigits = [x for x in pennums if x!=i and x!=j]
        remlist = [list(x) for x in list(permutations(remdigits,3))]
        for a in remlist:
            remnodes = [10]
            remnodes.append(m-j-a[0])
            remnodes.append(m-a[0]-a[1])
            remnodes.append(m-a[1]-a[2])
            remnodes.append(m-a[2]-i)
            if sorted(remnodes)==sorted(nodenums):
                startnode = min(remnodes)
                thelist = [10,i,j,m-j-a[0],j,a[0],m-a[0]-a[1],a[0],a[1],m-a[1]-a[2],a[1],a[2],m-a[2]-i,a[2],i]
                startindex = thelist.index(startnode)
                ans = thelist[startindex:]+thelist[:startindex]
                #print(ans)
                #print("")
                anslist.append(ans)
print(max(anslist))
            

print(f"Time taken: {time()-start}")
