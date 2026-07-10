# İstifadəçidən ədədlərin siyahısını al (məsələn, vergüllə ayrılmış: 12, 45, 7, 23, 9)     
#Bu ədədlər üzərində hesabla (sum(), max(), min(), sorted() kimi funksiyalardan istifadə etmə, hamısını özün for loop ilə yaz)
#İstifadəçi girişini input() ilə al, vergüllə ayır, ədədə çevir

# daxil = input("Ededinizi daxil edin :")
# ayir = daxil.split(" ,")
# sum=0
# for i in ayir:
#     cevir=int(i)
#     sum+=cevir
# print(sum)




# daxil = input("Ededinizi daxil edin :")
# ayir = daxil.split(",")
# boyuk= int(ayir[0])
# for i in ayir:
#     cevir=int(i)
#     if cevir > boyuk:
#         boyuk = cevir 
# print(f"Bu eded boyukdur: {boyuk} ")
   



# daxil = input("Ededinizi daxil edin :")
# ayir = daxil.split(",")
# kicik= int(ayir[0])
# for i in ayir:
#     cevir=int(i)
#     if cevir < kicik:
#         kicik = cevir 
# print(f"Bu eded kicikdir: {kicik} ")



daxil = input("Ededinizi daxil edin :")
spel = daxil.split(",")
cem = 0
for i in spel :
    cevir=int(i)
    cem+=cevir
print(cem)