    ##   KULLANICI BİLGİLERİYLE SİTEYE GİRİŞ - 3 HAK VAR

defNick = input("Kullanıcı adınızı belirleyiniz ")
defPassword = input("Şifrenizi belirleyiniz, şifreniz en az 8 karakterden,en az bir büyük harf, rakam ve özel karakterden ( % ! ; : . , ) oluşmalıdır " )
d_Pass = list(defPassword)
special_char = [",",".",":",";","!","%"," "]
integers = ["1","2","3","4","5","6","7","8","9","0"]

    
while   ( len(d_Pass)  < 8 )  or  ( defPassword.islower() == True )    or     ( any(special_char) not in d_Pass == True )  or  ( any(integers) not in d_Pass == True ):
    input("Şifreniz en az 8 karakterden,en az bir büyük harf, rakam ve özel karakterden ( % ! ; : . ,  ) oluşmalıdır ")


nickName = input("Kullanıcı adınızı giriniz ")
passWord =input("Şifrenizi giriniz ")

ent_try = 3

while ( defNick != nickName )  or  (defPassword != passWord ) :
    ent_try -=1
    print("Kullanıcı adı veya parola hatalı kalan giriş hakkınız {} ".format(ent_try))
    input("Kullanıcı adınızı giriniz ")
    input("Şifrenizi giriniz ")
    if ent_try == 0 :
        break 
      
if  (defNick == nickName) and  (defPassword == passWord ) :
    print("Giriş başarılı ")

    
    
