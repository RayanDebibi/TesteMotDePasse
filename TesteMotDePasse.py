etape_1 = 0
vitesse_hackeur = 10 ** 10
lettres_miniscules = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lettres_majuscules = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symboles = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]
mot_de_passe_simples = ["123456", "123456789", "000000", "12345678", "111111", "azerty", "azertyuiop", "qsdfgh", "azerty123", "motdepasse", "password", "admin", "soleil", "marseille", "chouchou", "doudou", "loulou", "bonjour", "secret"]


def dire_quel_mot_de_passe():
    print("Rentre un mot de passe pour le tester")
    mot_de_passe = str(input())
    return mot_de_passe

def si_mot_de_passe_existe(mot_de_passe):
    if len(mot_de_passe) == 0:
        print("Verifie ton mot de passe stp")

def si_mot_de_passe_simple(mot_de_passe):
    for mot_de_passe_simple in mot_de_passe_simples:
        if mot_de_passe_simple == mot_de_passe:
            print("Ta securite est a risque, change tout de suite ton mot de passe")
            exit()

def calcul_1_etape(mot_de_passe):
    etape_1 = 0
    for lettre_miniscule in lettre_miniscules:
        if lettre_miniscule in mot_de_passe:
            etape_1 += len(lettre_miniscules)
            break
    for lettre_majuscule in lettre_majuscules:
        if lettre_majuscule in mot_de_passe:
            etape_1 += len(lettres_majuscules)
            break
    for chiffre in chiffres:       
        if chiffre in mot_de_passe:
            etape_1 += len(chiffres)
            break
    for symbole in symboles:
        if symbole in mot_de_passe:
            etape_1 += len(symboles)
            break
    return etape_1
def calcul_longueur(mot_de_passe):
    longueur_mot_de_passe = len(mot_de_passe)
    return longueur_mot_de_passe
def calcul_nombre_possibilites_requises(etape_1, longueur_mot_de_passe):
    nbr_possibilites = etape_1 ** longueur_mot_de_passe
    return nbr_possibilites
def calcul_temps_requis(nbr_possibilites,vitesse_hackeur):
    secondes = nbr_possibilites / vitesse_hackeur
    return secondes
def convertis_temps(secondes):
    minutes = secondes / 60
    heures = minutes / 60
    jours = heures / 24
    semaines = jours / 7
    mois = semaines / 4
    annees = mois / 12
    siecles = annees / 100
    return minutes, heures, jours, semaines, mois, annees, siecles
def message_temps(secondes,minutes,heures,jours,semaines,mois,annees,siecles,vitesse_hackeur):
    print(f'Ton mot de passe prend {secondes} secondes ou {minutes} minutes ou {heures} heures ou {jours} jours ou {semaines} semaines ou {mois} mois ou {annees} annees ou {siecles} siecles a etre hacke par force brute a une vitesse de {vitesse_hackeur} essais par secondes')
def message_final(siecles):
    if siecles > 10:
        print("Ton mot de passe est parfait:)")
    elif siecles > 1.5:
        print("Ton mot de passe est assez bien mais je te conseille de l'ameliorer:)")
    else: 
        print("Ton mot de passe n'est pas du tout securise, change le tout de suite pour ta securite")
              
    
