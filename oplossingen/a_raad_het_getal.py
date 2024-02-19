import random

def is_getal_geraden(gok, geheim_nummer):
    if gok == geheim_nummer:
        print("Correct!")
        return True
    else:
        print("Fout, Probeer opnieuw!")
        return False


def raad_het_getal(bovengrens):
    geheim_nummer = random.randint(1, bovengrens)
    geraden = False

    while not geraden:
        gok = int(input(f"Raad een getal (1-{bovengrens}): "))
        geraden = is_getal_geraden(gok, geheim_nummer)


raad_het_getal(bovengrens=10)