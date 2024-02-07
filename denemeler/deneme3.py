f = open("deneme3.txt")
# print(f.readlines())


for a in f.readlines():
    print(a)


f.close()

#-----------
f = open("deneme3.txt","a",encoding="utf-8")
f.write("\nNew Line")
f.close()