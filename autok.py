from os import system

system("cls")

class autok:
    def __init__(self,ar,tipus,evjarat):
        self.ar=ar
        self.tipus=tipus
        self.evjarat=evjarat
def __str__(self):
        return f"{self.ar} {self.tipus} {self.evjarat}"
adatok_lista=[]
for i in range(3):
    ar=int(input('Kérem az autó árát: '))
    tipus=input('Kérem az autó típusát: ')
    evjarat=int(input('Kérem az autó évjáratát!'))

   
    adatok_lista.append(ar)

print(sum(adatok_lista))





