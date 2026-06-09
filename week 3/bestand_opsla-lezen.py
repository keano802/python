# Bestand schrijven
with open("voorbeeld.txt", "w") as bestand:
    bestand.write("Hallo, dit is opgeslagen tekst!")

print("Bestand opgeslagen.")

# Bestand lezen
with open("voorbeeld.txt", "r") as bestand:
    inhoud = bestand.read()

print("Inhoud van het bestand:")
print(inhoud)
