
for a in range(9,0,-1):
    for b in range(9,-1,-1):
        for c in range(9,-1,-1):
            for i in range(10,91):
                if (9091*a+910*b+100*c)%i==0 and (9091*a+910*b+100*c)//i<1000:
                    print(str(11*(9091*a+910*b+100*c))+" = "+str(11*i)+" x "+str((9091*a+910*b+100*c)//i))
                    break
            
        
    break

'''


'''

