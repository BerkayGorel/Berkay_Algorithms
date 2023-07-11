    ##   TEK ve ÇİFT SAYILAR

x = int(input("Bir tam sayı giriniz "))

bosListe1= []
bosListe2= []

if x >= 0 :
    print("Tek sayılar: ")
    for i in range(1,x+1):
        if i % 2 == 1 :
            bosListe1.append(i)
    print(bosListe1)

    print("Çift sayılar: ")            
    for i in range(1,x+1):
        if i % 2 == 0 :
            bosListe2.append(i)
    print(bosListe2)

if x < 0 :
    print("Tek sayılar: ")
    for i in range(x+1,1):
        if i % 2 == 1 :
            bosListe1.append(i)
    print(bosListe1)

    print("Çift sayılar: ")            
    for i in range(x+1,1):
        if i % 2 == 0 :
            bosListe2.append(i)
    print(bosListe2)
    



