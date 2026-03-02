def drucke_spielfeld(spielfeld):
    print()
    for i in range(3):
        print(" | ".join(spielfeld[i]))
        if i < 2:
            print("-" * 9)
    print()


def pruefe_sieger(spielfeld):
    # Reihen prüfen
    for reihe in spielfeld:
        if reihe[0] == reihe[1] == reihe[2] != " ":
            return reihe[0]

    # Spalten prüfen
    for spalte in range(3):
        if spielfeld[0][spalte] == spielfeld[1][spalte] == spielfeld[2][spalte] != " ":
            return spielfeld[0][spalte]

    # Diagonalen prüfen
    if spielfeld[0][0] == spielfeld[1][1] == spielfeld[2][2] != " ":
        return spielfeld[0][0]

    if spielfeld[0][2] == spielfeld[1][1] == spielfeld[2][0] != " ":
        return spielfeld[0][2]

    return None


def ist_unentschieden(spielfeld):
    for reihe in spielfeld:
        if " " in reihe:
            return False
    return True


def hauptprogramm():
    spielfeld = [[" " for _ in range(3)] for _ in range(3)]
    aktueller_spieler = "X"

    while True:
        drucke_spielfeld(spielfeld)

        try:
            zeile = int(input(f"Spieler {aktueller_spieler}, wähle eine Zeile (0-2): "))
            spalte = int(input(f"Spieler {aktueller_spieler}, wähle eine Spalte (0-2): "))
        except ValueError:
            print("Bitte eine Zahl eingeben!")
            continue

        if zeile not in range(3) or spalte not in range(3):
            print("Koordinaten außerhalb des gültigen Bereichs!")
            continue

        if spielfeld[zeile][spalte] != " ":
            print("Dieses Feld ist bereits belegt!")
            continue

        spielfeld[zeile][spalte] = aktueller_spieler

        sieger = pruefe_sieger(spielfeld)
        if sieger:
            drucke_spielfeld(spielfeld)
            print(f"Spieler {sieger} hat gewonnen! 🎉")
            break

        if ist_unentschieden(spielfeld):
            drucke_spielfeld(spielfeld)
            print("Unentschieden!")
            break

        aktueller_spieler = "O" if aktueller_spieler == "X" else "X"


if __name__ == "__main__":
    hauptprogramm()