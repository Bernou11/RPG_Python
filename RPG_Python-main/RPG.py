from ast import dump
import os
import sys
import random
import csv
import pickle



class Personnage():
    def __init__(self, nom, sexe, pdv, dmg, classe, potion, vivant):
        self.nom = nom
        self.sexe = sexe
        self.pdv = str(pdv)
        self.dmg = str(dmg)
        self.classe = classe
        self.potion = potion
        self.vivant = vivant

ennemie1 = Personnage("Dracula", "M", 30, 5, "Vampire", "Non", "Oui")
ennemie2 = Personnage("Miss Pacman", "F", 25, 3, "Boule jaune","Non", "Oui")
ennemie3 = Personnage("StarFox", "M", 20, 6, "Renard","Non", "Oui")

def lireCSV():
    with open('Save.csv', 'r+') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def firstSave(ennemie1, ennemie2, ennemie3, perso):
    with open('Save.csv', 'w+', newline='') as file:  
        writer = csv.writer(file)
        writer.writerow(["Nom", "Sexe", "Pdv", "Dmg", "Classe", "Vivant"])
        writer.writerow([ennemie1.nom, ennemie1.sexe, ennemie1.pdv, ennemie1.dmg, ennemie1.classe, ennemie1.vivant])
        writer.writerow([ennemie2.nom, ennemie2.sexe, ennemie2.pdv, ennemie2.dmg, ennemie2.classe, ennemie2.vivant])
        writer.writerow([ennemie3.nom, ennemie3.sexe, ennemie3.pdv, ennemie3.dmg, ennemie3.classe, ennemie3.vivant])
        writer.writerow([perso.nom, perso.sexe, perso.pdv, perso.dmg, perso.classe, perso.potion])

