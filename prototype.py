# To-Do List Applicatie

taken = []

# Taken laden uit bestand
try:
    with open("taken.txt", "r") as bestand:
        for regel in bestand:
            taken.append(regel.strip())
except FileNotFoundError:
    pass


def toon_taken():
    if len(taken) == 0:
        print("Er zijn geen taken.")
    else:
        print("\nTaken:")
        for i, taak in enumerate(taken, start=1):
            print(f"{i}. {taak}")


def voeg_taak_toe():
    taak = input("Voer een nieuwe taak in: ")
    taken.append(taak)
    print("Taak toegevoegd!")


def verwijder_taak():
    toon_taken()

    if len(taken) == 0:
        return

    try:
        nummer = int(input("Welk taaknummer wil je verwijderen? "))

        if 1 <= nummer <= len(taken):
            verwijderde_taak = taken.pop(nummer - 1)
            print(f"'{verwijderde_taak}' verwijderd.")
        else:
            print("Ongeldig nummer.")

    except ValueError:
        print("Voer een geldig getal in.")


def sla_taken_op():
    with open("taken.txt", "w") as bestand:
        for taak in taken:
            bestand.write(taak + "\n")


while True:
    print("\n===== TO-DO LIST =====")
    print("1. Taak toevoegen")
    print("2. Taken bekijken")
    print("3. Taak verwijderen")
    print("4. Afsluiten")

    keuze = input("Maak een keuze: ")

    if keuze == "1":
        voeg_taak_toe()

    elif keuze == "2":
        toon_taken()

    elif keuze == "3":
        verwijder_taak()

    elif keuze == "4":
        sla_taken_op()
        print("Taken opgeslagen. Programma afgesloten.")
        break

    else:
        print("Ongeldige keuze.")