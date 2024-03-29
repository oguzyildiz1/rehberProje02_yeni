import os
import time
import ast

# varsayılan dizin'i değiştirme
"""
simdikiDizin = os.getcwd()

try:
    os.chdir(simdikiDizin)
    #os.chdir("C:\\Users\\yildi\\OneDrive\\Desktop\\python\\vektorelBilisim\\github\\rehberProje02\\rehber_proje_02")
except:
    print("Dizin hatası")
"""


def trmenu():
    print("╔" + "═" * 25 + "╗")
    print("║      Telefon Rehberi    ║")
    print("║       1. Kişi ekle      ║")
    print("║       2. Listele        ║")
    print("║       3. Ara            ║")
    print("║       4. Düzelt         ║")
    print("║       5. Çıkar          ║")
    print("║       6. Çıkış          ║")
    print("╠" + "═" * 25 + "╣")
    print("║Seçiminiz: \t\t  ║")
    print("╚" + "═" * 25 + "╝")

    secim = input()
    if secim == "1":
        kullaniciEkle()
        trmenu()
    elif secim == "2":
        listele()
        trmenu()
    elif secim == "3":
        ara()
        trmenu()
    elif secim == "4":
        duzelt()
        trmenu()
    elif secim == "5":
        cikar()
        trmenu()
    elif secim == "6":
        pass



## telefon rehberi
def kullaniciEkle(): ## secim icin ayri fonksiyon kullandım
    print("╔" + "═" * 17 + "╗")
    print("║   Adı, Soyadı:  ║")
    print("╚" + "═" * 17 + "╝")
    adi = input("")

    print("╔" + "═" * 18 + "╗")
    print("║   Tel Numarası:  ║")
    print("╚" + "═" * 18 + "╝")
    numara = input("")

    #--- girdiyi alma -------------

    girdi = {"adi" : adi, "num" : numara}
    girdi = str(girdi)
    girdi = ", " + girdi + ")"
    #print(girdi) #   , {'adi': 'Hazal Kaya', 'num': '5326987845'}
    #---- girdi alma bitti

#------------ numara kontrolu ---------------
    if len(numara) != 10: #10 haneli değilse
        print("Eksik numara girildi")
        print("Tekrar giriniz")
        
        return kullaniciEkle() # fonksiyonu yeniden çağırıyorum
    else:
        girdi = str(girdi)
        #girdi 10 haneli bir numara mı?

#
    #----- girdiyi telefon rehberine ekleme --- 
        
    try:
            #aranılan dosya var mı?
        path = "./telefon_rehberi2.txt"
        check_file = os.path.isfile(path) #true or false

        if check_file: #eğer dosya varsa
        #append kullanıcağız
            with open("./telefon_rehberi2.txt","r",encoding="utf-8") as dosya:
                text = dosya.read()

            text_stripped = text.rstrip(")") # stripped

            with open("./telefon_rehberi2.txt","w",encoding="utf-8") as dosya:
                dosya.write(text_stripped + girdi) #ekleme burada oluyor
        else: #dosya yoksa
            ilk_girdi = {"adi" : adi, "num" : numara}
            ilk_girdi = str(ilk_girdi)
            ilk_girdi = "(" + ilk_girdi + ")"

            with open("./telefon_rehberi2.txt","w",encoding="utf-8") as dosya:
                dosya.write(ilk_girdi)

        #------ eklendi mesajı ------------   
        time.sleep(1)
        print(f"\n{adi}: {numara}")
        print("\nKişi başarıyla eklendi\n")
        time.sleep(1)

    except:
        print("Dosya hatası")
    
# ------------------ listeleme --------------------------------
def listele():
    try:
        f = open("./telefon_rehberi2.txt","r",encoding="utf-8")
        okunan = f.read()
        #okunan = okunan.strip("(")
        cevrilen = ast.literal_eval(okunan) #tuple

        print("Ad Soyad\t","Telefon","\n-----------\t","-----------")

        for a in cevrilen:
            print(f'{a["adi"]}\t',f'{a["num"]}') # adi: Oğuzhan Yıldız Numarası: 11

        f.close()
        print("----------------------------")
        input()

    except:
        print("Bir hata oluştu")

