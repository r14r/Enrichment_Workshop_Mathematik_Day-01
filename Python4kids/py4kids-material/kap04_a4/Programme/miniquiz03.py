# Python für Kids -- 4. Auflage, Kapitel 4
# Autor: Gregor Lingl
# Datum: 6. 8. 2009
# miniquiz03.py : (3) - mit drei Fragen

punkte = 0

frage = "Welche Programmiersprache lernst du gerade? "
loesung = "Python"

antwort = input(frage)
if antwort == loesung:
    print("Richtig!")
    punkte = punkte + 1
else:
    print("Leider falsch!")
    print("Richtig ist:", loesung)
print()

frage = """Mit welchem reservierten Wort beginnt eine
Funktionsdefinition? """
loesung = "def"

antwort = input(frage)
if antwort == loesung:
    print("Richtig!")
    punkte = punkte + 1
else:
    print("Leider falsch!")
    print("Richtig ist:", loesung)
print()

frage = "Wieviel reservierte Wörter hat Python? "
loesung = "33"

antwort = input(frage)
if antwort == loesung:
    print("Richtig!")
    punkte = punkte + 1
else:
    print("Leider falsch!")
    print("Richtig ist:", loesung)
print()

print("Du hast", punkte, "von 3 Punkten erreicht!")
