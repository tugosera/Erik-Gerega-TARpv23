


from audioop import reverse
from random import *

nimed=["Mati","Meelis","Kati","Mati"]
while True:
    print("*****************")
    v=input("N-näita andmed\nL-lisada andmeid?\nK-andmete kustutamine\nI-positsiooni otsing?n")
    if v=="N":
        v==input("Kas juhuslik(j) või terve loetelu(t)")
        if v=="t":
            print(nimed)
        elif V=="j":
            print(choise(nimed))
    elif v=="L":
        v=input("Kas nimekirja lõppu(l) või positsioonile(P)")
        if v=="l":
            nimi=input("Sisesta nimi: ")
            nimrd.append(nimi)
        elif v=="P":
            nimi=input("Sisesta nimi: ")
            ind=int(input("Mis kohale: "))
            nimed.insert(ind-1,nimi)
    elif V=="K":
        v=input("Kas nimi järgi(n) või indeksi jargi(i) või kõik nimed(k)")
        if V=="i":
            ind=int(input("Sisesta indeks: "))
            nimed.pop(ind-1)
        elif V=="k":
            nimed.clear()
        elif v=="n":
            nimi=input("Sisesta nimi: ")
            mittu=nimed.count(nimi)
            if mitu>0:
                if mitu>1:
                    ind=0
                    indlist=[]
                    sob=0
                    for e in nimed:
                        ind += 1
                        if e == nimi:
                            indlist.append(ind)
                    print(indlist)
                    v = int(input("Mis indeks"))
                    nimed.pop(v)
                else:
                    nimed.remuve(nimi)
            else:
                print(f"{nimi} ei ole loetelus")
            print(spc, nimed, end=spc)
    elif v=="H":
        v=input("sorteerimine(s), kopeerimine(k) või ümber pööramine(p)")
        if v=="s":
            v=int(input("A-z?(1) või Z-a?(2)"))
            if V==1:
                nimed.sort()
            elif v==2:
                nimed.sort(reverse=True)
        elif v=="k":
            nimed.copy()
        elif v=="p":
            nimed.reverse()
    elif v=="I":
        nimi=input("Sissesta nimi: ")
        mitu=nimed.count(nimi)
        if mitu>0:
            print(f"Seal on{mitu} {nimi}")
            for i in range(mitu):
                print(f"{nimi} on {i+1} positsioonil")
        else

            nimed.reverse()


