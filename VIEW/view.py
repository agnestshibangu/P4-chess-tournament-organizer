from colorama import Fore, Back
from colorama import init
import sys


class View:
    

    # @staticmethod
    def prompt_start_tournament():

        ''' This function ask for the user input. 'Y' to start a tournament and 
        'N' to quit the program. If the input is neither 'Y' or 'N', it exits the program.
        '''
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

        ''' This function takes as parameter players and displays them with their number. 
        '''
        print('The list of players')
        for player in players:
            print('player num ' + str(player.player_number))

    # @staticmethod
    def print_final_winner(players):
        
        ''' This function takes as parameter players when len(players) == 1
        and displays the winner.
        '''
        print('LE GAGNANT EST LE JOUEUR NUMERO ' + str(players[0]))
        print('LE TOURNOI EST TERMINE !!!!')
        sys.exit()

    # @staticmethod
    def print_first_tour_name(tour):
        
        ''' This function takes as parameter tour and displays the name of the tour
        '''
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

        ''' This function asks for the input of the user to get and calculate the score for each player.
        'w' means that the player won and his score is incremented by 1.  'l' means that the player lost
        and his score is not incremented. 't' means that the players has a tie and his score is incremented 
        with 0.5 points. If the input is neither of the above, a message 'wrong input' is displayed and the user
        has to input something valid.
        '''
        
        while True:
            print("player's number : " + player.player_number)
            print('Entrez le score de ce joueur' +
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
        ''' This function takes as a parameter a tour object and displays
        the attriburtes for each matches that are contained in this tour. 
        the number player --> player.player_number is being displayed for 
        each player for each match.   
        '''
        for match in tour:
            print(' ')
            print(' ')
            init(autoreset=True)
            print(Fore.BLUE + match._name)
            print(' ')
            print(Fore.BLUE + '-----------------------------------------')
            for player in match._array:
                print(player.player_number)
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
        ''' this function is called in the controllerTour.
        is display for each player his number --> player.player_number,
        and takes an input that determines the new score to be attributed 
        to the player score. 
        input w = win = 1 point / l = loose = 0 / t = tie = 0.5
        if the input is different from this 3 values, the score is aked again
        '''

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
        ''' This function is called when the length of selected_players (the parameter)
        is equal to 1. it then takes the first argument of the list and print the number 
        of the remaining player wich is the winner. 
        '''

        print('\n')
        print(Fore.GREEN + '||||||||||||||||||||||||||||' +
              '||||||||||||||||||||||||||||||||||||||')
        print("LE GAGNANT EST : " +
              str(selected_players[0].player_number))
        print(Fore.GREEN + '||||||||||||||||||||||||||||' +
              '||||||||||||||||||||||||||||||||||||||')
        
    
