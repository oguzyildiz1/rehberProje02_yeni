import ast
import os

rehber = ({'adi': 'Oğuzhan Yıldız', 'num': '5323041805'}, {'adi': 'Ferhan Yıldız', 'num': '5369874512'}, {'adi': 'Gökhan Yılmaz', 'num': '5369874512'}, {'adi': 'Yağmur Atay', 'num': '5325647887'})

print(os.listdir())

adi = input("Adı: ")
num = input("Numara: ")

girdi = {"adi" : adi, "numara" : num}

try:
    #aranılan dosya var mı?
    path = "./deneme3.txt"
    check_file = os.path.isfile(path) #true or false

    if check_file: #eğer dosya varsa
        #yeni bir dosya açmayacak, geleni ekleyecek
        #append kullanıcağız
        with open("telefon_rehberi2.txt","r",encoding="utf-8") as dosya:
            oku = dosya.read()
            
        print(oku)

    else:
        #yeni bir dosya oluşturacak.
        with open("deneme3.txt","w",encoding="utf-8") as dosya:
            dosya.write("(")
            dosya.write(f"{girdi}")
            dosya.write(")")

except:
    print("dosya hatası...")
"""
xxx = ast.literal_eval(okunan)

print(type(xxx))

for i in xxx:
    print(i)
"""