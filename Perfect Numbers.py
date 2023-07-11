
                                                                                         ####  PERFECT NUMBERS

        ## Perfect Numbers
# Firstly, I'd better create the algorithm of factors 
while True:
    num = int(input("Type a positive integer "))
    fac_list = [ ]
    for i in range(1,num):
        if num % i == 0 :
            fac_list.append(i)

# Then I question the sum of them (except number) are equal to the number or are not
    add = 0 
    for item in fac_list :
        add = add+item
    
    print("summation of factors except",num, "= ",add)
    if add == num :
        print("Your number is defined 'perfect number' ")

    else:
        print("Your number is NOT a 'perfect number' ")
    


    





