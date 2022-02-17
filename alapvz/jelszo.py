from os import system

system('cls')

while True:
    fnev= input('Felhasználónév: ')
    pw=input('Jelszó:')
    if fnev == 'bori99' and pw == 'Szivecske<3':
        print('Belépés engedélyezve')
        break
    print('Belepés megtagadva')