from ast import dump
import os
import random
import csv
import pickle
from sqlite3 import paramstyle



class Personnage():
    def __init__(self, nom, sexe, pdv, dmg, classe, potion, paralyse, vivant, element_inventaire):
        self.nom = nom
        self.sexe = sexe
        self.pdv = str(pdv)
        self.dmg = str(dmg)
        self.classe = classe
        self.potion = potion
        self.paralyse = paralyse
        self.vivant = vivant
        self.element_inventaire = element_inventaire

ennemie1 = Personnage("Dracula", "M", 30, 5, "Vampire", "Non", "Non", "Oui", 0)
ennemie2 = Personnage("Miss Pacman", "F", 25, 3, "Boule jaune","Non", "Non", "Oui", 0)
ennemie3 = Personnage("StarFox", "M", 20, 6, "Renard","Non", "Non", "Oui", 0)

def lireCSV():
    with open('Save.csv', 'r+') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def firstSave(ennemie1, ennemie2, ennemie3, perso):
    with open('Save.csv', 'w+', newline='') as file:  
        writer = csv.writer(file)      
        writer.writerow(["Nom", "Sexe", "Pdv", "Dmg", "Classe", "Potion", "Paralysie", "Vivant"])
        writer.writerow([ennemie1.nom, ennemie1.sexe, ennemie1.pdv, ennemie1.dmg, ennemie1.classe, ennemie1.potion, ennemie1.paralyse, ennemie1.vivant])
        writer.writerow([ennemie2.nom, ennemie2.sexe, ennemie2.pdv, ennemie2.dmg, ennemie2.classe, ennemie2.potion, ennemie1.paralyse, ennemie2.vivant])
        writer.writerow([ennemie3.nom, ennemie3.sexe, ennemie3.pdv, ennemie3.dmg, ennemie3.classe, ennemie3.potion, ennemie1.paralyse, ennemie3.vivant])
        writer.writerow([perso.nom, perso.sexe, perso.pdv, perso.dmg, perso.classe, perso.potion, ennemie1.paralyse, perso.vivant])

