        ##  İSTENEN KELİMENİN HARFLERİNİ ALT ALTA YAZDIRMA

x = input("Kelimeyi giriniz ")

for i in range(len(x)):
    print(x[i])



        ##  İSTENEN KELİMENİN HARFLERİNİ ALT ALTA ÜÇGENSEL YAZDIRMA
y = input("Kelimeyi giriniz ")

for k in range(len(y)):
    print(y[:k+1])
for m in range(len(y)):
    print(y[:-(m+1)])

        ## KELİMEYİ İKİ KEZ TEKRAR EDECEK ŞEKİLDE YAZDIRMA YÖNTEMLERİNDEN BİRİ
kelime = input("Kelimeyi giriniz: ")

sayac = 0 
basla=len(kelime)
while sayac < len(kelime)+1:
    print(kelime[:sayac])
    count+=1
while basla <= len(kelime)+1:
    print(kelime[:basla])
    basla-=1
    if basla <0 :
        break

        ##  İSTENEN KELİMENİN HARFLERİNİ SONDAN YAZDIRMA 
z = input("Kelimeyi giriniz ")
print(z)
for n in range(len(z)+1):
    print(z[:(-n-1)])
    

        ## 
    
