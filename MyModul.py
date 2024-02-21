def Summa(arv1:int,arv2:int,arv3=0)->int:
    """  Funktsioon tagastab kolme asrvu summa
         Summa(arv1,arv2,arv3)


    param int arv1: arv1 sisestab kasutaja
    param int arv2: arv2 sisestab kasutaja
    param int arv3: arv3 sisestab kasutaja

    """

    s=arv1+arv2+arv3
    return s

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