def attaques():
    if perso.paralyse == "Non":
        attaque = int(input("Quel ennemi voulez vous attaquer? (1 pour Dracula, 2 pour Miss Pacman, 3 pour Starfox)\n"))
        if attaque == 1 and perso.classe == "Guerrier":
            if int(ennemie1.pdv) <= 0:
                print("Dracula est déjà mort, visez un autre ennemi!")   
                attaques()                 
            elif int(ennemie1.pdv) > 0:
                    ennemie1.pdv = int(ennemie1.pdv) - 8
                    print("Vous infligez 8 dégâts à Dracula!\nIl lui reste",ennemie1.pdv,"points de vie")
                    with open ("dracula", "wb") as dracula:
                        pickle.dump(ennemie1, dracula)   
                    if int(ennemie1.pdv) <= 0:
                        print("Bravo vous avez tué Dracula! \nVous obtenez une dent de vampire")
                        perso.element_inventaire = perso.element_inventaire + 1
                        ennemie1.vivant = "Non"
                        ennemie1.pdv = 0
                        with open ("dracula", "wb") as dracula:
                            pickle.dump(ennemie1, dracula)
                        with open ("sauvegarde", "wb") as save:
                            pickle.dump(perso, save)
        elif attaque == 2 and perso.classe == "Guerrier":
            if int(ennemie2.pdv) <= 0:
                print("Miss Pacman est déjà morte, visez un autre ennemi!")
                attaques()
            elif int(ennemie2.pdv) > 0:
                ennemie2.pdv = int(ennemie2.pdv) - 8
                print("Vous infligez 8 dégâts à Miss Pacman!\nIl lui reste encore:",ennemie2.pdv,"points de vie")
                with open ("mpacman", "wb") as mpacman:
                    pickle.dump(ennemie2, mpacman)    
                if int(ennemie2.pdv) <= 0:
                    print("Bravo vous avez tué Miss Pacman! \nVous obtenez un citron")
                    perso.element_inventaire = perso.element_inventaire + 1
                    ennemie2.vivant = "Non"
                    ennemie2.pdv = 0
                    with open ("mpacman", "wb") as mpacman:
                        pickle.dump(ennemie2, mpacman)
                    with open ("sauvegarde", "wb") as save:
                        pickle.dump(perso, save)
        elif attaque == 3 and perso.classe == "Guerrier":
            if int(ennemie3.pdv) <= 0:
                print("Starfox est déjà mort, visez un autre ennemi!")
                attaques()
            elif int(ennemie3.pdv) > 0:
                ennemie3.pdv = int(ennemie3.pdv) - 8
                print("Vous infligez 8 dégâts à Starfox!\nIl lui reste encore:",ennemie3.pdv,"points de vie")
                if int(ennemie3.pdv) <= 0:
                    print("Bravo vous avez tué Starfox! \nVous obtenez un poil de renard")
                    perso.element_inventaire = perso.element_inventaire + 1
                    ennemie3.vivant = "Non"
                    ennemie3.pdv = 0
                    with open ("fox", "wb") as fox:
                        pickle.dump(ennemie3, fox)
                    with open ("sauvegarde", "wb") as save:
                        pickle.dump(perso, save) 

        elif attaque == 1 and perso.classe == "Mage":
            if int(ennemie1.pdv) <= 0:
                print("Dracula est déjà mort, visez un autre ennemi!")
                attaques()
            elif int(ennemie1.pdv) > 0:
                ennemie1.pdv = int(ennemie1.pdv) - 16
                print("Vous infligez 16 dégâts à Dracula!\nIl lui reste ",ennemie1.pdv,"points de vie")
                with open ("dracula", "wb") as dracula:
                    pickle.dump(ennemie1, dracula) 
                if int(ennemie1.pdv) <= 0:
                    print("Bravo vous avez tué Dracula! \nVous obtenez une dent de vampire")
                    perso.element_inventaire = perso.element_inventaire + 1
                    ennemie1.vivant = "Non"
                    ennemie1.pdv = 0
                    with open ("dracula", "wb") as dracula:
                        pickle.dump(ennemie1, dracula) 
                    with open ("sauvegarde", "wb") as save:
                        pickle.dump(perso, save)   
        elif attaque == 2 and perso.classe == "Mage":
            if int(ennemie2.pdv) <= 0:
                print("Miss Pacman est déjà morte, visez un autre ennemi!")
                attaques()
            elif int(ennemie2.pdv) > 0:
                ennemie2.pdv = int(ennemie2.pdv) - 16
                print("Vous infligez 16 dégâts à Miss Pacman!\nIl lui reste ",ennemie2.pdv,"points de vie")
                with open ("mpacman", "wb") as mpacman:
                    pickle.dump(ennemie2, mpacman) 
                if int(ennemie2.pdv) <= 0:
                    print("Bravo vous avez tué Miss Pacman! \nVous obtenez un citron")
                    perso.element_inventaire = perso.element_inventaire + 1
                    ennemie2.vivant = "Non"
                    ennemie2.pdv = 0
                    with open ("mpacman", "wb") as mpacman:
                        pickle.dump(ennemie2, mpacman) 
                    with open ("sauvegarde", "wb") as save:
                        pickle.dump(perso, save)    
        elif attaque == 3 and perso.classe == "Mage":
            if int(ennemie3.pdv) <= 0:
                print("Starfox est déjà mort, visez un autre ennemi!")
                attaques()
            elif int(ennemie3.pdv) > 0:
                ennemie3.pdv = int(ennemie3.pdv) - 16
                print("Vous infligez 16 dégâts à Starfox!\nIl lui reste ",ennemie3.pdv,"points de vie")
                with open ("fox", "wb") as fox:
                    pickle.dump(ennemie3, fox) 
                if int(ennemie3.pdv) <= 0:
                    print("Bravo vous avez tué Starfox! \nVous obtenez un poil de renard")
                    perso.element_inventaire = perso.element_inventaire + 1
                    ennemie3.vivant = "Non" 
                    ennemie3.pdv = 0 
                    with open ("fox", "wb") as fox:
                        pickle.dump(ennemie3, fox)
                    with open ("sauvegarde", "wb") as save:
                        pickle.dump(perso, save)

        elif attaque == 1 and perso.classe == "Archer":
            if int(ennemie1.pdv) <= 0:
                print("Dracula est déjà mort, visez un autre ennemi!")
                attaques()
            elif int(ennemie1.pdv) > 0:
                ennemie1.pdv = int(ennemie1.pdv) - 13
                print("Vous infligez 13 dégâts à Dracula!\nIl lui reste ",ennemie1.pdv,"points de vie")
                with open ("dracula", "wb") as dracula:
                    pickle.dump(ennemie1, dracula) 
                if int(ennemie1.pdv) <= 0:
                    print("Bravo vous avez tué Dracula! \nVous obtenez une dent de vampire")
                    perso.element_inventaire = perso.element_inventaire + 1
                    ennemie1.vivant = "Non"
                    ennemie1.pdv = 0
                    with open ("dracula", "wb") as dracula:
                        pickle.dump(ennemie1, dracula) 
                    with open ("sauvegarde", "wb") as save:
                        pickle.dump(perso, save)    
        elif attaque == 2 and perso.classe == "Archer":
            if int(ennemie2.pdv) <= 0:
                print("Miss Pacman est déjà morte, visez un autre ennemi!")
                attaques()
            elif int(ennemie2.pdv) > 0:
                ennemie2.pdv = int(ennemie2.pdv) - 13
                print("Vous infligez 13 dégâts à Dracula!\nIl lui reste ", ennemie2.pdv,"points de vie")
                with open ("mpacman", "wb") as mpacman:
                    pickle.dump(ennemie2, mpacman) 
                if int(ennemie2.pdv) <= 0:
                    print("Bravo vous avez tué Miss Pacman! \nVous obtenez un citron")
                    perso.element_inventaire = perso.element_inventaire + 1
                    ennemie2.vivant = "Non"
                    ennemie2.pdv = 0
                    with open ("mpacman", "wb") as mpacman:
                        pickle.dump(ennemie2, mpacman)
                    with open ("sauvegarde", "wb") as save:
                        pickle.dump(perso, save)    
        elif attaque == 3 and perso.classe == "Archer":
            if int(ennemie3.pdv) <= 0:
                print("Starfox est déjà mort, visez un autre ennemi!")
                attaques()
            elif int(ennemie3.pdv) > 0:
                ennemie3.pdv = int(ennemie3.pdv) - 13
                print("Vous infligez 13 dégâts à Starfox!\nIl lui reste ",ennemie3.pdv,"points de vie")
                with open ("fox", "wb") as fox:
                    pickle.dump(ennemie3, fox)
                if int(ennemie3.pdv) <= 0:
                    print("Bravo vous avez tué Starfox! \nVous obtenez un poil de renard")
                    perso.element_inventaire = perso.element_inventaire + 1
                    ennemie3.vivant = "Non"
                    ennemie3.pdv = 0
                    with open ("fox", "wb") as fox:
                        pickle.dump(ennemie3, fox)
                    with open ("sauvegarde", "wb") as save:
                        pickle.dump(perso, save)    
        elif attaque != 1 or attaque != 2 or attaque != 3:
            print("Choisissez entre 1, 2 ou 3") 
            attaques()  
    else:
        print("Vous avez été paralysé, vous devez donc passer votre tour")
        perso.paralyse = "Non"

