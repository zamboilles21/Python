class Stadion:
    def __init__(self, sor):
        adatok = sor.Split(';')
        self.varos = adatok[0]
        self.nev = adatok[1]
        self.nev2 = adatok[2]
        self.ferohely = int(adatok[3])
