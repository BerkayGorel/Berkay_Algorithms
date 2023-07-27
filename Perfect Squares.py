                                            ###     PRINTING PERFECT SQUARE NUMBERS IN A RANGE

num1 = int(input("Type the first number "))
num2 = int(input("Type the second number "))
nullList = []
for i in range(num1,num2+1):
    sqrt = int(i**0.5)
    if sqrt*sqrt == i:
        nullList.append(i)
print(nullList)



                            
