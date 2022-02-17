from os import system

system("cls")

class számitógép:
    def __init__(self, memo, bekapcs):
        self.memo = memo
        self.bekapcs = bekapcs
    def kapcsol(self):
        self.bekapcs = not self.bekapcs
    def program_masol(self, méret):
        if self.memo > méret and self.bekapcs:
            self.memo -= méret
            return True
        return False

pc1 = számitógép(2048, False)
pc2 = számitógép(1024, False)

pc2.bekapcs()
print("Sikeres") if pc2.program_masol(800) else print("Sikertelen")
print("Sikeres") if pc2.program_masol(400) else print("Sikertelen")
print("Sikeres") if pc1.program_masol(800) else print("Sikertelen")
            


    
