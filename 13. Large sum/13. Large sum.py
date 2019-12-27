f=open('13. Large numbers.txt','r')
message=f.read()
numlist=message.split("\n")
print(sum(int(i) for i in numlist))
