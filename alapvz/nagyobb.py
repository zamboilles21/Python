from os import system

system('cls')
egyik = int(input('Adj meg egy számot: '))
masik = int(input('Adj meg egy másik számot: '))
if egyik < masik:
    print(f'A nagyobb érték: {masik}')
elif masik < egyik:
    print(f'A nagyobb érték: {egyik}')
else:
    print('Egyenlő')
    
