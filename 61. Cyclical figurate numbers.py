import time
start= time.time()

triangles = [1]
diff = 2
while triangles[-1]<10000:
    triangles.append(triangles[-1]+diff)
    diff+=1
trilist = [x for x in triangles if 999<x<10000 and str(x)[2]!="0"]
tridict = {}
for x in trilist:
    if int(str(x)[:2]) in tridict:
        tridict[int(str(x)[:2])].append(int(str(x)[2:]))
    else:
        tridict[int(str(x)[:2])] = [int(str(x)[2:])]



squlist = [i**2 for i in range(32,100) if str(i**2)[2]!="0"]
squdict = {}
for x in squlist:
    if int(str(x)[:2]) in squdict:
        squdict[int(str(x)[:2])].append(int(str(x)[2:]))
    else:
        squdict[int(str(x)[:2])] = [int(str(x)[2:])]




pentagons = [1]
diff = 4
while pentagons[-1]<10000:
    pentagons.append(pentagons[-1]+diff)
    diff+=3
penlist = [x for x in pentagons if 999<x<10000 and str(x)[2]!="0"]

pendict = {}
for x in penlist:
    if int(str(x)[:2]) in pendict:
        pendict[int(str(x)[:2])].append(int(str(x)[2:]))
    else:
        pendict[int(str(x)[:2])] = [int(str(x)[2:])]





hexagons = [1]
diff = 5
while hexagons[-1]<10000:
    hexagons.append(hexagons[-1]+diff)
    diff+=4
hexlist = [x for x in hexagons if 999<x<10000 and str(x)[2]!="0"]

hexdict = {}
for x in hexlist:
    if int(str(x)[:2]) in hexdict:
        hexdict[int(str(x)[:2])].append(int(str(x)[2:]))
    else:
        hexdict[int(str(x)[:2])] = [int(str(x)[2:])]





heptagons = [1]
diff = 6
while heptagons[-1]<10000:
    heptagons.append(heptagons[-1]+diff)
    diff+=5
heplist = [x for x in heptagons if 999<x<10000 and str(x)[2]!="0"]

hepdict = {}
for x in heplist:
    if int(str(x)[:2]) in hepdict:
        hepdict[int(str(x)[:2])].append(int(str(x)[2:]))
    else:
        hepdict[int(str(x)[:2])] = [int(str(x)[2:])]




octagons = [1]
diff = 7
while octagons[-1]<10000:
    octagons.append(octagons[-1]+diff)
    diff+=6
octlist = [x for x in octagons if 999<x<10000 and str(x)[2]!="0"]


octdict = {}
for x in octlist:
    if int(str(x)[:2]) in octdict:
        octdict[int(str(x)[:2])].append(int(str(x)[2:]))
    else:
        octdict[int(str(x)[:2])] = [int(str(x)[2:])]


def search(n,m): #n is the value to find, m is a list of group numbers to avoid
    alllist = []
    for firsttwo in tridict:
        if 3 in m:
            break
        if n in tridict[firsttwo]:
            alllist.append(["3",firsttwo,n])
    for firsttwo in squdict:
        if 4 in m:
            break
        if n in squdict[firsttwo]:
            alllist.append(["4",firsttwo,n])
    for firsttwo in pendict:
        if 5 in m:
            break
        if n in pendict[firsttwo]:
            alllist.append(["5",firsttwo,n])
    for firsttwo in hexdict:
        if 6 in m:
            break
        if n in hexdict[firsttwo]:
            alllist.append(["6",firsttwo,n])
    for firsttwo in hepdict:
        if 7 in m:
            break
        if n in hepdict[firsttwo]:
            alllist.append(["7",firsttwo,n])
    for firsttwo in octdict:
        if 8 in m:
            break
        if n in octdict[firsttwo]:
            alllist.append(["8",firsttwo,n])
    return alllist


for i in octdict:
    avoidlist = [8]
    firstlist = search(i,avoidlist)
    if firstlist==[]:
        continue
    #print(firstlist)
    for j in firstlist:
        avoidlist2 = avoidlist + [int(j[0])]
        secondlist = search(j[1],avoidlist2)
        if secondlist==[]:
            continue
        #print(secondlist)
        for k in secondlist:
            avoidlist3 = avoidlist2 + [int(k[0])]
            thirdlist = search(k[1],avoidlist3)
            if thirdlist ==[]:
                continue
            #print(thirdlist)
            for l in thirdlist:
                avoidlist4 = avoidlist3 + [int(l[0])]
                fourthlist = search(l[1],avoidlist4)
                if fourthlist ==[]:
                    continue
                #print(fourthlist)
                for m in fourthlist:
                    avoidlist5 = avoidlist4 + [int(m[0])]
                    fifthlist = search(m[1],avoidlist5)
                    if fifthlist ==[]:
                        continue
                    #print(fifthlist)
                    for n in fifthlist:
                        if n[1] in octdict[i]:
                            inum = int(str(i)+str(n[1]))
                            jnum = int(str(j[1])+str(j[2]))
                            knum = int(str(k[1])+str(k[2]))
                            lnum = int(str(l[1])+str(l[2]))
                            mnum = int(str(m[1])+str(m[2]))                            
                            nnum = int(str(n[1])+str(n[2]))
                            print(inum, jnum, knum, lnum, mnum, nnum)
                            print(inum+ jnum+ knum+ lnum+ mnum+ nnum)
    

    

print(f"Time taken: {time.time()-start}")
