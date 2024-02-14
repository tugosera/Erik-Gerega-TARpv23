#1

#from string import *

#vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
#konsonanti="qwrtplkjhgfdszxcvbnm"
#markid=punctuation
#v=k=m=t=0

#tekst=(input("vvedite predlozenie\n")).lower()
#tekst_list=list(tekst)
#for sümvol in tekst_list:
#    if sümvol in vokaali:
#        v+=1
#    elif sümvol in konsonanti:
#        k+=1
#    elif sümvol in markid:
#        m+=1
#    else:
#        t+=1
#print("Vokaali:",v,"\nKonstanti: ",k)
#print("Kirjuvahemärgid: ",m,)
#print("Tühikud: ",t)


#2

#nimed=[]
#for i in range(5):
#    nimi=input("Sisesta nimi: ").capitalize()
#    nimed.append(nimi)

#print("loetelu oli: ",nimed)
#nimed.sort()
#print("Loetelu sorteeritud: ",nimed)
#for n in range(len(nimed)):
#    print(n+1,".",nimed[n],sep="")
#print("Viimasena oli lisatud: ",nimi)

#uued_nimed=[]
#for nimi in nimed:
#    if nimi not in uued_nimed:
#        uued_nimed.append(nimi)
#print(uued_nimed)

#uued_nimed=list(set(nimed))
##2.3
#vanused=[]
#for i in range(5):
#    vanus=int(input("SIsesta vanus: "))
#    vanused.append(vanus) #
#maksimum=max(vanused)
#minimum=min(vanused)
#summa=sum(vanused)
#keskmine=summa/len(vanused)
##kuva ekraanile nimi koos vanusega
#for i in range(5):
#    print(nimed[i],"on", vanused[i],"aastad vana")

#3

#from random import *
#arvud=[]
#N=int(input("Mitu rida joonistame? "))
#S=input("Sisesta sümbol: ")
##loengi täitmine
#for p in range(N):
#    arvud.append(randint(1,100))
##diagrammi loomine
#for p in range(N):
#    print(arvud[p]*S)

#4

#indeKSid=["Tallin","Narva","Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa","Lääne-Virumaa","Jõgevamaa","Tartu linn","Tartumaa","Põlvamaa","Võrumaa","Valgamaa","Viljandimaa","Järvamaa","Harjumaa","Raplamaa","Pärnumaa","Läänemaa","Hiiumaa","Saaremaa"]
#while True:
#    while True:
#        try:
#            indeks=int(input("Sisesta viienumbriline indeks: "))
#            if 10000<=indeks<=99999:
#                print("55numbriline indeks ")
#                break
#            else:
#                print("On vaja 5numbriline indeks")
#        except:
#            print("Vale andmetüpp!")
#    arv1=indeks//10000
#    print(arv1)
#    if 1<=arv1<=3:
#        print("Istu kodus!")
#    else:
#        print("MASKI NOSI")
#    print(f"Sa elad pirkonnas {}")

#5
#from random import *
#from string import *

#rida=[]
#N=randint(2,25)
#for i in range(N):
#    rida.append(choice(ascii_uppercase))
#print(rida)
#kogus=int(input("Mittu elemendi vahemate oma vahel? "))
#if len(rida)//2>=kogus:
#    for i in range(kogus):
#        a=rida[i]
#        rida[i]=rida[len(rida)-i-1]
#        rida[len(rida)-1-i]=a
#    print(rida)


#6



