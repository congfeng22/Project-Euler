fibonacci = [1,1]
new = fibonacci[-1]+fibonacci[-2]
while len(str(new))<1000:
    new = fibonacci[-1]+fibonacci[-2]
    fibonacci.append(new)
    
print(fibonacci.index(new)+1)
