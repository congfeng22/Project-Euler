# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:26:59 2019

@author: Cong Feng
"""
from time import time
import math
start = time()
L = 100
total =0
for i in range(L):
    count=0
    first = 1
    while first<math.ceil(i/(2+math.sqrt(2))):
        #execute counting triples
        for second in range(math.ceil(i/2-first),math.ceil((i-first)/2)):
            third = i - first - second
            if first**2+second**2 == third**2:
                count+=1
        
        if count==2:
            break
        first+=1
    if count==1:
       total+=1
print(total)

print("Time taken: ", time()-start)