def tour_ennemis():                    
    action_ennemie = [1, 2]
    if int(perso.pdv) > 0 and ennemie1.vivant == "Oui" or ennemie2.vivant == "Oui" or ennemie3.vivant == "Oui":
        print('Tour ennemi!\n')
        choix_action_ennemie = random.choice(action_ennemie)
        if choix_action_ennemie == 1 and int(ennemie1.pdv) > 0:
            perso.pdv = int(perso.pdv) - 5
            ennemie1.pdv = int(ennemie1.pdv) + 2
            print("Dracula vous inflige 5 points de dégats et vous vole 2 points de vie!\nIl vous reste ", perso.pdv,"points de vie et ses points de vie remontent à ", ennemie1.pdv,"\n")
        elif choix_action_ennemie == 2 and int(ennemie1.pdv) > 0:
            print("Dracula passe son tour\n")
        choix_action_ennemie = random.choice(action_ennemie)
        para = []
        i = 0
        for i in range(5):
            i += 1
            para.append(i)
        print(para)
        paralysie = random.choice(para)
        print(paralysie)
        if choix_action_ennemie == 1 and int(ennemie3.pdv) > 0:
            if paralysie > 1:
                perso.pdv = int(perso.pdv) - 6
                print("Starfox vous inflige 6 points de dommage!\nIl vous reste ",perso.pdv,"points de vie\n")
            else:
                perso.pdv = int(perso.pdv) - 6
                perso.paralyse = "Oui"
                print("Starfox vous inflige 6 points de dommage!\nIl vous reste ",perso.pdv,"points de vie\n")
                print("Ho non cette attaque vous a paralysé! Vous devrez passer votre prochain tour")
        elif choix_action_ennemie == 2 and int(ennemie3.pdv) > 0:
            print("Starfox passe son tour\n")  
        choix_action_ennemie = random.choice(action_ennemie)
        o_s = []
        j = 0
        for j in range (4):
            j += 1
            o_s.append(j)
        print(o_s)
        os = random.choice(o_s)
        print(os)
        if choix_action_ennemie == 1 and int(ennemie2.pdv) > 0:
            if os == 1 or os == 2 or os == 3 or os == 4:
                print("Pas de chance, Miss Pacman vous a mangé! vous perdez immédiatement la partie! :(")
                perso.pdv = 0
            else:
                perso.pdv = int(perso.pdv) - 3
                print("Miss Pacman vous inflige 3 dégats!\nIl vous reste ", perso.pdv,"points de vie\n")                  
        elif choix_action_ennemie == 2 and int(ennemie2.pdv) > 0:
            print("Miss Pacman passe son tour\n")  
        with open ("sauvegarde", "wb") as save:
            pickle.dump(perso, save)

