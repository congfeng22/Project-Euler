f = open("18. Maximum path I.txt", "r")
message = f.read()
pathlist = message.split("\n")
newpathlist=[]
for i in pathlist:
    newpathlist.append(i.split(" "))
for i in newpathlist:
    while len(i)<len(newpathlist[-1]):
        i.append("0")
newnewpathlist = []
for n in newpathlist:
    phrow=[]
    for i in n:
        phrow.append(int(i))
    newnewpathlist.append(phrow)
print(newnewpathlist)


        

def maxPathSum(tri, m, n): 
  
    # loop for bottom-up calculation 
    for i in range(m-1, -1, -1): 
        for j in range(i+1): 
  
            # for each element, check both 
            # elements just below the number 
            # and below right to the number 
            # add the maximum of them to it 
            if (tri[i+1][j] > tri[i+1][j+1]): 
                tri[i][j] += tri[i+1][j] 
            else: 
                tri[i][j] += tri[i+1][j+1] 
  
    # return the top element 
    # which stores the maximum sum 
    return tri[0][0]
print(maxPathSum(newnewpathlist, 14, 14))
