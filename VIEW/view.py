from colorama import Fore, Back, Style
from colorama import init
import sys

class view:
 
    def prompt_start_tournament():
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

    def display_all_players(players):
        print('The list of players')
        for player in players:
            print('player num ' + str(player.player_number))

    def print_final_winner(players):
        print('LE GAGNANT EST LE JOUEUR NUMERO ' + str(players[0]))
        print('LE TOURNOI EST TERMINE !!!!')
        sys.exit()

    def print_first_tour_name(tour):
        print(' ')
        print(Back.BLUE + tour._name)
        print('c est le premier tour donc on melange les joueurs au hasard')

    def display_points_retreive_first_tour_start():
        print(' ')
        print(Fore.MAGENTA + '|||||||||||||||||||||||||||||||||||||||||||||||||||||')
        print(Back.MAGENTA + '------ RECUPERATION DES POINTS POUR LE PREMIER ------')
        print(Fore.MAGENTA +'|||||||||||||||||||||||||||||||||||||||||||||||||||||')
        print(' ')

    def retreive_single_score(player):
        while True: 
                print("player's number : " + player.player_number)   
                print("entrez le score de ce joueur [WIN/LOO/TIE]")
                result = input()
                if result == 'w':
                    print(Fore.GREEN + 'CE JOUEUR A GAGNE LA PARTIE !')
                    player.player_score += 1
                    player.player_score
                    print(Fore.GREEN + "player's score : " + str(player.player_score))  
                    print(' ')
                elif result == 't':
                    print(Fore.YELLOW + "PARTIE NULLE" )
                    player.player_score += 0.5
                    player.player_score
                    print(Fore.YELLOW + "player's score : " + str(player.player_score))  
                    print(' ')
                elif result == 'l':
                    print(Fore.RED + 'CE JOUEUR A PERDU | ELIMINATION')
                    player.player_score
                    print(' ')
                else: 
                    print(Back.RED + 'MAUVAIS INPUT')
                return player



