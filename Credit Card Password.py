                                                    ###     CREDIT CARD PASSWORD

while True:
    number = int(input("Type the number of people "))

    count = 1

    for i in range(10001 - number):
        count = count * (i+1)
                    ##    print("{0}! = {1}".format(number,count))

    newCount = 1
    for item in range(10001):
        newCount = newCount * (item+1)
                    ##    print("{0}! = {1}".format(number,count))

    func = 1 - (newCount / ( count * 10000**number ))

    print(func)
