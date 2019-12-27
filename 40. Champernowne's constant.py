constant=""
number=1
while len(str(constant))<1000000:
    constant+=str(number)
    number+=1
product = int(constant[0])*int(constant[9])*int(constant[99])*int(constant[999])*int(constant[9999])*int(constant[99999])*int(constant[999999])
print(product)