def attaques():
    attaque = int(input("Quel ennemi voulez vous attaquer? (1 pour Dracula, 2 pour Miss Pacman, 3 pour Starfox)\n"))
    if attaque == 1 and perso.classe == "Guerrier":
        if int(ennemie1.pdv) <= 0:
            print("Dracula est déjà mort, visez un autre ennemi!")   
            attaques()                 
        elif int(ennemie1.pdv) > 0:
                ennemie1.pdv = int(ennemie1.pdv) - 8
                print("Vous infligez 8 dégâts à Dracula!\nIl lui reste encore",ennemie1.pdv,"points de vie")          
                if int(ennemie1.pdv) <= 0:
                    print("Bravo vous avez tué Dracula!")
                    ennemie1.vivant = "Non"
    elif attaque == 2 and perso.classe == "Guerrier":
        if int(ennemie2.pdv) <= 0:
            print("Miss Pacman est déjà morte, visez un autre ennemi!")
            attaques()
        elif int(ennemie2.pdv) > 0:
            ennemie2.pdv = int(ennemie2.pdv) - 8
            print("Vous infligez 8 dégâts à Miss Pacman!\nIl lui reste encore:",ennemie2.pdv,"points de vie")
            if int(ennemie2.pdv) <= 0:
                print("Bravo vous avez tué Miss Pacman!")
                ennemie2.vivant = "Non"
    elif attaque == 3 and perso.classe == "Guerrier":
        if int(ennemie3.pdv) <= 0:
            print("Starfox est déjà mort, visez un autre ennemi!")
            attaques()
        elif int(ennemie3.pdv) > 0:
            ennemie3.pdv = int(ennemie3.pdv) - 8
            print("Vous infligez 8 dégâts à Starfox!\nIl lui reste encore:",ennemie3.pdv,"points de vie")
            if int(ennemie3.pdv) <= 0:
                print("Bravo vous avez tué Starfox!")
                ennemie3.vivant = "Non"                      
    elif attaque == 1 and perso.classe == "Mage":
        if int(ennemie1.pdv) <= 0:
            print("Dracula est déjà mort, visez un autre ennemi!")
            attaques()
        elif int(ennemie1.pdv) > 0:
            ennemie1.pdv = int(ennemie1.pdv) - 16
            print("Vous infligez 16 dégâts à Dracula!\nIl lui reste ",ennemie1.pdv,"points de vie")
            if int(ennemie1.pdv) <= 0:
                print("Bravo vous avez tué Dracula!")
                ennemie1.vivant = "Non"
    elif attaque == 2 and perso.classe == "Mage":
        if int(ennemie2.pdv) <= 0:
            print("Miss Pacman est déjà morte, visez un autre ennemi!")
            attaques()
        elif int(ennemie2.pdv) > 0:
            ennemie2.pdv = int(ennemie2.pdv) - 16
            print("Vous infligez 16 dégâts à Miss Pacman!\nIl lui reste ",ennemie2.pdv,"points de vie")
            if int(ennemie2.pdv) <= 0:
                print("Bravo vous avez tué Miss Pacman!")
                ennemie2.vivant = "Non"
    elif attaque == 3 and perso.classe == "Mage":
        if int(ennemie3.pdv) <= 0:
            print("Starfox est déjà mort, visez un autre ennemi!")
            attaques()
        elif int(ennemie3.pdv) > 0:
            ennemie3.pdv = int(ennemie3.pdv) - 16
            print("Vous infligez 16 dégâts à Starfox!\nIl lui reste ",ennemie3.pdv,"points de vie")
            if int(ennemie3.pdv) <= 0:
                print("Bravo vous avez tué Starfox!")
                ennemie3.vivant = "Non"  
    elif attaque == 1 and perso.classe == "Archer":
        if int(ennemie1.pdv) <= 0:
            print("Dracula est déjà mort, visez un autre ennemi!")
            attaques()
        elif int(ennemie1.pdv) > 0:
            ennemie1.pdv = int(ennemie1.pdv) - 13
            print("Vous infligez 13 dégâts à Dracula!\nIl lui reste ",ennemie1.pdv,"points de vie")
            if int(ennemie1.pdv) <= 0:
                print("Bravo vous avez tué Dracula!")
                ennemie1.vivant = "Non"
    elif attaque == 2 and perso.classe == "Archer":
        if int(ennemie2.pdv) <= 0:
            print("Miss Pacman est déjà morte, visez un autre ennemi!")
            attaques()
        elif int(ennemie2.pdv) > 0:
            ennemie2.pdv = int(ennemie2.pdv) - 13
            print("Vous infligez 13 dégâts à Dracula!\nIl lui reste ", ennemie2.pdv,"points de vie")
            if int(ennemie2.pdv) <= 0:
                print("Bravo vous avez tué Miss Pacman!")
                ennemie2.vivant = "Non"
    elif attaque == 3 and perso.classe == "Archer":
        if int(ennemie3.pdv) <= 0:
            print("Starfox est déjà mort, visez un autre ennemi!")
            attaques()
        elif int(ennemie3.pdv) > 0:
            ennemie3.pdv = int(ennemie3.pdv) - 13
            print("Vous infligez 13 dégâts à Starfox!\nIl lui reste ",ennemie3.pdv,"points de vie")
            if int(ennemie3.pdv) <= 0:
                print("Bravo vous avez tué Starfox!")
                ennemie3.vivant = "Non"

def tour_ennemis():                    
    action_ennemie = [1, 2]
    if int(perso.pdv) > 0 and ennemie1.vivant == "Oui" or ennemie2.vivant == "Oui" or ennemie3.vivant == "Oui":
        print('Tour ennemi!\n')
        choix_action_ennemie = random.choice(action_ennemie)
        if choix_action_ennemie == 1 and int(ennemie1.pdv) > 0:
            perso.pdv = int(perso.pdv) - 5
            print("Dracula vous inflige 5 points de dégats!\nIl vous reste ", perso.pdv, " points de vie\n")
        elif choix_action_ennemie == 2 and int(ennemie1.pdv) > 0:
            print("Dracula passe son tour\n")
        choix_action_ennemie = random.choice(action_ennemie)
        if choix_action_ennemie == 1 and int(ennemie2.pdv) > 0:
            perso.pdv = int(perso.pdv) - 3
            print("Miss Pacman vous inflige 3 dégats!\nIl vous reste ", perso.pdv, " points de vie\n")                  
        elif choix_action_ennemie == 2 and int(ennemie2.pdv) > 0:
            print("Miss Pacman passe son tour\n")
        choix_action_ennemie = random.choice(action_ennemie)
        if choix_action_ennemie == 1 and int(ennemie3.pdv) > 0:
            perso.pdv = int(perso.pdv) - 6
            print("Starfox vous inflige 6 points de dommage! \n Il vous reste ",perso.pdv,"points de vie\n")
        elif choix_action_ennemie == 2 and int(ennemie3.pdv) > 0:
            print("Starfox passe son tour\n")

