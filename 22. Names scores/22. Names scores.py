f=open("p022_names.txt","r")
message=f.read()
msglist=message.split(',')
newmsglist = []
for i in msglist:
    newmsglist.append(i[1:-1])

newmsglist.sort()


letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
namescore=0
for i in newmsglist:
    lettercount=0
    for j in i:
        lettercount+=numbers[letters.index(j)]
    namescore+=lettercount*(newmsglist.index(i)+1)
print(namescore)