def crea_perso():
    sexe = input("Choisissez le sexe de votre personnage (F pour femme et H pour homme): ")
    if sexe == "H" or sexe == "F" or sexe == "h" or sexe == "f":
        def crea_perso_classe():
            classe = int(input("Choisissez votre classe (1 = guerrier, 2 = mage ou 3 = archer): "))
            if classe == 1: 
                perso = Personnage(nom, sexe, 50, 8, "Guerrier","Oui", "Non", "Oui", 0)
                with open("sauvegarde", "wb") as save:
                    pickle.dump(perso, save)
                with open("dracula", "wb") as dracula:
                    pickle.dump(ennemie1, dracula)     
                with open("mpacman", "wb") as mpacman:
                    pickle.dump(ennemie2, mpacman)
                with open("fox", "wb") as fox:
                    pickle.dump(ennemie3, fox)                  
            elif classe == 2:
                perso = Personnage(nom, sexe, 25, 16, "Mage",'Oui', "Non", "Oui", 0)
                with open("sauvegarde", "wb") as save:
                    pickle.dump(perso, save) 
                with open("dracula", "wb") as dracula:
                    pickle.dump(ennemie1, dracula)     
                with open("mpacman", "wb") as mpacman:
                    pickle.dump(ennemie2, mpacman)
                with open("fox", "wb") as fox:
                    pickle.dump(ennemie3, fox)  
            elif classe == 3:
                perso = Personnage(nom, sexe, 35, 13, "Archer",'Oui', "Non", "Oui", 0)
                with open("sauvegarde", "wb") as save:
                    pickle.dump(perso, save) 
                with open("dracula", "wb") as dracula:
                    pickle.dump(ennemie1, dracula)     
                with open("mpacman", "wb") as mpacman:
                    pickle.dump(ennemie2, mpacman)
                with open("fox", "wb") as fox:
                    pickle.dump(ennemie3, fox)       
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
            with open ("sauvegarde", "wb") as save:
                pickle.dump(perso, save)
        else:
            print("Choisissez 1 ou 2")
            partie()
    else:
        if perso.element_inventaire == 2:
            craft = input("Bravo vous avez récupéré 2 ressources différentes! Voulez-vous créer une nouvelle potion? (répondre par oui ou non)\n")
            if craft == "oui" or craft == "Oui":
                print("Vous créez une nouvelle potion et continuez la partie!")
                perso.potion = "Oui"
                perso.element_inventaire = 0 
                partie()
            elif craft == "non" or craft == "Non":
                print("Vous ne créez pas de potion")
        print("Vous n'avez plus de potion, vous devez donc attaquer")
        attaques()
    print('\n')
    tour_ennemis()

if os.path.exists("sauvegarde"):
    with open("sauvegarde", "rb") as save:
        perso = pickle.load(save)
        print(perso)
    with open("dracula", "rb") as dracula:
        ennemie1 = pickle.load(dracula)
        print(ennemie1)
    with open("mpacman", "rb") as mpacman:
        ennemie2 = pickle.load(mpacman)
        print(ennemie2)
    with open("fox", "rb") as fox:
        ennemie3 = pickle.load(fox)
        print(ennemie3)
else:
    nom = input("Choisissez le nom de votre personnage: ")  
    crea_perso()
    with open("sauvegarde", "rb") as save:
        perso = pickle.load(save)
while int(perso.pdv) > 0 or int(ennemie1.pdv) > 0 and int(ennemie2.pdv) > 0 and int(ennemie3.pdv) > 0:
    print('Votre tour!\n')
    partie()
    firstSave(ennemie1, ennemie2, ennemie3, perso)

    if int(perso.pdv) <= 0:
        print('Dommage vous avez perdu :(')
        os.remove("Save.csv")
        os.remove("sauvegarde")
        os.remove("dracula")
        os.remove("mpacman")
        os.remove("fox")
        break
    
    elif int(ennemie1.pdv) <= 0 and int(ennemie2.pdv) <= 0 and int(ennemie3.pdv) <= 0:
        print('Bravo vous avez gagné!')
        os.remove("Save.csv")
        os.remove("sauvegarde")
        os.remove("dracula")
        os.remove("mpacman")
        os.remove("fox")
        break