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

nimed=[]
for i in range(5):
    nimi=input("Sisesta nimi: ").capitalize()
    nimed.append(nimi)

print("loetelu oli: ",nimed)
nimed.sort()
print("Loetelu sorteeritud: ",nimed)
for n in range(len(nimed)):
    print(n+1,".",nimed[n],sep="")
print("Viimasena oli lisatud: ",nimi)

uued_nimed=[]
for nimi in nimed:
    if nimi not in uued_nimed:
        uued_nimed.append(nimi)
print(uued_nimed)

uued_nimed=list(set(nimed))

