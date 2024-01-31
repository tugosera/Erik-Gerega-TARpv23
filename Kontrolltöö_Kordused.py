#1


#try:
#    i=int(input("sisesta sõnaseadjate arv ")) 
#except:
#    ValueError


#if 0>i>9:
#    print("error")
#else:
#    for i in range (0,i,1):
#        print(" -----  ")
#        print("|  O  |  ")
#        print("!  -  !  ")
#        print(" -----  ")

#2


a=int(input("vvedite chislo"))
d=int(input("vvedite chislo ese raz"))
b=int(input("vvedite vtoroe chislo"))

while True:
    for a in range(0,d,1):
        c=int()
        c=a**b
        if c<a**3:
            print(c)
        elif c>a**4:
            break
        

