# Zufallsgenerator
import random
random.seed()

# Werte und berechnungen
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b

print("Die Aufgabe:", a, "+", b)

# Schleife Initialisieren
zahl = c + 1

# Anzahl initialisieren
versuch = 0

# Schleife mit while
while zahl != c:
    # Anzahl Versuche
    versuch = versuch + 1

    # Eingabe 
    print("Bitte eine Zahl eingeben:")
    z = input()

    # Versuch einer Umwandlung
    try:
        zahl = int(z)
    except:
        # Falls Umwandlung nicht erfolgreich
        print("Sie haben keine Zahl eingegeben")
        # Schleife unmittelbar fortsetzen
        continue
    
    # Verzweigung
    if zahl == c:
        print(zahl, "ist richtig")
    else:
        print(zahl, "ist falsch")

# Anzahl versuche
print("Ergebnis: ", c)
print("Anzahl Versuche:", versuch)
