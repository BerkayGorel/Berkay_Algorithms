                        ###     DIVISORS

        ### FOR LOOP
num = int(input("Type a natural number "))
nullList=[]
divisors=""
for i in range(1,num+1):
    if num % i == 0 :
        nullList.append(i)
print("Divisors of",num,":",nullList)


        ### WHILE LOOP
num = int(input("Type a positive natural number "))
i = 1 
nullList=[]
while i <= num:
    if num % i == 0 :
        nullList.append(i)
    i+=1
print(nullList)
