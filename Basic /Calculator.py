            ####    HESAP MAKİNESİ 
a = float(input("Bir sayı değeri giriniz "))
b = float(input("Bir sayı değeri giriniz "))

toplam = a + b
fark = a - b
if fark < 0 :
    fark = b - a 
çarpım = a * b 
oran = a / b 
aüsb = a ** b
büsa = b ** a 
aderkökb = b ** (1/a)
bderköka = a ** (1/b)
loga_b = bderköka
logb_a = aderkökb
anın_yüzde_bsi = a * b / 100 
bnin_yüzde_ası = anın_yüzde_bsi
print("toplam = {}".format(toplam))
print("farklarının mutlak değeri = {}".format(fark))
print("çarpım ={}".format(çarpım))
print("İlk sayının ikinciye oranı  = {}".format(oran))
print("a üssü b = {}".format(aüsb))
print("b üssü a = {}".format(büsa))
print("a. dereceden b = {}".format(aderkökb))
print("b. dereceden kök a = {}".format(bderköka))
print("log a tabanında b  = {}".format(loga_b))
print("log b tabanında a = {}".format(logb_a))
print("a'nın % b'si = {}".format(anın_yüzde_bsi))
print("b'nin % a'sı = {}".format(bnin_yüzde_ası))
