import ast

adi = ({'adi': 'Oğuzhan Yıldız', 'num': '5323041805'}, {'adi': 'Ferhan Yıldız', 'num': '5369874512'}, {'adi': 'Gökhan Yılmaz', 'num': '5369874512'}, {'adi': 'Yağmur Atay', 'num': '5325647887'}, {'adi': 'Kazım Kara', 'num': '5336095658'})

print(type(adi))
adi = str(adi)
print(adi)
print(type(adi))

dosya1 = open("deneme.txt","w",encoding="utf-8")
dosya1.write(adi)
dosya1.close()

with open("deneme.txt","r",encoding="utf-8") as dosya:
    okunan = dosya.read()
    print(okunan)


xxx = ast.literal_eval(okunan)

print(type(xxx))

for i in xxx:
    print(i)