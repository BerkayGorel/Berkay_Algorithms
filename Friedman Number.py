while True:
                                                                                    ### FRIEND NUMBERS
        ## If sum of two numbers' factors (except themselves) are equal to each other, they are defined "Friend Numbers"

    num1= int(input("Type the first positive integer number "))
    num2= int(input("Type the second positive integer number "))
    list1 = [ ]
    list2 = [ ]
# Firstly, I'll entype the factors of these numbers

    for item in range (1,num1):
        if num1 % item == 0 :
            list1.append(item)

    for element in range (1,num2):
        if num2 % element == 0 :
            list2.append(element)

    addition1=0
    for new_item in list1:
        addition1 = addition1 + new_item
    print(addition1)

    addition2=0
    for new_elements in list2:
        addition2 = addition2 + new_elements
    print(addition2)

    if addition1 == num2 and addition2 == num1 :
        print("They are friend numbers")
    else:
        print("They are NOT friend numbers")
    print("------------------")






