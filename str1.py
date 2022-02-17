from  os import system

system("Cls")

teljes_nev = input("Írd be a neved: ")
nevek = teljes_nev.split()
for  nev in nevek:
    print(f"{nev[0].upper()}.",end="")
    
"""
print(f"{nevek[0][0].upper()}.{nevek[1][0].upper()}.")
"""