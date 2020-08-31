# Python für Kids -- 4. Auflage, Kapitel 9
# Autor: Gregor Lingl
# Datum: 10. 8. 2009
# randomwalk04.py

from turtle import *
import random

def zufallsschritt(laenge, maxwinkel):
    winkel = random.randint(-maxwinkel,maxwinkel)
    left(winkel)
    forward(laenge)

def randomwalk(entfernung, schrittlaenge, maxwinkel=180):
    global schrittsumme
    pu(); home(); pd()
    startwinkel = random.randint(0, 395)
    right(startwinkel)
    start = position()
    schritte = 0
    while distance(start) < entfernung:
        zufallsschritt(schrittlaenge, maxwinkel)
        schritte = schritte + 1
    schrittsumme = schrittsumme + schritte
    print("Anzahl der Schritte: ", schritte)

def randomwalk_test(anzahl_walks):
    global schrittsumme
    reset()
    setup(400,400)
    speed(0)
    pensize(1)
    schrittsumme = 0
    for i in range(anzahl_walks):
        pencolor("black")
        randomwalk(150, 15)
        pencolor("red")
        stamp()
    durchschnitt = schrittsumme / anzahl_walks
    print("Durchschnittliche Schrittanzahl:", durchschnitt)

if __name__ == "__main__":
    randomwalk_test(6)
