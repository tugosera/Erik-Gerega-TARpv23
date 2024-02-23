from MyModul import * #Summa as s
#b=int(input("Sisesta arv2 "))
#summa_3=Summa(3,b,int(input("Kolmas arv: ")))
#summa_31=Summa(100,100)

#print(summa_3)
#print(summa_31)

a=int(input("Sisesta arv1 "))
b=int(input("Sisesta arv2 "))
c=(input("Sisesta sümbol "))
bubu=arithmetic(a,b,c)
print(bubu)

#from modul import *

#while True:
#    try:
#        aasta=int(input("Sisesta aastanumber: "))
#        break
#    except:
#        print("viga")
#a=isYearLeap(aasta)
#print(a)

#from modul import *

while True:
    try:
        a=int(input("Sisesta külg: "))
        break
    except:
        print("viga")
S,P,d=square(a)
print(f"S={S}, P={P}, d={d}")

#from modul import *

while True:
    try:
        kuu=int(input("Kuu number: "))
        break
    except:
        print("Viga")
a=season(kuu)
print(a)