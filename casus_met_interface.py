from tabulate import tabulate
import csv

# =====================
# DATA INLEZEN
# =====================

with open("personeel.csv", "r", encoding="utf-8") as f:
    data_list = []
    reader = csv.reader(f)

    for row in reader:
        data_list.append(row)

headers = data_list[0]
data = data_list[1:]

# =====================
# FUNCTIONALITEITEN
# =====================

def toon_alle_data():
    print(tabulate(data, headers=headers, showindex=True))


def toon_alle_afdelingen():
    afdelingen = sorted(set([x[3] for x in data]))

    for e, afdeling in enumerate(afdelingen):
        print(e, afdeling, end="\t")

    print()


def toon_alle_functies():
    functies = sorted(set([x[4] for x in data]))

    print("\nVolgende functies zijn er in de onderneming")
    print("------------------------------------------")

    for e, functie in enumerate(functies):
        print(e, functie)


def toon_iedereen_van_afdeling():
    toon_alle_afdelingen()

    afdeling = input("\nGeef de naam van de afdeling: ")

    afdeling_data = [x for x in data if afdeling == x[3]]

    print(tabulate(afdeling_data, headers=headers))


def toon_iedereen_met_bedrijfswagen():
    wagen_data = [x for x in data if x[6] == "Ja"]

    print(tabulate(wagen_data, headers=headers))
    print(f"\n{len(wagen_data)} medewerkers hebben een bedrijfswagen")


def voeg_persoon_toe():
    voornaam = input("Voornaam: ").capitalize()
    achternaam = input("Achternaam: ").capitalize()
    geslacht = input("Geslacht (M/V/X): ").upper()
    afdeling = input("Afdeling: ")
    functie = input("Functie: ").capitalize()
    loon = int(input("Loon: "))
    bedrijfswagen = input("Bedrijfswagen (Ja/Nee): ").capitalize()

    nieuw_pers = [
        voornaam,
        achternaam,
        geslacht,
        afdeling,
        functie,
        loon,
        bedrijfswagen
    ]

    data.append(nieuw_pers)

    print("Persoon toegevoegd.")


def toon_namen():
    namen = [f"{x[0]} {x[1]}" for x in data]

    for e, naam in enumerate(namen):
        print(e, naam)


def verwijder_persoon():
    toon_namen()

    try:
        index = int(
            input("\nGeef het nummer van de persoon die je wilt verwijderen: ")
        )

        if 0 <= index < len(data):
            verwijderd = data.pop(index)
            print(
                f"{verwijderd[0]} {verwijderd[1]} werd verwijderd."
            )
        else:
            print("Persoon kan niet verwijderd worden.")

    except ValueError:
        print("Geef een geldig nummer in.")


def pas_het_loon_aan():
    toon_namen()

    try:
        index = int(input("\nGeef het nummer van de persoon: "))

        if 0 <= index < len(data):
            nieuw_loon = int(input("Geef het nieuwe loon: "))
            data[index][5] = nieuw_loon
            print("Loon aangepast.")
        else:
            print("Kan loon niet aanpassen.")

    except ValueError:
        print("Geef geldige gegevens in.")


def sorteer_op_loon_aflopend():

    def loon_key(x):
        return int(x[5])

    res = sorted(data, key=loon_key, reverse=True)

    print(tabulate(res, headers=headers))


def update_data():
    with open("personeel.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(headers)
        writer.writerows(data)

    print("Data opgeslagen in personeel.csv")


# =====================
# MENU VIA DICTIONARY
# =====================

functies = {
    "1": toon_alle_data,
    "2": toon_alle_afdelingen,
    "3": toon_alle_functies,
    "4": toon_iedereen_van_afdeling,
    "5": toon_iedereen_met_bedrijfswagen,
    "6": voeg_persoon_toe,
    "7": verwijder_persoon,
    "8": pas_het_loon_aan,
    "9": sorteer_op_loon_aflopend,
    "10": update_data
}

# =====================
# HOOFDLUS
# =====================

while True:

    print("\n")
    print("=" * 40)
    print("      PERSONEELSBEHEER")
    print("=" * 40)
    print("1  - Toon alle data")
    print("2  - Toon alle afdelingen")
    print("3  - Toon alle functies")
    print("4  - Toon iedereen van een afdeling")
    print("5  - Toon medewerkers met bedrijfswagen")
    print("6  - Voeg persoon toe")
    print("7  - Verwijder persoon")
    print("8  - Pas loon aan")
    print("9  - Sorteer op loon (aflopend)")
    print("10 - Bewaar wijzigingen")
    print("0  - Stoppen")

    keuze = input("\nMaak een keuze: ")

    if keuze == "0":
        print("Programma afgesloten.")
        break

    if keuze in functies:
        functies[keuze]()
    else:
        print("Ongeldige keuze.")