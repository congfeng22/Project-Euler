letterdict1 = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
lettercount1=0
for i in range(1,10):
    lettercount1+=letterdict1.get(i)
print(lettercount1)


letterdict2={10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
lettercount2=0
for i in range(10,20):
    lettercount2+=letterdict2.get(i)
print(lettercount2)

letterlist1=[6, 6, 5, 5, 5, 7, 6, 6]
lettercount3=0
for i in range(2,10):
    for j in range(0,10):
        lettercount3+=letterlist1[i-2]
        lettercount3+=letterdict1.get(j)
print(lettercount3)

onetoninetynine = lettercount1+lettercount2+lettercount3

totalsum=onetoninetynine
for i in range(1,10):
    totalsum+=100*(letterdict1.get(i)+10)-3
    totalsum+=onetoninetynine
totalsum+=3+8
print(totalsum)
