from tabulate import tabulate
import csv
#lees de data in
with open("personeel.csv", "r") as f:
    data_list = []
    data = csv.reader(f)
    for row in data:
        data_list.append(row)

headers = data_list[0]
data = data_list[1:]

###functionaliteiten###

def toon_alle_data():
    print(tabulate(data,headers=headers,showindex=True))

def toon_alle_afdelingen():
    #steek alle unieke waardes van afdeling uit data in 1 lijst
    afdelingen = sorted(set([x[3] for x in data]))
    for e,afdeling in enumerate(afdelingen):
        print(e,afdeling,end="\t")
    print()

def toon_alle_functies():
    #steek alle unieke waardes van afdeling uit data in 1 lijst
    functie = sorted(set([x[4] for x in data]))
    print("volgende functies zijn er in de onderneming")
    print("-----------------------------")
    for e,functie in enumerate(functie):
        print(e,functie)


def toon_iedereen_van_afdeling():
    #welke afdeling
    toon_alle_afdelingen()
    afdeling = input("geef de naam van de afdeling")
    #iedereen tonen van die afdeling
    #de rij wordt opgevangen als de afdeling van de rij = gevraagde afdeling
    afdeling_data = [x for x in data if afdeling == x[3]]
    print(tabulate(afdeling_data,headers=headers))

def toon_iedereen_met_bedrijfswagen():
    #indien de waarde van index 6 in de rij == "Ja" dan bedrijfswagen
    wagen_data = [x for x in data if "Ja" == x[6]]
    print(tabulate(wagen_data,headers=headers))
    print(f"{len(wagen_data)} hebben een bedrijfswagen")

def voeg_persoon_toe():
    voornaam = input("voornaam").capitalize()
    achternaam = input("achternaam").capitalize()
    geslacht = input("geslacht").upper()
    afdeling = input("afdeling")
    functie = input("functie").capitalize()
    loon = int(input("loon"))
    bedrijfswagen = input("bedrijfswagen Ja / Nee").capitalize()
    nieuw_pers = [voornaam,achternaam,geslacht,afdeling,functie,loon,bedrijfswagen]
    data.append(nieuw_pers)

def toon_namen():
    #lijst maken met string van de voornaam(0) en achternaam(1) uit de data
    namen = [str(x[0]+" "+x[1]) for x in data]
    for e,naam in enumerate(namen):
        print(e,naam)

def verwijder_persoon():
    toon_namen()
    index = int(input("geef het nummer van de persoon die je wilt verwijderen"))
    if index < len(data):
        data.pop(index)
    else:
        print("persoon kan niet verwijderd worden")

def pas_het_loon_aan():
    #wie? nieuwe_loon
    toon_namen()
    index = int(input("geef het nummer van de persoon"))
    if index < len(data):
        nieuw_loon = int(input("geef het nieuwe loon"))
        data[index][5] = nieuw_loon #index rij(welke persoon) 5 loondata staat
    else:
        print("kan loon niet aanpassen")


def sorteer_op_loon_aflopend():
    res = sorted(data,key=lambda x:x[5],reverse=True)
    print(tabulate(res,headers=headers))

def update_data():
    with open('personeel.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        data.insert(0, headers)
        new_data = data
        writer.writerows(new_data)

toon_alle_data()