"""
Auteur: [#########]
Date: 23/10/2020
"""

import time, re # Importe le module time (gestion du temps et des dates) et re (Gestion des expréssions régulières)

# Déclaration de la fonction du compteur (EX: 1)
def compteur1():
    # Définitions des variables
    pause = 0.5
    compteur = 0

    # Définition de la boucle
    while True:
        print(compteur)   # On affiche le nombre compté
        compteur += 1     # On incrémente le compteur de 1 pour la prochaine itération de la boucle
        time.sleep(pause)  # On stoppe le code pendant pause = 0.5s


# Déclaration de la variable du décompteur (EX: 2)
def decompteur2():
    # Définition des variables
    pause = 0.5
    compteur = 9

    # Définition de la boucle
    while compteur >= 0:  # Boucle tant que compteur >= 0
        print(compteur)   # Affiche le nombre décrémenté
        compteur -= 1     # Décrémente le compteur de 1 pour la prochaine itération de la boucle
        time.sleep(pause)  # On stoppe le code pendant pause = 0.5s
    print("Terminé !")   # Affiche "Terminé !" à la fin de l'exécution de la boucle

# Déclaration de la variable du compteur deux digit (EX: 3)
def compteur3():
    # Définition des variables
    pause = 0.5
    compteur_dizaine = 0
    compteur_unites = 0

    while compteur_dizaine < 6:  # Boucle tant que le compteur n'est pas à 60
        # Affiche les deux digits incrémentées en un nombre
        print(str(compteur_dizaine) + str(compteur_unites))
        compteur_unites += 1  # Incrémente les unitées de 1
        if compteur_unites > 9:  # Si les unités dépassent 9
            compteur_dizaine += 1  # Incrémenter les dizaines
            compteur_unites = 0   # Mettre les unités à 0
        time.sleep(pause)  # Stoppe le code pendant pause = 0.5s

# Déclaration de la variable du compteur Minutes : Secondes (EX: 4)
def compteur4(vitesse = 1): # Par défaut, la vitesse est un ratio 1:1 pour une seconde, une incrémentation.
    # Définition des variables
    u_secondes = 0
    d_secondes = 0
    u_minutes = 0
    d_minutes = 0

    # Définition de la boucle
    while d_minutes < 6:  # Boucle tant que le compteur n'atteint pas une heure.
        # Affiche le compteur sous la forme 00:00
        print(f"{d_minutes}{u_minutes}:{d_secondes}{u_secondes}")
        u_secondes += 1  # Incrémente les secondes de 1
        # Les conditions changent le compteur en fonction des unités
        if u_secondes > 9:
            u_secondes = 0
            d_secondes += 1
        if d_secondes > 5:
            d_secondes = 0
            u_minutes += 1
        if u_minutes > 9:
            u_minutes = 0
            d_minutes += 1
        time.sleep(vitesse) # On attend X secondes où X est la vitesse définie lors de l'appel de la fonction

# Déclaration de la fonction du décompteur de minutes/secondes (EX: 5)
def decompteur5(vitesse = 1): # Par défaut, la vitesse est un ratio 1:1 pour une seconde, une décrémentation.
    temps = input("Temps (00:00)> ") # Demande le temps à l'utilisateur
    if not(len(temps.split()) == 1): return print("Merci de rentrer une expréssion sous la forme 00:00") # Si l'utilisateur donne une valeur nulle ou plus que demandée
    regex = re.compile("^(\d{1,2}(?!\d):?){2,3}$") # Défini comme expréssion régulière l'expréssion ^(\d{1,2}(?!\d):?){2,3}$ qui vérifie l'existance d'une chaine de charactère sous la forme 00:00
    if (regex.match(temps) == None): return print("Merci de rentrer une expréssion sous la forme 00:00") # Si la valeur ne comprend pas une expréssion sous la forme 00:00
    # Définition des variables
    minutes = int(temps.split(":")[0])
    secondes = int(temps.split(":")[1])
    # Conversion en integer

    while minutes + secondes > 0: # Boucle tant que le compteur n'est pas à 00:00
        print(f"{0 if minutes < 10 else ''}{minutes}:{0 if secondes < 10 else ''}{secondes}") # Affiche le décompte
        secondes -= 1 # Décrémente le compteur d'une seconde
        # Les conditions changent le compteur en fonction des unités
        if secondes < 0 and minutes > 0:
            secondes = 59
            minutes -= 1
        time.sleep(vitesse) # On attend X secondes où X est la vitesse définie lors de l'appel de la fonction
    print("00:00") # Affiche 00:00 à la fin

# Apppel des fonctions
# compteur1()   Affiche 0, 1, 2, 3 ... jusqu'à l'infini à mesure de x + 1 / 0.5s
# decompteur2() Affiche 9, 8, 7, 6 ... jusqu'à 0 suivis de "Terminé" à mesure de x - 1 / 0.5s
# compteur3()   Affiche 00, 01, 02 ... jusqu'à 59 à mesure de unités + 1 / 0.5s et dizaines + 1 / 5s
# compteur4()   Affiche 00:00, 00:01 ... jusqu'à 59:59 à un ratio de vitesse:1 (Incrémentation toutes les [vitesse] secondes)
# decompteur5() Affiche depuis le nombre choisit par l'utilisateur jusqu'à 00:00 à un ratio de vitesse:1 (Décrémentation toutes les [vitesse] secondes)
