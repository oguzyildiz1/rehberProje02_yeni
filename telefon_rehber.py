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
            with open("telefon_rehberi2.txt","r",encoding="utf-8") as dosya:
                text = dosya.read()

            text_stripped = text.rstrip(")") # stripped

            with open("telefon_rehberi2.txt","w",encoding="utf-8") as dosya:
                dosya.write(text_stripped + girdi) #ekleme burada oluyor
        else: #dosya yoksa
            ilk_girdi = {"adi" : adi, "num" : numara}
            ilk_girdi = str(ilk_girdi)
            ilk_girdi = "(" + ilk_girdi + ")"

            with open("telefon_rehberi2.txt","w",encoding="utf-8") as dosya:
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
        f = open("telefon_rehberi2.txt","r",encoding="utf-8")
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
    with open("telefon_rehberi2.txt","r",encoding="utf-8") as dosya:
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


#deneme
def duzelt():
    with open("./telefon_rehberi2.txt","r",encoding="utf-8") as dosya:
        okunan_tum = dosya.read()

    oku_eval = ast.literal_eval(okunan_tum)

    #aranacak ad
    aranan_isim = input("Düzeltilecek isim: ")
    isim_bulundu = False

    print(type(oku_eval), oku_eval)

    try:
    #----  isim arama
        for i in oku_eval:

            if i["adi"] == aranan_isim:
                print(f"{aranan_isim} :", i["num"],"\n") #isim bulundu
                yeni_numara = input("Yeni numara :")
                i["num"] = yeni_numara
                print(f"{aranan_isim} :", i["num"],"\n")
                isim_bulundu = True

                break
            # if oku_eval["adi"] == aranan_isim:

            #     oku_eval["num"] = yeni_numara

            #     print(f"{aranan_isim} :", oku_eval["num"],"\n")
            #     

            #bu isime ait numura düzeltmek

        if isim_bulundu == False: #isim bulnamadıysa
            print("Aranılan isim bulunamadı.")
            
    except:
        print("Kod hatası..")

    print(oku_eval)
    print(type(oku_eval))

    #cevir is the variable for tuple
    #isim bulundu

    # ----- isime ait numarayı değiştirme...
    # dosya = open("telefon_rehberi1.txt","w",encoding="utf-8")

    # cevir_str = str(cevir)
    # dosya.write(cevir_str)
    # dosya.close()


#rehbere kaydet


trmenu()
