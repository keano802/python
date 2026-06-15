# Sla je notitie op als tekstbestand
notitie_tekst = input("Typ hier je notitie: ")

with open("mijn_notitie.txt", "a") as bestand:
    bestand.write(notitie_tekst + "\n")

print("Notitie succesvol opgeslagen!")


import tkinter as tk
from tkinter import messagebox

def opslaan_notitie():
    inhoud = tekst_vak.get("1.0", tk.END)
    with open("notitie.txt", "w") as f:
        f.write(inhoud)
    messagebox.showinfo("Succes", "Notitie is opgeslagen!")

# Venster instellen
venster = tk.Tk()
venster.title("Mijn Python Notitie App")

# Tekstvak
tekst_vak = tk.Text(venster, height=15, width=40)
tekst_vak.pack()

# Opslaan Knop
knop = tk.Button(venster, text="Opslaan", command=opslaan_notitie)
knop.pack()

# Applicatie starten
venster.mainloop()
