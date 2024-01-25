import random


def veletlen():
    lista=[]
    for i in range(10):
        szam=random.randint(10,350)
        lista.append(szam)
        if i > 9:
            print(szam,end="")
        else:
            print(szam,end="#")
    return lista

def parosok_szama(lista):
    megszamol=0
    for i in range(0,len(lista),1):
        if lista[i] % 2 == 0:
            megszamol+=1
    return megszamol

def konzol_kiir(db):
    print(f"\t A párosok száma:{db}")
def fajl_kiir(db):
    fajl=open("kimutatas.txt","w","utf-8")
    fajl=write("kimutatas.txt")
    fajl=print(f"\t A párosok száma:{db}")
