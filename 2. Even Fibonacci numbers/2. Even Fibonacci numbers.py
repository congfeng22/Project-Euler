fibonacci = [1,2]
new = fibonacci[-1]+fibonacci[-2]
even = 2
while new<=4000000:
    fibonacci.append(new)
    if new%2==0:
        even+=new
    new = fibonacci[-1]+fibonacci[-2]
    
print(even)
