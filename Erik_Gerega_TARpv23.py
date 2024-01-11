#1
#print("Tere maailm")
#nimi=input("Mis on sinu nimi?")
#vanus=int(intup("kui vana sa oled"))
#("Tere tulemast "+nimi)
#print("Tere tulemast ",nimi)," Sa oled" ,vanus, "aasta vana)"
#print("Tere tulemast {0}. sa oled {1} aastat vana".format(nimi,vanus))
#print("muutuja vanus=" ,vanus ,"tüüp on",type(vanus))
#2
#vanus = 18
#eesnimi = "Jaak"
#pikkus = 16.5
#kas_käib_koolis = True
#print("muutuja eesnimi=" ,eesnimi ,"tüüp on",type(eesnimi))
#print("muutuja pikkus=" ,pikkus ,"tüüp on",type(pikkus))
#print("muutuja kas_käib_koolis=" ,kas_käib_koolis ,"tüüp on",type(kas_käib_koolis))
#print("muutuja pikkus=" ,pikkus ,"tüüp on",type(pikkus))
#3
from random import *
#konfeti=randint(10,100)
#print("konfeti",konfeti)
#ukral=int(input("skolko ukrast"))
#konfeti-=ukral
#print("na stole teper",konfeti,"konfet")
#print()

try:
    aeg = float(input("mittu tundi kulus söiduks? ")) #aeg ei sa olla 0
    teepikkus = float(input("mittu kilomeetri söitsid?"))
    kiirus = teepikkus/aeg 
    print("sinu kiirus oli " + str(kiirus) + " km/h")
except:
    print("viga bljat")


