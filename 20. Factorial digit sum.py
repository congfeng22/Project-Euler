def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

sumdigit=0
for i in str(factorial(100)):
    sumdigit+=int(i)
print(sumdigit)
