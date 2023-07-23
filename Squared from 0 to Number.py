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



        



    
            
    

        

   
    
    


    
