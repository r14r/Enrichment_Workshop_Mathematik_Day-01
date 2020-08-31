# Python für Kids - Kapitel 15:  Moorhuhn

# Autor: Gregor Lingl
# Datum: 27. 8. 2009
# moorhuhn_03.py  - Entwicklung der Moorhuhn-Spiels

from turtle import Screen, Turtle
import random

class Huhn(Turtle):
    """Objekte dieser Klasse sind Moorhühner im Moorhuhn-Spiel.
    Sie 'fliegen' geradlinig und - wenn getroffen - auf einer
    Parabelbahn.
    """
    def __init__(self, bilddatei, moorhuhnspiel):
        Turtle.__init__(self, shape=bilddatei)
        self.spiel = moorhuhnspiel
        self.hideturtle()
        self.penup()
        self.speed(0)

    def zumstart(self):
        self.hideturtle()
        self.setpos(-340, random.randint(-120, 120))
        self.vx = random.randint(6,11) 
        self.vy = random.randint(-3,3) 
        self.showturtle()
        self.tot = False

    def schritt(self):
        if self.tot:
            self.vy = self.vy - 0.25
        x, y = self.position()
        x = x + self.vx
        y = y + self.vy
        self.goto(x,y)
               
    def raus(self):
        x, y = self.position()
        return x > 340 or abs(y) > 250

    def getroffen(self, x, y):
        if self.tot:
            return
        self.tot = True
        self.spiel.treffer = self.spiel.treffer + 1

class MoorhuhnSpiel:
    """Kombiniert die Bestandteile des Moorhuhnspiels.
    Legt den Spielablauf fest.
    """
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(640, 480)
        self.screen.clear()
        self.screen.title("Moorhuhn - Python für Kids, Kapitel 15")
        self.screen.bgpic("landschaft.gif")
        self.screen.register_shape("huhn01.gif")
        self.screen.register_shape("huhn02.gif")
        # Der Schreib-Gehilfe
        self.schreiber = Turtle(visible=False)
        self.schreiber.speed(0)
        self.schreiber.penup()
        self.schreiber.goto(-290, -220)
        self.schreiber.pencolor("yellow")
        # Die Moorhühner
        self.huehner = (Huhn("huhn01.gif", self), 
                        Huhn("huhn02.gif", self))    

    def melde(self, txt):
        """Gibt Text txt im Grafik-Fenster aus.
        """
        self.schreiber.clear()
        self.schreiber.write(txt, font=("Courier", 18, "bold"))

    def spielstand(self):
        return "Treffer/Schüsse: {0}/{1}".format(
                                   self.treffer, self.schuesse)
    def schuss(self, x, y):
        """Wird bei Mausklick auf das Grafikfenster aufgerufen,
        wenn das Spiel läuft.
        """
        self.schuesse = self.schuesse + 1
        self.melde(self.spielstand())

    def spiel(self):
        # Initialisierung
        self.screen.onkeypress(None, "space")
        self.screen.onclick(self.schuss)
        self.melde("SPIEL LÄUFT!")
        self.schuesse = 0
        self.treffer = 0
        for huhn in self.huehner:
            huhn.zumstart()
            huhn.onclick(huhn.getroffen)
        # Ausführung
        while self.schuesse < 5:  # SCHUESSE:
            for huhn in self.huehner:
                huhn.schritt()        
                if huhn.raus():
                    huhn.zumstart()
        self.screen.onclick(None)

        # Abschluss und Ergebnis
        self.screen.onkeypress(self.spiel, "space")
        self.melde(self.spielstand() + " - Leertaste drücken!")

    def run(self):
        self.melde("Start mit Leertaste!")
        self.screen.onkeypress(self.spiel, "space")
        self.screen.listen()

if __name__ == "__main__":
    spiel = MoorhuhnSpiel()
    spiel.run()