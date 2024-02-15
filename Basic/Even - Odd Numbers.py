    ##   TEK ve ÇİFT SAYILAR

x = int(input("Bir tam sayı giriniz "))
bosListe1= []
bosListe2= []

if x >= 0 :
    for i in range(1,x+1,2):
        bosListe1.append(i)
    print("Tek Sayılar:",bosListe1)
    
    for i in range(0,x+1,2):
        bosListe2.append(i)
    print("Çift Sayılar:",bosListe2)
    
else:
    for i in range(x+1,0,2):
        bosListe1.append(i)
    print("Tek Sayılar:",bosListe1)

    for i in range(x+1,1,2):
        bosListe2.append(i)
    print("Çift Sayılar:",bosListe2)
    



