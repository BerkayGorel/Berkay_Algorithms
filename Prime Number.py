                                        ##  CHECKKING THE ENTERED NUMBER WHETHER PRIME OR NOT

while True:
    count = 1
    
    number = int(input("Bir doğal sayı giriniz "))
    if number % 2 == 0 :
        print("Sayınız asal DEĞİL")
        continue
    
    while count < number:
        count +=2
        if number % count == 0 :
            print("Sayınız asal DEĞİL")
            break
        else:
            print("Sayınız asal")
            break
    
