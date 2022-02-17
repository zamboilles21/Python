from os import system

system('cls')

egyik = str(input('Adjon meg egy szót: '))
masik = str(input('Adjon meg egy masik szót: '))

if len(egyik)<len(masik):
    print(f'A hosszabbik: {masik}')
elif len(masik)<len(egyik):
    print(f'A hosszabbik: {egyik}')
else:
    print('Egyenlő')
    