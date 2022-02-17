from os import system

system("cls")

class Torta:
    def __init__(self, emelet=1, kremese=False):
        self.emelet = emelet
        self.kremese = kremese

        def uj_emelet(self):
            self.emelet += 1

        def kremmel_megkent(self):
            if not self.kremese:
                self.kremese=True
                return True
            return False
        def mennyi_kal(self):
            if self.kremese:
                return self.emelet * 2000
            return self.emelet * 1000

        def __str__(self)
            return f"ez egy (self.emelet) emeletes {'kremes' if  self.kremese else 'Nem kremes'} torta":
                

t1 = Torta(2, True)
t2 = Torta()


                
