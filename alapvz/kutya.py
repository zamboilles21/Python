from os import system
from osztalyok import kutya

system('cls')

kutyak=[]

for _ in range(3):
    nev = input("Kutya neve: ")
    szul_eve = int(input("Kutya születési éve: "))
    suly=int(input("Kutya súlya: "))
    kutyak.append(kutya(nev, szul_eve, suly))

legfiatalabb = kutyak[0]
for kutya in kutyak:
    if kutya.szul_eve < legfiatalabb.szul_eve:
        legfiatalabb = kutya

    