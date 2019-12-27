import time
start= time.time()
#1 digit: 9 x (1,2,3,4,5) = 918273645
allconcatlist = [918273645]

#2 digit: ?? x (1,2,3,4) = ?? ?? ?? ???
for i in range(25, 34):
    concat=""
    for j in range(1,5):
        concat+=str(i*j)
    concatlist = [int(i) for i in concat]
    concatlist.sort()
    if concatlist == [1,2,3,4,5,6,7,8,9]:
        allconcatlist.append(int(concat))
        
#3 digit: ??? x (1,2,3) = ??? ??? ???
for i in range(100,334):
    concat=""
    for j in range(1,4):
        concat+=str(i*j)
    concatlist = [int(i) for i in concat]
    concatlist.sort()
    if concatlist == [1,2,3,4,5,6,7,8,9]:
        allconcatlist.append(int(concat))
        
#4 digit: ???? x (1,2) = ???? ?????
for i in range(5000,10000):
    concat=""
    for j in range(1,3):
        concat+=str(i*j)
    concatlist = [int(i) for i in concat]
    concatlist.sort()
    if concatlist == [1,2,3,4,5,6,7,8,9]:
        allconcatlist.append(int(concat))
        
print(max(allconcatlist))
print(f"Time taken: {time.time()-start}")

