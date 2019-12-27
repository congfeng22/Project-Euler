import time
start=time.time()

def baseconv(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return baseconv(n//base,base) + convertString[n%base]


counter=0
for i in range(1,1000000,2):
    if str(i)==str(i)[::-1]:
        if str(baseconv(i,2))==str(baseconv(i,2))[::-1]:
            counter+=i
print(counter)


end = time.time()
print(f"Time taken: {end-start}")