def crea_perso():
    sexe = input("Choisissez le sexe de votre personnage (F pour femme et H pour homme): ")
    if sexe == "H" or sexe == "F" or sexe == "h" or sexe == "f":
        def crea_perso_classe():
            classe = int(input("Choisissez votre classe (1 = guerrier, 2 = mage ou 3 = archer): "))
            if classe == 1: 
                perso = Personnage(nom, sexe, 50, 8, "Guerrier","Oui", "Oui")
                with open("sauvegarde", "wb") as save:
                    pickle.dump(perso, save) 
                    pickle.dump(ennemie1, save)
                    pickle.dump(ennemie2, save)
                    pickle.dump(ennemie3, save)              
            elif classe == 2:
                perso = Personnage(nom, sexe, 25, 16, "Mage",'Oui', "Oui")
                with open("sauvegarde", "wb") as save:
                    pickle.dump(perso, save) 
                    pickle.dump(ennemie1, save)
                    pickle.dump(ennemie2, save)
                    pickle.dump(ennemie3, save)  
            elif classe == 3:
                perso = Personnage(nom, sexe, 35, 13, "Archer",'Oui', "Oui")
                with open("sauvegarde", "wb") as save:
                    pickle.dump(perso, save) 
                    pickle.dump(ennemie1, save)
                    pickle.dump(ennemie2, save)
                    pickle.dump(ennemie3, save)       
            else:
                print("Veuillez choisir entre 1, 2 et 3")
                crea_perso_classe()
            firstSave(ennemie1, ennemie2, ennemie3, perso)        
        crea_perso_classe()          
    else:
        print("Veuillez choisir entre h ou f")
        crea_perso()

def partie():
    if perso.potion == "Oui":
        action = int(input("Voulez vous attaquer ou vous soigner? (1 pour attaquer; 2 pour vous soigner)\n"))
        if action == 1:
            attaques()
        elif action == 2:
            perso.pdv = int(perso.pdv) + 15
            print('Vous avez maintenant',perso.pdv,"points de vie")
            perso.potion = "Non"
        else:
            print("Choisissez 1 ou 2")
            partie()
    else:
        print("Vous n'avez plus de potion, vous devez donc attaquer")
        attaques()             
    print('\n')
    tour_ennemis()

potion = 1
if os.path.exists("sauvegarde"):
    with open("sauvegarde", "rb") as save:
        perso = pickle.load(save)
else:
    nom = input("Choisissez le nom de votre personnage: ")  
    crea_perso()
    with open("sauvegarde", "rb") as save:
        perso = pickle.load(save)    
while int(perso.pdv) > 0 or int(ennemie1.pdv) > 0 and int(ennemie2.pdv) > 0 and int(ennemie3.pdv) > 0:
    print('Votre tour!\n')
    partie()
    with open('Save.csv', 'w+', newline='') as file:  
        writer = csv.writer(file)
        writer.writerow(["nom", "sexe", "pdv", "dmg", "classe", "Vivant"])
        writer.writerow([ennemie1.nom, ennemie1.sexe, ennemie1.pdv, ennemie1.dmg, ennemie1.classe, ennemie1.vivant])
        writer.writerow([ennemie2.nom, ennemie2.sexe, ennemie2.pdv, ennemie2.dmg, ennemie2.classe, ennemie2.vivant])
        writer.writerow([ennemie3.nom, ennemie3.sexe, ennemie3.pdv, ennemie3.dmg, ennemie3.classe, ennemie3.vivant])
        writer.writerow([perso.nom, perso.sexe, perso.pdv, perso.dmg, perso.classe, perso.potion])

    if int(perso.pdv) <= 0:
        print('Dommage vous avez perdu :(')
        os.remove("Save.csv")
        os.remove("sauvegarde")
        break
    elif int(ennemie1.pdv) <= 0 and int(ennemie2.pdv) <= 0 and int(ennemie3.pdv) <= 0:
        print('Bravo vous avez gagné!')
        os.remove("Save.csv")
        os.remove("sauvegarde")
        break