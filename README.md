# TesteMotDePasse

J'ai cree pour mon tout premier programme un testeur de solidite de mot de passe avec les mots de passe simples ainsi que le calcul de temps necessaire.


## Comment il marche

Le programme prend comme entree ton mot de passe puis verifie si il continet qqch. Regarde si le mot de passe est dans ceux simples et si c'est le cas il renvoie directement que le mot de passe n'est pas du tout securise et qu'il faut le changer tout de suite.
J'ai laisse Bolt genere un site web avec mon code phyton, j'ai égallemnet verifie avec une inteligence artificielle (arena.ai, agent mode) si il n'envoyait pas les mots de passe sur serveurs etc, elle m'a répondu que ce n'était pas le cas : https://password-strength-te-vadz.bolt.host

### Comment lancer

Il faut avoir Pyhton 3

puis le lancer avec : python [TesteMotDePasse.py](http://TesteMotDePasse.py) 

Ensuite faut mettre le mot de passe sinon, il regarde quels types de caractères sont utilisés (minuscules, majuscules, chiffres, symboles) pour connaitre la taille de l'alphabet, puis calcule le nombre de combinaisons possibles et divise par 10 milliards d'essais par seconde.

### Ce que j'ai appris

Mettre mes connaisances appris theorique dans de la pratique
La vitesse des hackeurs et commnet calculer temps pour mot de passe
A appeler mes fonctions crees
La correction de bugs (exemple s dans lettre(s) et mot(s) que j'oubliais...

### Amelioration

Accents pas pris comptes
Programme plante si + 180 caracteres 
Fautes orthographes

### Message Fin

J'espere avoir des retours si possible
