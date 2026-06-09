import random
import string

def genereer_wachtwoord(lengte=12):
    tekens = string.ascii_letters + string.digits + string.punctuation
    wachtwoord = ''.join(random.choice(tekens) for _ in range(lengte))
    return wachtwoord

# Maak een random wachtwoord
print("Je nieuwe wachtwoord is:", genereer_wachtwoord())