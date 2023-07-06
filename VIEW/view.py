from colorama import Fore, Back
from colorama import init
import sys


class View:
    # class view:

    # @staticmethod
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

    # @staticmethod
    def display_all_players(players):
        print('The list of players')
        for player in players:
            print('player num ' + str(player.player_number))

    # @staticmethod
    def print_final_winner(players):
        print('LE GAGNANT EST LE JOUEUR NUMERO ' + str(players[0]))
        print('LE TOURNOI EST TERMINE !!!!')
        sys.exit()

    # @staticmethod
    def print_first_tour_name(tour):
        print(' ')
        print(Back.BLUE + tour._name)
        print('c est le premier tour donc on melange les joueurs au hasard')

    # @staticmethod
    def display_points_retreive_first_tour_start():
        print(' ')
        print(Fore.MAGENTA + '||||||||||||||||||||||||||'
              + '|||||||||||||||||||||||||||')
        print(Back.MAGENTA + '------ RECUPERATION DES'
              + 'POINTS POUR LE PREMIER ------')
        print(Fore.MAGENTA + '||||||||||||||||||||||||||'
              + '|||||||||||||||||||||||||||')
        print(' ')

    # @staticmethod
    def retreive_single_score(player):
        while True:
            print("player's number : " + player.player_number)
            print('entrez le score de ce joueur' +
                  '[ w = WIN / l = LOO / t = TIE]')
            result = input()
            if result == 'w':
                print(Fore.GREEN + 'CE JOUEUR A GAGNE LA PARTIE !')
                player.player_score += 1
                player.player_score
                print(Fore.GREEN + "player's score : "
                      + str(player.player_score))
                print(' ')
                break
            elif result == 't':
                print(Fore.YELLOW + "PARTIE NULLE")
                player.player_score += 0.5
                player.player_score
                print(Fore.YELLOW + "player's score : "
                      + str(player.player_score))
                print(' ')
                break
            elif result == 'l':
                print(Fore.RED + 'CE JOUEUR A PERDU | ELIMINATION')
                player.player_score
                print(' ')
                break
            else:
                print(Back.RED + 'MAUVAIS INPUT')
        return player

    # @staticmethod
    def message_text_all_players():
        print('________________________________________________'
              '____________________________________________________')
        print(' un nouveau fichier texte contenant les' +
              'informartions pour tout les joueurs a ete cree ! ')
        print('________________________________________________'
              '____________________________________________________')

    # @staticmethod
    def message_text_tournament_players():
        print('________________________________________________'
              '____________________________________________________')
        print(' un nouveau fichier texte contenant les' +
              'informartions pour tout les joueurs du tournoi a ete cree ! ')
        print('________________________________________________'
              '____________________________________________________')

    # @staticmethod
    def message_text_tournament_infos():
        print('________________________________________________'
              '____________________________________________________')
        print('           un nouveau fichier texte contenant les' +
              ' informartions du tournoi en cours a ete cree !    ')
        print('________________________________________________'
              '____________________________________________________')

    # @staticmethod
    def message_text_all_tournament_infos():
        print('________________________________________________'
              '____________________________________________________')
        print(' un nouveau fichier texte contenant les' +
              ' informartions de tout les tournois a ete cree ! ')
        print('________________________________________________'
              '____________________________________________________')

    # VIEWS FOR THE CONTROLLER MATCHES
    # @staticmethod
    def message_player_same_as_history():
        print(' ce joueur figure deja dans l historique,' +
              ' un autre joueur va etre selectionne ')

    # @staticmethod
    def print_infos_for_each_match(tour):
        for match in tour:
            print(' ')
            print(' ')
            init(autoreset=True)
            print(Fore.BLUE + match._name)
            print(' ')
            print(Fore.BLUE + '-----------------------------------------')
        for player in match._array:
            print("player's number : " + player.player_number)
        print(Fore.BLUE + '-----------------------------------------')

    # @staticmethod
    def display_points_retreive_first_tour_end():
        print(Fore.MAGENTA + '||||||||||||||||||||||||||||' +
              '||||||||||||||||||||||||||||||||||||||')
        print(Back.MAGENTA + '------ LA RECUPERATION DES' +
              'POINTS EST TERMINEE POUR CE TOUR ------')
        print(Fore.MAGENTA + '||||||||||||||||||||||||||||' +
              '||||||||||||||||||||||||||||||||||||||')

    # @staticmethod
    def print_separator():
        print(Fore.BLUE + '-----------------------------------------')

    # @staticmethod
    def retreive_single_score_view(player):
        while True:
            print("player's number : " + player.player_number)
            print("entrez le score de ce joueur [w = WIN / l =LOO/ t = TIE]")
            result = input()
            if result == 'w':
                print(Fore.GREEN + 'CE JOUEUR A GAGNE LA PARTIE !')
                player.player_score += 1
                player.player_score
                print(Fore.GREEN + "player's score : "
                      + str(player.player_score))
                print(' ')
            elif result == 't':
                print(Fore.YELLOW + "PARTIE NULLE")
                player.player_score += 0.5
                player.player_score
                print(Fore.YELLOW + "player's score : "
                      + str(player.player_score))
                print(' ')
            elif result == 'l':
                print(Fore.RED + 'CE JOUEUR A PERDU | ELIMINATION')
                player.player_score
                print(' ')
            else:
                print(Back.RED + 'MAUVAIS INPUT')

    # @staticmethod
    def print_winner(selected_players):
        print('\n')
        print(Fore.GREEN + '||||||||||||||||||||||||||||' +
              '||||||||||||||||||||||||||||||||||||||')
        print("LE GAGNANT EST : player's number :" +
              str(selected_players[0].player_number))
        print(Fore.GREEN + '||||||||||||||||||||||||||||' +
              '||||||||||||||||||||||||||||||||||||||')
