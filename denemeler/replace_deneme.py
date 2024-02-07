import ast

dosya = open("./replace.txt","r",encoding="utf-8")

okunan_tum = dosya.read()

dosya.close()

print(okunan_tum)
print(type(okunan_tum))

yeni_dosya = okunan_tum.replace("Oğuzhan", "Orhan")
print(yeni_dosya)

#---- tekrar kayıt

with open("./replace.txt","w",encoding="utf-8") as dosya:
    dosya.write(yeni_dosya)

#---------
    

# ------------- tuple'a değişim
    
with open("./replace_tuple.txt","r",encoding="utf-8") as dosya:
    oku_tum_2 = dosya.read()

print(oku_tum_2)
oku_eval = ast.literal_eval(oku_tum_2)

print(oku_eval)
print(type(oku_eval))

for i in oku_eval: # numarasını değişkende değiştirdik
    print(oku_eval["adi"] , "  hey")
    if oku_eval["adi"] == "Oğuzhan Yıldız":
        oku_eval["num"] = "5326987800"
    # if ["adi"] == "Oğuzhan Yıldız":
    #     i["num"] = "5326987800"
# --- stringe çevirme
        
oku_str = str(oku_eval)
print(oku_str, "  str")

# ------------ doğru formata çevirme
oku_str = "(" + oku_str + ")"


# ------- değişkeni dosyaya yazacağız
with open("./replace_tuple.txt","w",encoding="utf-8") as dosya:
    dosya.write(oku_str)


