def arithmetic(arv1:int,arv2:int,sümbol:str) -> int:
    if sümbol=="+":
        s=arv1+arv2
    elif sümbol=="-":
        s=arv1-arv2
    elif sümbol=="*":
        s=arv1*arv2
    elif sümbol=="/":
        s=arv1/arv2
    else:
        s="Неизвестная операция"
    return s

def isYearLeap(aasta: int)->bool:
    """Funktsioon otsustab kas aasta on liigaasta või ei ole.
    Tagastab True kui aasta on liigaasta ja false kui on tavaline aasta.

    parem int aasta: Aasta sissestab kasutaja
    type: bool
    """
    if aasta%4==0 and aasta%100!=0:
        return True
    else:
        return False 

from math import *
def square(külg:float)->any:
    """
    """
    S=külg**2
    P=4*külg
    d=külg*sqrt(2)
    return S,P,d

from math imprt *
def season(a:int)->str:
    """
    """
    while True:
        if a>0 and a<13:
            break
        else:
            try:
                a=int(input("Ainult 1-12, Sisesta veel kord number: "))
            except:
                print("Vigaandmetüübiga")
    if a>2 and a<6:
        s="kevad"
    elif a>5 and a<9:
        s="suvi"
    elif a>8 and a<12:
        s="kevad"
    else:
        s="talv"
return s
