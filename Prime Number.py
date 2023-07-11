        ##   SAYININ ASAL OLUP OLMADIĞINI GÖSTEREN ALGORİTMA

count = 1

number = int(input("Bir doğal sayı giriniz "))

while count < number :
    count +=1
    if number % count == 0 :
        print("Sayınız asal DEĞİL")
        break
    else:
        print("Sayınız asal")
        break
    
