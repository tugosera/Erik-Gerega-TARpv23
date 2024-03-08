from os import *
from gtts import *
def loe_failist(fail:str):
    """

    """
    f=open(fail,'r',encoding="utf-8")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend

def kirjuta_failisse(fail:str):
    """

    """
    n=int(input("Sisesta mitu elemendi: "))
    for i in range(n):
        jarjend.append(input(f"{i+1}. element: "))
    f=open(fail,'w',encoding="utf-8")
    for el in jarjend:
        f.write(el+"\n")
    f.close()

def heli(text:str,keel:str):

    obj=gTTS(text=tekst,lang=keel,slow=False).save("heli.mp3")
    system("heli.mp3")

text=input("Sisesta tekst: ")
heli(tekst,'et')

kirjuta_failisse("Text.txt")

paevat=loe_failist("paevad.txt")
print(paevat)
 