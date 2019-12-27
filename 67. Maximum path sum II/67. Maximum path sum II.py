from time import time
start = time()

f=open("p067_triangle.txt","r")
message = f.read()
msglist = message.split("\n")
rowlist = [x.split(" ") for x in msglist]

for rowindex in range(len(rowlist)-1,0,-1):
    for eleindex in range(len(rowlist[rowindex])-1):
        rowlist[rowindex-1][eleindex]=str(int(rowlist[rowindex-1][eleindex])+max(int(rowlist[rowindex][eleindex]),int(rowlist[rowindex][eleindex+1])))
print(rowlist[0][0])
            
print(f"Time taken: {time()-start}")
