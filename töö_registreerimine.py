from modul_registreerimine import *
parol=[1337,228,1488,696969]
user=["Evgenij","TurboKiller","tugosera","Nikita"]

while True:
    print("Vali mida teha\n 0-posmotret vse username/paroli\n 1-log in\n 2-sign in\n 3-change username\n 4-change password\n")

    valik=int(input())
    if valik==0:
        vivod_dannih(parol,user)
    elif valik==1:
        registreerimine(parol,user)
    elif valik==2:
        sign_in(parol,user)
    elif valik==3:
        change(parol,user)
    elif valik==4:
        change2(parol,user)
        """
        dplj cluh drnm exef 
        """

