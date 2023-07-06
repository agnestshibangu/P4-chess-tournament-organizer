from colorama import Fore, Back
from colorama import init
import sys


def start_tournament():
    while True:
        init(autoreset=True)
        print(Back.GREEN + 'Voulez-vous démarrer un tournoi ? [Y/N]')
        data = input()
        if data == 'Y':
            print(Fore.GREEN + 'STARTING A NEW TOURNAMENT...')
            break
        elif data == 'N':
            print(Fore.RED + 'GOOD BYE !')
            sys.exit()
        else:
            print('invalide answer')
