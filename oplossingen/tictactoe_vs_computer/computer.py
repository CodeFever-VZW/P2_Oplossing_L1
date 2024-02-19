from mytictactoe import *
import random


def random_zet(bord):
    while True:
        rij = random.randint(0, 2)
        kolom = random.randint(0, 2)

        if bord[rij][kolom] == ' ':
            bord[rij][kolom] = ' '

            return rij, kolom


def vind_beste_zet(bord, speler):
    for rij in range(3):
        for kolom in range(3):
            if bord[rij][kolom] == ' ':
                bord[rij][kolom] = speler

                if controleer_winnaar(bord):  # Als er een winnaar is (True)
                    bord[rij][kolom] = ' '
                    return rij, kolom
                bord[rij][kolom] = ' '
    rij = None
    kolom = None
    return rij, kolom


def computer_zet(bord, speler, tegenspeler):
    # kijk voor overwinning in de huidige beurt
    rij, kolom = vind_beste_zet(bord, speler)

    if not rij:  # Geen beste zet gevonden
        # kijk of de tegenspeler kan winnen in de volgende beurt
        rij, kolom = vind_beste_zet(bord, tegenspeler)

        if not rij:  # Weer geen beste zet gevonden
            rij, kolom = random_zet(bord)

    return rij, kolom

