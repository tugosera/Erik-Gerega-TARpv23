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
        tulemus="siis ma ostan pilet tasuta"
    elif 6<=age>14:
        tulemus="siis ma ostan laste pilet"
    elif 15<=age>65:
        tulemus="siis ma ostan täispilet"
    elif 66<=age>100:
        tulemus="siis ma ostan sooduspilet"
    print(tulemus)
else:
    print("me ei lähe kinnos")


    


