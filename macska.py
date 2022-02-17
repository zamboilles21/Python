from os import system

system("cls")
class Macska:
    def _init_(self, nev, suly, ehese=True):
        self.nev = nev
        self.suly = suly
        self.ehese = ehese

    def eszik(self, mennyiseg):
        if self.ehese:
            self.suly += mennyiseg
            self.ehese=False
            return True
        return False

    def futkos(self):
        self.suly -= 0.1
        if not self.ehese:
            self.ehese=True
    def __str__(self):
        if  self.ehese:
            return f"{self.nev} macska éhes, súlya: {self.suly}"
        return f"{self.nev} macska nem éhes, súlya: {self.suly}"

m1 = Macska("Cili", 1.8, False)
m2 = Macska("Sanyi", 3.85)

if m1.eszik(0.1):
    print(f"{m1.nev} kajált!")
else:
    print(f"{m1.nev} nem kajált!")

if m2.eszik(0.2):
    print(f"{m2.nev} kajált!")
else:
    print(f"{m2.nev} nem kajált!")

m1.futkos()
m2.futkos()
print(m1)
print(m2)


    



