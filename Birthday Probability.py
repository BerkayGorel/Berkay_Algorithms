                                                                                       ###     BIRTHDAY PARADOX

        # According to the paradox, the probability of two people was born on the same day in a place become at least 23 people is about 50%
while True:
    people = int(input("Type the number of people "))
    number = 366
    count = 1
    for i in range(number):
        count = count * (i+1)
    print("{0}! = {1}".format(number,count))

    newNumber = (366-people)
    newCount = 1
    for item in range(newNumber):
        newCount = newCount * (item+1)
    print("{0}! = {1}".format(newNumber,newCount))    

    func = 1 - (count / (newCount * 366**people))

    print("Probability= ", func)
    

    
