def initialiseer_bord():
    # bord = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    bord = []
    for rij in range(3):
        rij_inhoud = []
        for kolom in range(3):
            rij_inhoud.append(' ')
        bord.append(rij_inhoud)
    return bord


def print_bord(bord):
    print()                     # Print een lege lijn
    for rij in bord:
        print('|'.join(rij))    # Print de zetten van de rij, gescheiden door verticale strepen
        print('-' * 5)          # Print een horizontale lijn, "-----"


def zet(bord, rij, kolom, speler):
    bord[rij][kolom] = speler   # "speler" is gelijk aan "X" of "O"
    return bord


def controleer_input(bord, rij, kolom):
    rij_is_geldig = 0 <= rij <= 2       # Geldig rijnummer
    kolom_is_geldig = 0 <= kolom <= 2   # Geldig kolomnummer

    if rij_is_geldig and kolom_is_geldig:
        if bord[rij][kolom] == ' ':     # Controle of vakje vrij is
            return True
    return False                        # Als we nergens return True deden, return dan False


def controleer_winnaar(bord):
    if controleer_horizontaal(bord) or controleer_verticaal(bord) or controleer_diagonaal(bord):
        return True
    else:
        return False


def controleer_horizontaal(bord):
    for rij in bord:
        if rij[0] == rij[1] == rij[2] != ' ':
            return True
    return False


def controleer_verticaal(bord):
    for kolom in range(3):
        if bord[0][kolom] == bord[1][kolom] == bord[2][kolom] != ' ':
            return True
    return False


def controleer_diagonaal(bord):
    if bord[0][0] == bord[1][1] == bord[2][2] != ' ':
        return True
    if bord[0][2] == bord[1][1] == bord[2][0] != ' ':
        return True
    return False


