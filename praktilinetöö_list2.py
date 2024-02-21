1

from string import *

vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
konsonanti="qwrtplkjhgfdszxcvbnm"
markid=punctuation
v=k=m=t=0

tekst=(input("vvedite predlozenie\n")).lower()
tekst_list=list(tekst)
for sümvol in tekst_list:
    if sümvol in vokaali:
        v+=1
    elif sümvol in konsonanti:
        k+=1
    elif sümvol in markid:
        m+=1
    else:
        t+=1
print("Vokaali:",v,"\nKonstanti: ",k)
print("Kirjuvahemärgid: ",m,)
print("Tühikud: ",t)


2

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
#2.3
vanused=[]
for i in range(5):
    vanus=int(input("SIsesta vanus: "))
    vanused.append(vanus) #
maksimum=max(vanused)
minimum=min(vanused)
summa=sum(vanused)
keskmine=summa/len(vanused)
#kuva ekraanile nimi koos vanusega
for i in range(5):
    print(nimed[i],"on", vanused[i],"aastad vana")

3

from random import *
arvud=[]
N=int(input("Mitu rida joonistame? "))
S=input("Sisesta sümbol: ")
#loengi täitmine
for p in range(N):
    arvud.append(randint(1,100))
#diagrammi loomine
for p in range(N):
    print(arvud[p]*S)

4

indeKSid=["Tallin","Narva","Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa","Lääne-Virumaa","Jõgevamaa","Tartu linn","Tartumaa","Põlvamaa","Võrumaa","Valgamaa","Viljandimaa","Järvamaa","Harjumaa","Raplamaa","Pärnumaa","Läänemaa","Hiiumaa","Saaremaa"]
while True:
    while True:
        try:
            indeks=int(input("Sisesta viienumbriline indeks: "))
            if 10000<=indeks<=99999:
                print("55numbriline indeks ")
                break
            else:
                print("On vaja 5numbriline indeks")
        except:
            print("Vale andmetüpp!")
    arv1=indeks//10000
    print(arv1)
    if 1<=arv1<=3:
        print("Istu kodus!")
    else:
        print("MASKI NOSI")
    print(f"Sa elad pirkonnas ")

5
from random import *
from string import *

rida=[]
N=randint(2,25)
for i in range(N):
    rida.append(choice(ascii_uppercase))
print(rida)
kogus=int(input("Mittu elemendi vahemate oma vahel? "))
if len(rida)//2>=kogus:
    for i in range(kogus):
        a=rida[i]
        rida[i]=rida[len(rida)-i-1]
        rida[len(rida)-1-i]=a
    print(rida)



from random import *
from string import *
numbers = imput("vvedite chisla cherez probel: ").split()
numbers = list(map(int, numbers))
if not numbers:
    print("Oshibka: spisok chisel pust.")
else:
    max_number = max(numbers)
numbers[numbers.index]




6
from random import *
nimekirja1=[]
nimekirja=[]
n=int(input("Nimekirja suurus: "))
for i in range(n):
    arv=randint(10,100)
    nimkeirja1.append(arv)
    nimekirja.append(arv)
mmaksimum=nimekirja[0]
for arv in nimekirja:
    if arv>maksimum:
        maksimum=arv
        vajavarv=maksimum/len(nimekirja)
for i in range(len(nimekirja)):
    if nimekirja[i]==maksimum:
        nimekirja[i]=vajavarv
print(nimekirja1)
print(nimekirja)

7
from audioop import reverse
from random import *
from tkinter import TRUE

bebe2=[]
bebe=[]
for i in range(10):
    arv=randint(-100,100)
    bebe.append(arv)
print(bebe)
for arv in bebe:
    if arv<0:
        arv*= -1
        bebe2.append(arv)
    else:
        bebe2.append(arv)
bebe2.sort(reverse=TRUE)
print(bebe2)

12
from random import *

bebe=[]
for i in range(10):
    arv=randint(1,100)
    bebe.append(arv)
print("Def spisok - ",bebe)
max_bebe=max(bebe)
min_bebe=min(bebe)
print("maximalnoe chislo - ",max_bebe)
print("minimalnoe chislo - ",min_bebe)
maxbebe=max_bebe
minbebe=min_bebe
maxindex=bebe.index(max_bebe)
minindex=bebe.index(min_bebe)
print(maxindex, minindex)
del bebe[maxindex]
bebe.insert(maxindex,minbebe)
del bebe[minindex]
bebe.insert(minindex,maxbebe)
print(bebe)

9
from string import *
vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
konsonanti="qwrtplkjhgfdszxcvbnm"
v=k=0

name=input("Vedite name ")
print("privet ",name.capitalize())
kolichestvo=len(name)
print("Kolichstvo bukv v vashem imeni:", kolichestvo)
name_list=list(name)
for sümvol in name_list:
    if sümvol in vokaali:
        v+=1
    elif sümvol in konsonanti:
        k+=1
print("Glasnie:",v,"\nSoglasnie: ",k)
name_list.sort()
print("Bukvi v alphavitnom porjadke",name_list)

9999
from string import *
a=0
b=0

stolitsi=['Париж', 'Берлин', 'Лондон', 'Рим', 'Мадрид', 'Амстердам', 'Варшава', 'Стокгольм', 'Афины', 'Прага']
sort_stolitsi=stolitsi.sort()
for i in stolitsi:
    a+=1
    print(a,i)

new_stolitsa1 = input("Vvedite novuju stolitsu: ")
new_stolitsa2 = input("Vvedite novuju stolitsu: ")
stolitsi.extend([new_stolitsa1, new_stolitsa2])
sort_stolitsi=stolitsi.sort()
for i in stolitsi:
    b+=1
    print(b,i)

