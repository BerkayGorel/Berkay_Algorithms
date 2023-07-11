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


        ##  İSTENEN KELİMENİN HARFLERİNİ SONDAN YAZDIRMA 
z = input("Kelimeyi giriniz ")
print(z)
for n in range(len(z)+1):
    print(z[:(-n-1)])
    


    
