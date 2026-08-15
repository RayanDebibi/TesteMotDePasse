# TesteMotDePasse

J'ai créé pour mon tout premier programme un testeur de solidité de mot de passe avec les mots de passe simples ainsi que le calcul de temps nécessaire.

## Comment il marche

Le programme prend comme entrée ton mot de passe puis vérifie s'il contient quelque chose. Il regarde si le mot de passe est dans ceux simples et égallement dans la liste rockyou.txt et si c'est le cas il renvoie directement que le mot de passe n'est pas du tout sécurisé et qu'il faut le changer tout de suite.

Sinon, il regarde quels types de caractères sont utilisés (minuscules, majuscules, chiffres, symboles) pour connaître la taille de l'alphabet, puis calcule le nombre de combinaisons possibles et divise par 10 milliards d'essais par seconde.

Il vérifie aussi que le mot de passe n'utilise pas trop souvent les mêmes caractères. (Il ignore les majuscules et minuscules).

## Le site web

J'ai laissé Bolt générer un site web avec mon code Python : https://password-strength-te-vadz.bolt.host

J'ai fait trois vérifications pour être sûr que le site n'envoie pas les mots de passe :

1. J'ai vérifié avec une intelligence artificielle (arena.ai, agent mode) s'il n'envoyait pas les mots de passe sur des serveurs, elle m'a répondu que ce n'était pas le cas.
2. J'ai essayé le site sans connexion internet (en chargeant le site avant avec internet) et il marchait, donc aucun mot de passe n'est envoyé.
3. Voici aussi le code source JavaScript pour les connaisseurs : https://password-strength-te-vadz.bolt.host/assets/index-BU01N3ND.js

## Comment lancer

Il faut avoir Python 3 et télécharger le fichier rockyou : https://drive.usercontent.google.com/download?id=1emavX129hVevMpIn-WN7eoJ7nNVuH4k7&authuser=0


Puis le lancer avec :

    python TesteMotDePasse.py

Ensuite il faut mettre le mot de passe.

## Ce que j'ai appris

- Mettre mes connaissances théoriques apprises dans de la pratique
- La vitesse des hackeurs et comment calculer le temps pour un mot de passe
- À appeler mes fonctions créées
- La correction de bugs (exemple : le s dans lettre(s) et mot(s) que j'oubliais)

## Améliorations

- Accents pas pris en compte
- Le programme plante si trop de caractere (environ 150+ caractères )

## Message de fin

J'espère avoir des retours si possible.