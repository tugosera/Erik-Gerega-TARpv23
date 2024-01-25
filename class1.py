#print("Tund on alanud")
#opozdanie=input("Kas õpilane on hilinenud")
#if opozdanie.upper()=="JAH" :
#    print("õpilane ootab 30 minutid")
#print("Õpilane astub klassi")


#from random import *

#arv=randint(0,100) 
#print(arv)
#if arv%2==0:
#    print(arv,"on paaris arv")
#else:
#    print(arv, "on paaritu arv")



#from random import *
#protsent=randint(-100,500) #0-100 0-60-"2" 61-75-"3" 76-89-"4" 90-100-"5"
#print(protsent, "% on testi tulemus")
#if protsent<0 or protsent>100:
#    tulemus="peredelaj"
#elif 0<=protsent<60:
#    tulemus="dva"
#elif 60>=protsent<75:
#    tulemus="tri"
#elif 75>=protsent<90:
#    tulemus="chetire"
#else:
#    tulemus="pjat"
#print(tulemus)

#1

print("Mis on sinu nimi?")
nimi=input()
if nimi.lower()=="juku":
   print("me läheme kinnos")
   print("skolko let?")
   age=int(input())
   if age<0 or age>100:
       tulemus="viga"

   elif age<6:
       tulemus=("siis ma ostan pilet tasuta")

   elif 6<=age>14:
       tulemus=("siis ma ostan laste pilet")

   elif 15<=age>65:
       tulemus=("siis ma ostan täispilet")

   elif 66<=age>100:
       tulemus=("siis ma ostan sooduspilet")

   print(tulemus)
else:
   print("me ei lähe kinnos")

#2

print("mis on teie nimed?")
a=input()
b=input()
print(a, "ja", b, "te olete täna pinginaabrid")

#3

from math import *

print("skolko dlinna syen?")
dlinna1=int(input())
dlinna2=int(input())
S=dlinna2*dlinna1
print("plosad ravna", S)
print("hotite remont? 1=>da 0=>net")
a=int(input())
if a==0:
   print("nu ok")
elif a==1:
   print("skolko 1 kvadratni metr syoit?")
   q=float(input())
   d=S*q     
   print("zamena pola stoit", d)

#4
from math import *

print("milline on alghind?")
a=int(input())
if a>700:
    a*0.30
    print("uus hind = ", a )
else:
    print("hind ei muuda, ja on ", a)

#5

a=int(input("temperatuur praegu on "))
if a>17:
    print("Temperatuur on hea")
else:
    print("temperatuur on liiga väike")

#6

a=int(input("teie pikkus on "))
if a<160:
    print("sina pikkus on väga väike")
elif 161<=a<185:
    print("sinu pikkus on normaalne")
else:
    print("sinu pikkus on väga suur")
    
#7
a=int(input("teie pikkus on "))
b=int(input("kas sina oled pois või tüdruk (pois=1, tüdruk=0)"))
if b==1:
    if a<160:
        print("sina pikkus on väga väike")
    elif 161<=a<185:
        print("sinu pikkus on normaalne")
    else:
        print("sinu pikkus on väga suur")
else:
    if a<150:
        print("sina pikkus on väga väike")
    elif 151<=a<175:
        print("sinu pikkus on normaalne")
    else:
        print("sinu pikkus on väga suur")
 
from datetime import *
from random import *
#8.2

arve_nr= date.today()
print(arve_nr)
tsekk="arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
suma=0
for tode in ["piim","leib","kommid"]:
   hind=randint(50,150)/100
   v=input("toode: "+toode+" Hind: "+str(hind)+"\nKas tahad osta?").lower()
   if v=="jah":
       mittu=int(input("Mittu? "))
       tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
       summa+=mitu*hind
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)
while true:

   raha=float(input("Maksa "+str(summa)))
   if raha==summa:
       print("Tänan ostu eest!")
       break
   elif raha>summa:
       print("Tänan ostu eest! Tagasi "+str(raha-summa))
       break
   else:
       summa-=raha
       print("Maksa veel"+str(summa))




#8.1


from datetime import*
from random import * 

arve_nr = date.today()
print(arve_nr)
tsekk="arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0

toode="Piim"
hind=randint(50,150)/100
v=input("Toode:"+toode+" Hind: "+str(hind)+"\nkas tahad osta?").lower()
if v=="jah":
      mitu=int(input("mitu?"))
      tsekk+=toode+"  "+str(hind)+"  "+str(mitu*hind)+"\n"
      summa+=mitu*hind

toode="Leib"
hind=randint(90,300)/100
v=input("Toode:"+toode+" Hind: "+str(hind)+"\nkas tahad osta?").lower()
if v=="jah":
      mitu=int(input("mitu?"))
      tsekk+=toode+"  "+str(hind)+"  "+str(mitu*hind)+"\n"
      summa+=mitu*hind

toode="Kommid"
hind=randint(600,1500)/100
v=input("Toode:"+toode+" Hind: "+str(hind)+"\nkas tahad osta?").lower()
if v=="jah":
      mitu=int(input("mitu?"))
      tsekk+=toode+"  "+str(hind)+"  "+str(mitu*hind)+"\n"
      summa+=mitu*hind

tsekk+="Kokku maksta: "+str(summa)
print(tsekk)

raha=float(input("maksa"+str(summa)))
if raha==summa:
   print("tänan ostu eest")
elif raha >summa:
   print("Tänan ostu eest! Tagasi "+str(raha-summa))
else:
   print("Maksa veel"+str(summa-raha))

#9

a=int(input("vedite 1 storonu kvadrata "))
b=int(input("vedite 2 storonu kvadrata "))
if a==b:
    print("eto kvadrat")
else:
    print("eto ne kvadrat")

#10

from math import *

a=int(input("vedite chislo 1 "))
b=int(input("vedite chislo 2 "))
c=int(input("kakoe deistvie? (+ = 1, - = 2, / = 3, * = 4)"))
if c==1:
    print(a, " + ", b, " = ", a+b )
elif c==2:
    print(a, " - ", b, " = ", a-b )
elif c==3:
    print(a, " / ", b, " = ", a/b )
elif c==4:
    print(a, " * ", b, " = ", a*b )
else:
    print("oshibka")



#11

ta=date.today().year
sp=date(int(input("Sünniaasta: ")),int(input("Sünnikuu: ")),int(input("Sünnipäev: "))).year
if (ta-sp)%5==0:
   print("Juubel")
else:
   print("tavaline sünnipäev")

#12

from math import *

a=int(input("cena produkta - "))
if a<=10:
    print("novaja cena = ", a*0.9)
elif 0<a>=20:
    print("novaja cena = ", a*0.8)
else:
    print("oshibka")


#13 

a=int(input("sa oled pois(1) või töüdruk(2) "))
if a==1:
    b=int(input("kui palju aastad sulle on? "))
    if 16<=b<=18:
        print("ti prinjat v komandu!")
    else:
        print("ti ne prohodish v komandu")
else:
    print("ti ne prohodish v komandu")

    


#14

maht=int(input("Bussi maht: "))
i=int(input("Inimeste arv: "))
ba=round(i/maht)
if i%maht!=0:
    ba+=1
vb=i%maht
print("Kokku on vaja {0} bussi ja vimasel sõidavad {1} inimest".format(ba,vb))