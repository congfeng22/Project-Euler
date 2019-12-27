import time
start=time.time()

f=open("p059_cipher.txt","r")
message = f.read()
msglist = message.split(",")
intmsglist = [ int(x) for x in msglist ]
properlist2 = [32,33,44,46]+[i for i in range(48,58)]+[i for i in range(65,91)]+[i for i in range(97,123)]
properlist = [i for i in range(32,127)]
#space, exclamation,comma,period + digits + capitals + lowercase

sumchar = 0

for i in range(97,123):
    done = False
    for j in range(97,123):
        
        for k in range(97,123):
            keylist = [i,j,k]
            decrypted = ""
            fail = False
            for x in range(len(intmsglist)):
                char = keylist[x%3]^intmsglist[x]
                if char in properlist:
                    decrypted+=(chr(char))
                else:
                    fail = True
                    break
                
            if fail==True:
                continue
            if " the " in decrypted:
                print(decrypted)
                for i in decrypted:
                    sumchar+=ord(i)
                done = True
            if done==True:
                break
        if done==True:
            break
    if done==True:
        break
    
print(sumchar)
'''
keylist = [key1,key2,key3]

decrypted = ""
sumchar = 0
for x in range(len(intmsglist)):
    char = keylist[x%3]^intmsglist[x]
    sumchar+=char
    decrypted+=chr(char)
                
print(decrypted)
print(sumchar)
'''
print(f"Time taken: {time.time()-start}")
            
