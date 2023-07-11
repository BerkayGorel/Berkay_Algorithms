

                        ####      TAKSİ ÜCRET TARİFESİ

        # AÇILIŞ ÜCRETİ = 10 TL , İLK 5KM İÇİN KM BAŞINA 6TL ; DAHA SONRAKİ HER KMDE 4,8TL

first = 10

km = float(input("Alınan yolu kilometre cinsinden giriniz"))

if km < 5.0 :
        price = round((first + 6 * km) , 3)
        print(price)

else :
        price = round((first + 5*6  + (km-5)*4.8) , 3)
        print(price)

        

