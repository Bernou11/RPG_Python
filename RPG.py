import os
import sys
import random
import csv



class Personnage():
    def __init__(self, nom, sexe, pdv, dmg, classe):
        self.nom = nom
        self.sexe = sexe
        self.pdv = str(pdv)
        self.dmg = str(dmg)
        self.classe = classe

ennemie1 = Personnage("Dracula", "M", 30, 5, "Vampire")
ennemie2 = Personnage("Miss Pacman", "F", 25, 3, "Boule jaune")
ennemie3 = Personnage("StarFox", "M", 20, 6, "Renard")

def lireCSV():
    with open('Save.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def firstSave(ennemie1, ennemie2, ennemie3, perso):
    with open('Save.csv', 'w', newline='') as file:  
        writer = csv.writer(file)
        writer.writerow(["nom", "sexe", "pdv", "dmg", "classe"])
        writer.writerow([ennemie1.nom, ennemie1.sexe, ennemie1.pdv, ennemie1.dmg, ennemie1.classe])
        writer.writerow([ennemie2.nom, ennemie2.sexe, ennemie2.pdv, ennemie2.dmg, ennemie2.classe])
        writer.writerow([ennemie3.nom, ennemie3.sexe, ennemie3.pdv, ennemie3.dmg, ennemie3.classe])
        writer.writerow([perso.nom, perso.sexe, perso.pdv, perso.dmg, perso.classe])

nom = input("Choisissez le nom de votre personnage: ")
sexe = input("Choisissez le sexe de votre personnage (F pour femme et H pour homme): ")
if sexe == "H" or sexe == "F" or sexe == "h" or sexe == "f":
    classe = int(input("Choisissez votre classe (1 = guerrier, 2 = mage ou 3 = archer): "))
    if classe == 1: 
        perso = Personnage(nom, sexe, 50, 8, "Guerrier")               
    elif classe == 2:
        perso = Personnage(nom, sexe, 25, 16, "Mage")
    elif classe == 3:
        perso = Personnage(nom, sexe, 35, 13, "Archer")
    else:
        print("Valeur invalide, veuillez relancer le programme")
else:
    print("Valeur invalide, veuillez relancer le programme")

def attaque_guerrier(ennemis_restant):
    if perso.classe == "Guerrier":       
        attaque = int(input("Quel ennemi voulez vous attaquer? (1 pour Dracula, 2 pour Miss Pacman, 3 pour Starfox)\n"))
        if attaque == 1:
            if int(ennemie1.pdv) <= 0:
                print("Dracula est déjà mort, visez un autre ennemi!")   
                attaque_guerrier()                 
            elif int(ennemie1.pdv) > 0:
                ennemie1.pdv = int(ennemie1.pdv) - 8
                print("Vous infligez 8 dégâts à Dracula!\nIl lui reste encore",ennemie1.pdv,"points de vie")          
                if int(ennemie1.pdv) <= 0:
                    print("Bravo vous avez tué Dracula!")
                    ennemis_restant -= 1

        elif attaque == 2:
            if int(ennemie2.pdv) <= 0:
                print("Miss Pacman est déjà morte, visez un autre ennemi!")
                attaque_guerrier()
            elif int(ennemie2.pdv) > 0:
                ennemie2.pdv = int(ennemie2.pdv) - 8
                print("Vous infligez 8 dégâts à Miss Pacman!\nIl lui reste encore:",ennemie2.pdv,"points de vie")
                if int(ennemie2.pdv) <= 0:
                    print("Bravo vous avez tué Miss Pacman!")
                    ennemis_restant -= 1

        elif attaque == 3:
            if int(ennemie3.pdv) <= 0:
                print("Starfox est déjà mort, visez un autre ennemi!")
                attaque_guerrier()
            elif int(ennemie3.pdv) > 0:
                ennemie3.pdv = int(ennemie3.pdv) - 8
                print("Vous infligez 8 dégâts à Starfox!\nIl lui reste encore:",ennemie3.pdv,"points de vie")
                if int(ennemie3.pdv) <= 0:
                    print("Bravo vous avez tué Starfox!")
                    ennemis_restant -= 1                      

def attaque_mage(ennemis_restant):
    if perso.classe == "Mage":
        attaque = int(input("Quel ennemi voulez vous attaquer? (1 pour Dracula, 2 pour Miss Pacman, 3 pour Starfox)\n"))
        if attaque == 1:
            if int(ennemie1.pdv) <= 0:
                print("Dracula est déjà mort, visez un autre ennemi!")
                attaque_mage()
            elif int(ennemie1.pdv) > 0:
                ennemie1.pdv = int(ennemie1.pdv) - 16
                print("Vous infligez 16 dégâts à Dracula!\nIl lui reste encore:",ennemie1.pdv,"points de vie")
                if int(ennemie1.pdv) <= 0:
                    print("Bravo vous avez tué Dracula!")
                    ennemis_restant -= 1
        elif attaque == 2:
            if int(ennemie2.pdv) <= 0:
                print("Miss Pacman est déjà morte, visez un autre ennemi!")
                attaque_mage()
            elif int(ennemie2.pdv) > 0:
                ennemie2.pdv = int(ennemie2.pdv) - 16
                print("Vous infligez 16 dégâts à Miss Pacman!\nIl lui reste encore:",ennemie2.pdv,"points de vie")
                if int(ennemie2.pdv) <= 0:
                    print("Bravo vous avez tué Miss Pacman!")
                    ennemis_restant -= 1
        elif attaque == 3:
            if int(ennemie3.pdv) <= 0:
                print("Starfox est déjà mort, visez un autre ennemi!")
            elif int(ennemie3.pdv) > 0:
                ennemie3.pdv = int(ennemie3.pdv) - 16
                print("Vous infligez 16 dégâts à Starfox!\nIl lui reste encore:",ennemie3.pdv,"points de vie")
                if int(ennemie3.pdv) <= 0:
                    print("Bravo vous avez tué Starfox!")
                    ennemis_restant -= 1               

def attaque_archer(ennemis_restant):
    if classe == "Archer": 
        attaque = int(input("Quel ennemi voulez vous attaquer? (1 pour Dracula, 2 pour Miss Pacman, 3 pour Starfox)\n"))
        if attaque == 1:
            if int(ennemie1.pdv) <= 0:
                print("Dracula est déjà mort, visez un autre ennemi!")
                attaque_archer()
            elif int(ennemie1.pdv) > 0:
                ennemie1.pdv = int(ennemie1.pdv) - 13
                print("Vous infligez 13 dégâts à Dracula!\nIl lui reste encore:",ennemie1.pdv,"points de vie")
                if int(ennemie1.pdv) <= 0:
                    print("Bravo vous avez tué Dracula!")
                    ennemis_restant -= 1
        elif attaque == 2:
            if int(ennemie2.pdv) <= 0:
                print("Miss Pacman est déjà morte, visez un autre ennemi!")
                attaque_archer()
            elif int(ennemie2.pdv) > 0:
                ennemie2.pdv = int(ennemie2.pdv) - 13
                print("Vous infligez 13 dégâts à Dracula!\nIl lui reste encore:", ennemie2.pdv,"points de vie")
                if int(ennemie2.pdv) <= 0:
                    print("Bravo vous avez tué Miss Pacman!")
                    ennemis_restant -= 1
        elif attaque == 3:
            if int(ennemie3.pdv) <= 0:
                print("Starfox est déjà mort, visez un autre ennemi!")
            elif int(ennemie3.pdv) > 0:
                ennemie3.pdv = int(ennemie3.pdv) - 13
                print("Vous infligez 13 dégâts à Starfox!\nIl lui reste encore:",ennemie3.pdv,"points de vie")
                if int(ennemie3.pdv) <= 0:
                    print("Bravo vous avez tué Starfox!")
                    ennemis_restant -= 1               

def tour_ennemis(ennemis_restant):                    

    action_ennemie = [1, 2]
    if int(perso.pdv) > 0 and ennemis_restant > 0:
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


firstSave(ennemie1, ennemie2, ennemie3, perso)

ennemis_restant = 3
potion = 1
pv_perdus = 0
while int(perso.pdv) > 0 or int(ennemie1.pdv) > 0 and int(ennemie2.pdv) > 0 and int(ennemie3.pdv) > 0:
    print('Votre tour!\n')
    if potion == 1:
        action = int(input("Voulez vous attaquer ou vous soigner? (1 pour attaquer; 2 pour vous soigner)\n"))
        if action == 1:
            attaque_guerrier(ennemis_restant)
            attaque_mage(ennemis_restant)
            attaque_archer(ennemis_restant)
        elif action == 2:
            if potion == 1: 
                perso.pdv = int(perso.pdv) + 15
                print('Vous avez maintenant',perso.pdv,"points de vie")
                potion -= 1
    else:
        print("Vous n'avez plus de potion, vous devez donc attaquer")
        attaque_guerrier(ennemis_restant)
        attaque_mage(ennemis_restant)
        attaque_archer(ennemis_restant)            
    print('\n')

    print('Tour ennemi!\n')
    tour_ennemis(ennemis_restant)

    with open('Save.csv', 'w', newline='') as file:  
        writer = csv.writer(file)
        writer.writerow(["nom", "sexe", "pdv", "dmg", "classe"])
        writer.writerow([ennemie1.nom, ennemie1.sexe, ennemie1.pdv, ennemie1.dmg, ennemie1.classe])
        writer.writerow([ennemie2.nom, ennemie2.sexe, ennemie2.pdv, ennemie2.dmg, ennemie2.classe])
        writer.writerow([ennemie3.nom, ennemie3.sexe, ennemie3.pdv, ennemie3.dmg, ennemie3.classe])
        writer.writerow([perso.nom, perso.sexe, perso.pdv, perso.dmg, perso.classe])

    if int(perso.pdv) <= 0:
        print('Dommage vous avez perdu :(')
        break
    elif int(ennemie1.pdv) <= 0 and int(ennemie2.pdv) <= 0 and int(ennemie3.pdv) <= 0:
        print('Bravo vous avez gagné!')
        break