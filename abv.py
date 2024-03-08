def registreerimine (p:list,u:list,)->any:
    """

    """
    username=input("Vedite username: ")
    parol=input("Vedite parol: ")
    return p,u

def vivod_dannih (p:list,u:list,)->any:
    """

    """
    print("usernames: ", u)
    print("passwords: ", p)
    print()
    return p,u

def sign_in (p:list,u:list,)->any:
    """

    """
    username=input("Vedite username: ")
    parol=input("Vedite password: ")
    for i in range(0, len(u)):
        if username==u[i]:
            for y in range(0, len(p)):
                if parol==p[y]:
                    print("Vi voshli v akaunt")
                else:
                    print("neverni parol")
        else: 
            print("Polzovatel s takim username ne naiden")
    print()
    return p,u


def change (p:list,u:list,)->any:
    """

    """
    username=input("Vedite username: ")
    novij=input("Vedite novij username: ")
    for i in range(0, len(u)):
        if username==u[i]:
            u[i] = novij
    print()
    return p,u

def change2 (p:list,u:list,)->any:
    """

    """
    password=input("Vedite parol: ")
    novij=input("Vedite novij parol: ")
    for i in range(0, len(p)):
        if password==p[i]:
            p[i] = novij
    print()
    return p,u
