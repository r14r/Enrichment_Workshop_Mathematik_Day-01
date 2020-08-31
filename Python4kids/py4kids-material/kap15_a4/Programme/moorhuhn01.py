# Python für Kids - Kapitel 15:  Moorhuhn

# Autor: Gregor Lingl
# Datum: 27. 8. 2009
# moorhuhn_01.py  - Entwicklung der Moorhuhn-Spiels

from turtle import Screen, Turtle

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

    def melde(self, txt):
        """Gibt Text txt im Grafik-Fenster aus.
        """
        self.schreiber.clear()
        self.schreiber.write(txt, font=("Courier", 18, "bold"))

    def schuss(self, x, y):
        """Wird bei Mausklick auf das Grafikfenster aufgerufen,
        wenn das Spiel läuft.
        """
        self.schuesse = self.schuesse + 1
        self.melde("SCHUSS {0}".format(self.schuesse))

    def spiel(self):
        # Initialisierung
        self.screen.onkeypress(None, "space")
        self.screen.onclick(self.schuss)
        self.melde("SPIEL LÄUFT!")
        self.schuesse = 0

        # Ausführung
        while self.schuesse < 5:  # SCHUESSE:
            print("*", end="") 
        self.screen.onclick(None)

        # Abschluss und Ergebnis
        self.screen.onkeypress(self.spiel, "space")
        self.melde("DAS SPIEL IST AUS! - Leertaste!!!")

    def run(self):
        self.melde("Start mit Leertaste!")
        self.screen.onkeypress(self.spiel, "space")
        self.screen.listen()

if __name__ == "__main__":
    spiel = MoorhuhnSpiel()
    spiel.run()
