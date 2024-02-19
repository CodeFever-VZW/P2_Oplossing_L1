from mytictactoe import *
from computer import *


def tic_tac_toe():
    bord = initialiseer_bord()
    huidige_speler = 'X'
    einde_spel = False
    winnaar = ''
    teller = 0

    while not einde_spel:
        print_bord(bord)

        if huidige_speler == 'X':
            rij = int(input("Kies een rij (0, 1, 2): "))
            kolom = int(input("Kies een kolom (0, 1, 2): "))
        else:
            rij, kolom = computer_zet(bord, 'O', 'X')

        if controleer_input(bord, rij, kolom):
            bord = zet(bord, rij, kolom, huidige_speler)
            einde_spel = controleer_winnaar(bord)
            teller += 1
            if einde_spel:
                winnaar = huidige_speler

            else:
                if huidige_speler == 'X':
                    huidige_speler = 'O'
                else:
                    huidige_speler = 'X'

        else:
            print("Ongeldige zet. Probeer opnieuw.")

        if teller == 9:
            einde_spel = True


    print_bord(bord)

    if winnaar == '':
        print("Het spel eindigt in gelijkspel.")
    else:
        print(f"Speler {winnaar} heeft gewonnen!")


tic_tac_toe()
