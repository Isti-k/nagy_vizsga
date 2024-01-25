import random
def bekeres():
    rendezo=input("\t Adja meg a rendező nevét:")
    film_cime=input("\t Aja meg a film címét:")
    print("I/A")
    print(f"\t Rendező neve: {rendezo}")
    print(f"\t Film címe: {film_cime}")
    print("I/B")
    szam=random.randint(0,10)
    print("\t Pontozás (0-10):")
    if szam < 4:
        print("\t Gyenge film.")
    elif 3 < szam > 8:
        print("\t Érdemes megnézni!")
    else:
        print("\t kihagyhatatlan film!")