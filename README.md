# Développez un programme logiciel en Python
## logiciel de gestion de tournoi


En tant que developpeur junior freelance, le but de ce projet est de creer un logiciel python qui fonctionne hors ligne pour automatiserla gestion de tournois. L'application suit une conception MVC. Les classes de tournoim joueurm matchs et tour servent de modeles. Les vues affichent les informations a l'utilisateur et recuperent ses inputs. Enfin, les controleurs servent a lancer de nouveaux tournois, produisent les resultat des matchs, etc... Les données des matchs sont stockées aux formats JSON et text.

## Installation

from source :

```sh
git clone https://github.com/agnestshibangu/P4-chess-tournament-organizer.git
cd code
python controller.py
```

Mode d'emploi : 

pour demarrer un nouveau tournoi, lancer le script controller.py et entrer Y une fois arrivé a la question suivante : 
```sh
Voulez-vous démarrer un tournoi ? [Y/N]
Y 
```

nommer le nouveau tournoi : 
```sh
Entrez un nom pour le tournoi: 
```
Entrer les scores des joueurs au moment de la récupération des points : 

3 inputs possibles 

w : le joueur est gagnant, son score total est incrémenté  de 1 point
l : le joueur est perdant, son score n'est pas actualisé et il est éliminé de la compétition.
t : la partie est nulle, les deux adversaires remportent 0.5 points
```sh
Entrez le score de ce joueur [ w = WIN / l = LOO / t = TIE]
```

Le code respecte le style PEP8 afin d'être plus maintenable. Un rapport flake 8 est disponible en ouvrant le dossier flake-report et en ouvrant le fichier index.html dans un navigateur.







