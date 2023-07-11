    ## 0'DAN GİRİLEN SAYIYA KADAR KARE YAZDIRMA

x = int(input("Bir sayı giriniz "))

bosListe1= [ ]
if x >= 0 :
    for i in range(0,x+1):
        bosListe1.append(i**2)
    print(bosListe1)

else  :
    for i in range(x,1):
        bosListe1.append(i**2)
    bosListe1.sort()
    print(bosListe1)


    ## 0'DAN GİRİLEN SAYIYA KADAR TAM KARE OLANLARI YAZDIRMA

kucuk = int(input("Küçük sayıyı giriniz "))
buyuk =  int(input("Büçük sayıyı giriniz "))
ksqrt = (kucuk) ** 1/2
var = type(ksqrt)
bosListe=[]
if kucuk < buyuk:
    
    for item in range(kucuk,buyuk+1):
        if var == int :
            bosListe.append(item)
            print(bosListe)
    
        



    
            
    

        

   
    
    


    
