"""
Jeu du Motus
Bienvenue dans le jeu du Motus, les règes sont simples :
Un mot de 6 lettres va apparaître à l'écran, vous devez le deviner
Pour cela, vous devez citer des mots inscrits dans le dictionnaire français
Si une lettre de votre mot est à la bonne place, elle s'affichera en rouge
Si une lettre de votre mot est bonne mais à la mauvaise place, elle s'affichera en Jaune
Sinon, elle s'affichera en Bleu
Le but du jeu est de retrouver le mot de 6 lettres choisi aléatoirement par l'ordinateur
Bonne Chance !
"""
#J'importe toutes les bibliothèques dont je vais avoir besoin
import random
from colorama import init
init()
from colorama import Fore, Back, Style
import time

#L'ordinateur choisit aléatoirement un mot de 6 lettres parmis une liste prédéfinis
choix = ["destin", "joyeux", "kayaks", "hockey", "pyjama", "bijoux", "huskys", "zigzag", "viking", "fuyiez", "vivrez"]            

#Fonction qui choisit aléatoirement
solution = random.choice(choix) 

#Ma fonction play qui définit tout mon jeu principal
def play():
    #On dispose de 8 tentatives, j'initialise des variables qui me serviront plus loin dans mon code
    tentatives = 8
    affichage = ""
    lettres_trouvees = ""

#Pour chaque lettres (6) présentes dans mon mot, je remplace une lettre par un '_' et je l'affiche
    for l in solution:
        affichage = affichage + "_ "
    print (affichage)

#Debut du jeu pour l'utilisateur

    print("\n>> Bienvenue dans l'émission 'Motus' ! <<")

#Tant que les tentatives ne sont pas tombées à 0, on continue

    while tentatives > 0:
      print("\nMot à deviner : ", affichage)
      proposition = input("proposez une lettre : ")[0:1].lower()
    
      if proposition in solution:
          lettres_trouvees = lettres_trouvees + proposition
          print("-> Bien vu!")
      else:
        tentatives = tentatives - 1
        print("-> Non\n")
        if tentatives > 5:
            print("Il vous reste", tentatives, "tentatives")
        else:
            print(Fore.RED + "ATTENTION ! Il ne vous reste plus que", tentatives , "tentatives", end =" ")
    
      affichage = ""
      for x in solution:
          if x in lettres_trouvees:
              affichage += x + " "
          else:
              affichage += "_ "
    
      if "_" not in affichage:
          print(Fore.YELLOW + ">>> Gagné! <<<", end=" ")
          break
    
    print(Fore.RED + "\n    * Fin de la partie *    ", end=" ")


#Ma fonction consulter qui me permet de voir les mots inscrits dans ma liste prédéfinis
def consulter():
    print("\nVoici la liste des mots :", choix)

#Ma fonction qui ajoute un mot à la liste de base
def ajouter():
    votremot = input("\nQuel est le mot que vous souhaitez ajouter ? : ")
    if len(votremot) == 6:
        choix.append(votremot)
        print("\nVoici la nouvelle liste de mots : ", choix)
        time.sleep(2)
        menu()
    else:
        print("\nVous devez entrer un mot de 6 lettres")

#Ma fonction qui permet de supprimer un mot
def supprimer():
    print(choix)
    lequel = int(input("\nQuel mot voulez-vous supprimer (Utilisez le pavé numérique): "))
    if lequel == 1 : 
        choix.pop(0)
        print("\nTrès bien, votre mot a été supprimer")
    elif lequel == 2: 
        choix.pop(1)
        print("\nTrès bien, votre mot a été supprimer")
    elif lequel == 3: 
        choix.pop(2)
        print("\nTrès bien, votre mot a été supprimer")
    elif lequel == 4: 
        choix.pop(3)
        print("\nTrès bien, votre mot a été supprimer")
    elif lequel == 5: 
        choix.pop(4)
        print("\nTrès bien, votre mot a été supprimer")
    elif lequel == 6: 
        choix.pop(5)
        print("\nTrès bien, votre mot a été supprimer")
    elif lequel == 7: 
        choix.pop(6)
        print("\nTrès bien, votre mot a été supprimer")
    elif lequel == 8: 
        choix.pop(7)
        print("\nTrès bien, votre mot a été supprimer")
    elif lequel == 9: 
        choix.pop(8)
        print("\nTrès bien, votre mot a été supprimer")
    elif lequel == 10: 
        choix.pop(9)
        print("\nTrès bien, votre mot a été supprimer")
    elif lequel == 11: 
        choix.pop(10)
        print("\nTrès bien, votre mot a été supprimer")
    else:
        print("\nVous devez saisir un numéro valide")
    menu()

#Je définis une fonction menu qui me permet de soit jouer au jeu, soit consulter la liste de mots
def menu():
    print("\nBienvenue, que voulez-vous faire ?")
    time.sleep(1)
    print("\nChoix 1 : Jouer au jeu")
    time.sleep(1)
    print("\nChoix 2 : Consulter la liste de mots")
    time.sleep(1)
    print("\nChoix 3 : Ajouter un mot")
    time.sleep(1)
    print("\nChoix 4 : Supprimer un mot de la liste")
    utilisateur_choix = int(input("\nVotre choix (1, 2, 3 ou 4) : "))
    if utilisateur_choix == 1:
        play()
    elif utilisateur_choix == 2:
        consulter()
    elif utilisateur_choix == 3:
        ajouter()
    elif utilisateur_choix == 4:
        supprimer()
    else:
        print("merci d'entrer une valeur disponible !")
        menu()

#Je n'ai pas réussis à comparer un mot à un autre lettre par lettre
"""
monmot = "monmot"
monautremot = "autres"
if monmot == monautremot:
    print("Les 2 mots sont identiques")
else:
    print("Les 2 mots sont différents")
"""

menu()
input()