# -------------- arama fonksiyonu--------------
def ara():
    with open("./telefon_rehberi2.txt","r",encoding="utf-8") as dosya:
        okunan = dosya.read()
    print("╔" + "═" * 20 + "╗")
    print("║   Aranacak kişi:   ║")
    print("╚" + "═" * 20 + "╝")

    arananIsim = input("")
    cevrilen = ast.literal_eval(okunan) #tuple

    bulunan = 0

    for a in cevrilen:
        if a["adi"] == arananIsim: #input ile girilen isim ise
            print("\n-----------------")
            print(f'No: {a["num"]}')
            bulunan = 1
            input()
            break
    
    if bulunan == 0:
        print(f"\n{arananIsim} diye bir kayıt bulunamadı")
        input()


#--------- duzeltme fonksiyonu --------- suc
def duzelt():
    #-------------- telefon düzeltme -----------------
        with open("./telefon_rehberi2.txt","r",encoding="utf-8") as dosya:
            okunan_tum = dosya.read()

        oku_eval = ast.literal_eval(okunan_tum)

        #aranacak ad
        aranan_isim = input("Düzeltilecek isim: ")
        isim_bulundu = False

        try:
        #----  isim arama tuple'da
            for i in oku_eval:

                if i["adi"] == aranan_isim:
                    print(f"{aranan_isim} :", i["num"],"\n") #isim bulundu
                    yeni_isim = input("Yeni isim :")
                    yeni_numara = input("Yeni numara :")

                    i["adi"] = yeni_isim
                    i["num"] = yeni_numara
                    
                    time.sleep(1)
                    print(f'\n{i["adi"]} :', i["num"],"\n")
                    isim_bulundu = True

                    break

            if isim_bulundu == False: #isim bulnamadıysa
                print("Aranılan isim bulunamadı.")

        #----- değişen tuple'ı stringe çevirip tekrar kaydetme
            
            elif isim_bulundu == True:
                oku_str = str(oku_eval)

                with open("./telefon_rehberi2.txt","w",encoding="utf-8") as dosya:
                    dosya.write(oku_str)

                time.sleep(1)
                print("Kayıt başarıyla değiştirildi.")

        except:
            print("Kod hatası..")

#------------- kisi cikarma fonksiyonu -----------------

def cikar():
    with open("./telefon_rehberi2.txt","r",encoding="utf-8") as dosya:
            okunan_tum = dosya.read()

    oku_eval = ast.literal_eval(okunan_tum)
    oku_eval_list = list(oku_eval) #silmek için listeye çevirdik

        #aranacak ad
    aranan_isim = input("Silinecek isim: ")
    isim_bulundu = False

    try:
    #----  isim arama tuple'da
        sayac = -1 #index numarasını bulmak istiyoruz
        for i in oku_eval_list:
            sayac += 1

            if i["adi"] == aranan_isim:
                print(f"{aranan_isim} :", i["num"],"\n") #isim bulundu

                #tuple'daki elementi silme
                oku_eval_list.remove(oku_eval_list[sayac])

                time.sleep(1)
                print(f'\n{aranan_isim} silindi.')
                isim_bulundu = True

                break

        if isim_bulundu == False: #isim bulnamadıysa
            print("Aranılan isim bulunamadı.")

    #----- değişen tuple'ı stringe çevirip tekrar kaydetme
    #--------- list'i tuple'a çevit    
        elif isim_bulundu == True:
            oku_eval_tuple = tuple(oku_eval_list)
            oku_str = str(oku_eval_tuple)

            with open("./telefon_rehberi2.txt","w",encoding="utf-8") as dosya:
                dosya.write(oku_str)

            time.sleep(1)
            print("Kayıt başarıyla değiştirildi.")

    except:
        print("Kod hatası..")

trmenu()
