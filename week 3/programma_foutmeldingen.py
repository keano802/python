import tkinter as tk
from tkinter import messagebox

# Hoofdvenster verbergen
root = tk.Tk()
root.withdraw()

# Foutmelding tonen
messagebox.showerror("Fout", "Er is iets misgegaan!")