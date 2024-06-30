
                                                                                         ####  PERFECT NUMBERS

        ## Perfect Numbers
# Firstly, I'd better create the algorithm of divisors
divisors = []

num = int(input("Type the number: "))

N = int(num**(1/2))
summa = 0
for i in range(1,N+1):
    if num % i == 0:
        divisors.append(int(i))
        divisors.append(int(num/i))
for item in divisors:
    summa+=divisors
if summa == num:
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect number")
    
    
      
        



    





