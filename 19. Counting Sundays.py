
jan = 31
feb = 28
mar = 31
apr = 30
may = 31
jun = 30
jul = 31
aug = 31
sep = 30
oct = 31
nov = 30
dec = 31


#1 jan 1901 is 2
day = 2
countsun=0
# 1 feb 1901 is 2+31%7 = 5
for i in range(1,101):
    #print("Year 190"+str(i))
    if i%4==0:
        feb=29
    else:
        feb=28
    monthlist = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
    for month in monthlist:
        #print(day%7)
        day+=month
        if day%7==0:
            countsun+=1
            
print(countsun)
    
