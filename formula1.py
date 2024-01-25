from Osztaly import Osztaly

def kiir():
    fajl=open("balkezesek.txt","r","utf-8")
    fajl.readline()
    fajl_lista=fajl.readlines()
    fajl.close()

    lista=[]
    for i in range(0,len(fajl_lista),1):
        aktsor=fajl_lista.strip().split(",")
        balkezes=Osztaly(aktsor[0],aktsor[1],aktsor[2],aktsor[3],aktsor[4])
        lista.append(balkezes)
    return lista


def jatekosok(lista,i):
    print(f"\t A balkezes játékosok száma:{len(lista)}")

def atlag_sulya():
    




