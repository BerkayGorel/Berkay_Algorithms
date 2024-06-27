                                        ##  CHECKING THE ENTERED NUMBER WHETHER PRIME OR NOT

number = int(input("Type the number: "))
N = int((number)**(1/2))
isPrime = True

for i in range(2,N+1,2):
    if N % i == 0:
        isPrime = False
        break
    
if isPrime == False:
    print(number,"is not prime")
else:
    print(number,"is prime")
      
        





    
