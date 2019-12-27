seriessum = 0
for i in range(1,1001):
    seriessum+=(i**i)%10000000000
print(seriessum%10000000000)
