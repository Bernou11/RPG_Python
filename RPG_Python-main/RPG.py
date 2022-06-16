from ast import dump
import random
import csv
import os
import pickle
from sqlite3 import paramstyle

class Personnage():
    def __init__(self, nom, sexe, pdv, dmg, defense, classe, potion, capacite, paralyse, vivant, element_inventaire):
        self.nom = nom
        self.sexe = sexe
        self.pdv = str(pdv)
        self.dmg = str(dmg)
        self.defense = str(defense)
        self.classe = classe
        self.potion = potion
        self.capacite = capacite
        self.paralyse = paralyse
        self.vivant = vivant
        self.element_inventaire = element_inventaire

def lireCSV():
    with open('Save.csv', 'r+') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def firstSave(dracula, missPacman, starfox, perso):
    with open('Save.csv', 'w+', newline='') as file:
        writer = csv.writer(file)      
        writer.writerow(["Nom", "Sexe", "Pdv", "Dmg", "Classe", "Potion", "Capacité", "Paralysie", "Vivant"])
        writer.writerow([dracula.nom, dracula.sexe, dracula.pdv, dracula.dmg, dracula.classe, dracula.potion, dracula.capacite, dracula.paralyse, dracula.vivant])
        writer.writerow([missPacman.nom, missPacman.sexe, missPacman.pdv, missPacman.dmg, missPacman.classe, missPacman.potion, missPacman.capacite, missPacman.paralyse, missPacman.vivant])
        writer.writerow([starfox.nom, starfox.sexe, starfox.pdv, starfox.dmg, starfox.classe, starfox.potion, starfox.capacite, starfox.paralyse, starfox.vivant])
        writer.writerow([perso.nom, perso.sexe, perso.pdv, perso.dmg, perso.classe, perso.potion, perso.capacite, dracula.paralyse, perso.vivant])

def attaques():
    if perso.paralyse == "Non":
        attaque = int(input("Quel ennemi voulez vous attaquer? (1 pour Dracula, 2 pour Miss Pacman, 3 pour starfox)\n"))
        if attaque == 1 and perso.classe == "Guerrier":
            global dracula    
            if int(dracula.pdv) <= 0:
                print("Dracula est déjà mort, visez un autre ennemi!")   
                attaques()                 
            elif int(dracula.pdv) > 0:
                    dracula.pdv = int(dracula.pdv) - 8
                    print("Vous infligez 8 dégâts à Dracula!\nIl lui reste",dracula.pdv,"points de vie")
                    with open ("Dracula", "wb") as Dracula:
                        pickle.dump(dracula, Dracula)   
                    if int(dracula.pdv) <= 0:
                        print("Bravo vous avez tué Dracula! \nVous obtenez une dent de vampire")
                        perso.element_inventaire = perso.element_inventaire + 1
                        dracula.vivant = "Non"
                        dracula.pdv = 0
                        with open ("Dracula", "wb") as Dracula:
                            pickle.dump(dracula, Dracula)
                        with open ("sauvegarde", "wb") as save:
                            pickle.dump(perso, save)
        elif attaque == 2 and perso.classe == "Guerrier":
            global missPacman
            if int(missPacman.pdv) <= 0:
                print("Miss Pacman est déjà morte, visez un autre ennemi!")
                attaques()
            elif int(missPacman.pdv) > 0:
                missPacman.pdv = int(missPacman.pdv) - 8
                print("Vous infligez 8 dégâts à Miss Pacman!\nIl lui reste encore:",missPacman.pdv,"points de vie")
                with open ("mpacman", "wb") as mpacman:
                    pickle.dump(missPacman, mpacman)    
                if int(missPacman.pdv) <= 0:
                    print("Bravo vous avez tué Miss Pacman! \nVous obtenez un citron")
                    perso.element_inventaire = perso.element_inventaire + 1
                    missPacman.vivant = "Non"
                    missPacman.pdv = 0
                    with open ("mpacman", "wb") as mpacman:
                        pickle.dump(missPacman, mpacman)
                    with open ("sauvegarde", "wb") as save:
                        pickle.dump(perso, save)
        elif attaque == 3 and perso.classe == "Guerrier":
            global starfox
            if int(starfox.pdv) <= 0:
                print("starfox est déjà mort, visez un autre ennemi!")
                attaques()
            elif int(starfox.pdv) > 0:
                starfox.pdv = int(starfox.pdv) - 8
                print("Vous infligez 8 dégâts à starfox!\nIl lui reste encore:",starfox.pdv,"points de vie")
                if int(starfox.pdv) <= 0:
                    print("Bravo vous avez tué starfox! \nVous obtenez un poil de renard")
                    perso.element_inventaire = perso.element_inventaire + 1
                    starfox.vivant = "Non"
                    starfox.pdv = 0
                    with open ("fox", "wb") as fox:
                        pickle.dump(starfox, fox)
                    with open ("sauvegarde", "wb") as save:
                        pickle.dump(perso, save)
        elif attaque < 1 and attaque >= 3:
            print("Choisissez entre 1, 2 ou 3")
            attaques()

    elif perso.paralyse == "Non":
        if i < 3:
            if attaque == 1 and perso.classe == "Mage":
                global dracula
                if int(dracula.pdv) <= 0:
                    print("Dracula est déjà mort, visez un autre ennemi!")
                    attaques()
                elif int(dracula.pdv) > 0:
                    dracula.pdv = int(dracula.pdv) - 16
                    print("Vous infligez 16 dégâts à Dracula!\nIl lui reste ",dracula.pdv,"points de vie")
                    with open ("Dracula", "wb") as Dracula:
                        pickle.dump(dracula, Dracula) 
                    if int(dracula.pdv) <= 0:
                        print("Bravo vous avez tué Dracula! \nVous obtenez une dent de vampire")
                        perso.element_inventaire = perso.element_inventaire + 1
                        dracula.vivant = "Non"
                        dracula.pdv = 0
                        with open ("Dracula", "wb") as Dracula:
                            pickle.dump(dracula, Dracula) 
                        with open ("sauvegarde", "wb") as save:
                            pickle.dump(perso, save)
                    k += 1
                    with open ("sauvegarde", "wb") as save:
                        pickle.dump(i, save)
            elif attaque == 2 and perso.classe == "Mage":
                global missPacman
                if int(missPacman.pdv) <= 0:
                    print("Miss Pacman est déjà morte, visez un autre ennemi!")
                    attaques()
                elif int(missPacman.pdv) > 0:
                    missPacman.pdv = int(missPacman.pdv) - 16
                    print("Vous infligez 16 dégâts à Miss Pacman!\nIl lui reste ",missPacman.pdv,"points de vie")
                    with open ("mpacman", "wb") as mpacman:
                        pickle.dump(missPacman, mpacman) 
                    if int(missPacman.pdv) <= 0:
                        print("Bravo vous avez tué Miss Pacman! \nVous obtenez un citron")
                        perso.element_inventaire = perso.element_inventaire + 1
                        missPacman.vivant = "Non"
                        missPacman.pdv = 0
                        with open ("mpacman", "wb") as mpacman:
                            pickle.dump(missPacman, mpacman) 
                        with open ("sauvegarde", "wb") as save:
                            pickle.dump(perso, save)
                    k += 1
                    with open ("sauvegarde", "wb") as save:
                        pickle.dump(i, save)
            elif attaque == 3 and perso.classe == "Mage":
                global starfox
                if int(starfox.pdv) <= 0:
                    print("starfox est déjà mort, visez un autre ennemi!")
                    attaques()
                elif int(starfox.pdv) > 0:
                    starfox.pdv = int(starfox.pdv) - 16
                    print("Vous infligez 16 dégâts à starfox!\nIl lui reste ",starfox.pdv,"points de vie")
                    with open ("fox", "wb") as fox:
                        pickle.dump(starfox, fox) 
                    if int(starfox.pdv) <= 0:
                        print("Bravo vous avez tué starfox! \nVous obtenez un poil de renard")
                        perso.element_inventaire = perso.element_inventaire + 1
                        starfox.vivant = "Non" 
                        starfox.pdv = 0 
                        with open ("fox", "wb") as fox:
                            pickle.dump(starfox, fox)
                        with open ("sauvegarde", "wb") as save:
                            pickle.dump(perso, save)
                    k += 1
                    with open ("sauvegarde", "wb") as save:
                        pickle.dump(i, save)
            elif attaque != 1 or attaque != 2 or attaque != 3:
                print("Choisissez entre 1, 2 ou 3") 
                attaques()            
        else:
            print("Vous rentrez en rage! Vous infligerez 8 dégâts de plus ce tour!\n")
            if attaque == 1 and perso.classe == "Mage":
                global dracula
                if int(dracula.pdv) <= 0:
                    print("Dracula est déjà mort, visez un autre ennemi!")
                    attaques()
                elif int(dracula.pdv) > 0:
                    dracula.pdv = int(dracula.pdv) - 24
                    print("Vous infligez 21 dégâts à Dracula!\nIl lui reste ",dracula.pdv,"points de vie")
                    with open ("Dracula", "wb") as Dracula:
                        pickle.dump(dracula, Dracula) 
                    if int(dracula.pdv) <= 0:
                        print("Bravo vous avez tué Dracula! \nVous obtenez une dent de vampire")
                        perso.element_inventaire = perso.element_inventaire + 1
                        dracula.vivant = "Non"
                        dracula.pdv = 0
                        with open ("Dracula", "wb") as Dracula:
                            pickle.dump(dracula, Dracula) 
                        with open ("sauvegarde", "wb") as save:
                            pickle.dump(perso, save)
                    k += 1
                    with open ("sauvegarde", "wb") as save:
                        pickle.dump(k, save)
            elif attaque == 2 and perso.classe == "Mage":
                global missPacman
                if int(missPacman.pdv) <= 0:
                    print("Miss Pacman est déjà morte, visez un autre ennemi!")
                    attaques()
                elif int(missPacman.pdv) > 0:
                    missPacman.pdv = int(missPacman.pdv) - 24
                    print("Vous infligez 21 dégâts à Miss Pacman!\nIl lui reste ",missPacman.pdv,"points de vie")
                    with open ("mpacman", "wb") as mpacman:
                        pickle.dump(missPacman, mpacman) 
                    if int(missPacman.pdv) <= 0:
                        print("Bravo vous avez tué Miss Pacman! \nVous obtenez un citron")
                        perso.element_inventaire = perso.element_inventaire + 1
                        missPacman.vivant = "Non"
                        missPacman.pdv = 0
                        with open ("mpacman", "wb") as mpacman:
                            pickle.dump(missPacman, mpacman) 
                        with open ("sauvegarde", "wb") as save:
                            pickle.dump(perso, save)
                    k += 1
                    with open ("sauvegarde", "wb") as save:
                        pickle.dump(k, save)
            elif attaque == 3 and perso.classe == "Mage":
                global starfox
                if int(starfox.pdv) <= 0:
                    print("starfox est déjà mort, visez un autre ennemi!")
                    attaques()
                elif int(starfox.pdv) > 0:
                    starfox.pdv = int(starfox.pdv) - 24
                    print("Vous infligez 21 dégâts à starfox!\nIl lui reste ",starfox.pdv,"points de vie")
                    with open ("fox", "wb") as fox:
                        pickle.dump(starfox, fox) 
                    if int(starfox.pdv) <= 0:
                        print("Bravo vous avez tué starfox! \nVous obtenez un poil de renard")
                        perso.element_inventaire = perso.element_inventaire + 1
                        starfox.vivant = "Non" 
                        starfox.pdv = 0 
                        with open ("fox", "wb") as fox:
                            pickle.dump(starfox, fox)
                        with open ("sauvegarde", "wb") as save:
                            pickle.dump(perso, save)
                    k += 1
                    with open ("sauvegarde", "wb") as save:
                        pickle.dump(k, save)
            elif attaque != 1 or attaque != 2 or attaque != 3:
                print("Choisissez entre 1, 2 ou 3")
                attaques()

    if perso.paralyse == "Non":
        critique = []
        for i in range(100):
            i += 1
            critique.append(i)
        crit = random.choice(critique)    
        if attaque == 1 and perso.classe == "Archer" and crit > 20:
            global dracula
            if int(dracula.pdv) <= 0:
                print("Dracula est déjà mort, visez un autre ennemi!")
                attaques()
            elif int(dracula.pdv) > 0:
                dracula.pdv = int(dracula.pdv) - 13
                print("Vous infligez 13 dégâts à Dracula!\nIl lui reste ",dracula.pdv,"points de vie")
                with open ("dracula", "wb") as dracula:
                    pickle.dump(dracula, dracula) 
                if int(dracula.pdv) <= 0:
                    print("Bravo vous avez tué Dracula! \nVous obtenez une dent de vampire")
                    perso.element_inventaire = perso.element_inventaire + 1
                    dracula.vivant = "Non"
                    dracula.pdv = 0
                    with open ("dracula", "wb") as dracula:
                        pickle.dump(dracula, dracula) 
                    with open ("sauvegarde", "wb") as save:
                        pickle.dump(perso, save)    
        elif attaque == 2 and perso.classe == "Archer" and crit > 20:
            global missPacman
            if int(missPacman.pdv) <= 0:
                print("Miss Pacman est déjà morte, visez un autre ennemi!")
                attaques()
            elif int(missPacman.pdv) > 0:
                missPacman.pdv = int(missPacman.pdv) - 13
                print("Vous infligez 13 dégâts à Dracula!\nIl lui reste ", missPacman.pdv,"points de vie")
                with open ("mpacman", "wb") as mpacman:
                    pickle.dump(missPacman, mpacman) 
                if int(missPacman.pdv) <= 0:
                    print("Bravo vous avez tué Miss Pacman! \nVous obtenez un citron")
                    perso.element_inventaire = perso.element_inventaire + 1
                    missPacman.vivant = "Non"
                    missPacman.pdv = 0
                    with open ("mpacman", "wb") as mpacman:
                        pickle.dump(missPacman, mpacman)
                    with open ("sauvegarde", "wb") as save:
                        pickle.dump(perso, save)    
        elif attaque == 3 and perso.classe == "Archer" and crit > 20:
            global starfox
            if int(starfox.pdv) <= 0:
                print("starfox est déjà mort, visez un autre ennemi!")
                attaques()
            elif int(starfox.pdv) > 0:
                starfox.pdv = int(starfox.pdv) - 13
                print("Vous infligez 13 dégâts à starfox!\nIl lui reste ",starfox.pdv,"points de vie")
                with open ("fox", "wb") as fox:
                    pickle.dump(starfox, fox)
                if int(starfox.pdv) <= 0:
                    print("Bravo vous avez tué starfox! \nVous obtenez un poil de renard")
                    perso.element_inventaire = perso.element_inventaire + 1
                    starfox.vivant = "Non"
                    starfox.pdv = 0
                    with open ("fox", "wb") as fox:
                        pickle.dump(starfox, fox)
                    with open ("sauvegarde", "wb") as save:
                        pickle.dump(perso, save)
        if crit <= 20:  
            print("Vous infligez un coup critique! Vous infligez 3 dégâts supplémentaires!")              
            if attaque == 1 and perso.classe == "Archer":
                if int(dracula.pdv) <= 0:
                    print("Dracula est déjà mort, visez un autre ennemi!")
                    attaques()
                elif int(dracula.pdv) > 0:
                    dracula.pdv = int(dracula.pdv) - 16
                    print("Vous infligez 16 dégâts à Dracula!\nIl lui reste ",dracula.pdv,"points de vie")
                    with open ("dracula", "wb") as dracula:
                        pickle.dump(dracula, dracula) 
                    if int(dracula.pdv) <= 0:
                        print("Bravo vous avez tué Dracula! \nVous obtenez une dent de vampire")
                        perso.element_inventaire = perso.element_inventaire + 1
                        dracula.vivant = "Non"
                        dracula.pdv = 0
                        with open ("dracula", "wb") as dracula:
                            pickle.dump(dracula, dracula) 
                        with open ("sauvegarde", "wb") as save:
                            pickle.dump(perso, save)    
            elif attaque == 2 and perso.classe == "Archer":
                if int(missPacman.pdv) <= 0:
                    print("Miss Pacman est déjà morte, visez un autre ennemi!")
                    attaques()
                elif int(missPacman.pdv) > 0:
                    missPacman.pdv = int(missPacman.pdv) - 16
                    print("Vous infligez 16 dégâts à Dracula!\nIl lui reste ", missPacman.pdv,"points de vie")
                    with open ("mpacman", "wb") as mpacman:
                        pickle.dump(missPacman, mpacman) 
                    if int(missPacman.pdv) <= 0:
                        print("Bravo vous avez tué Miss Pacman! \nVous obtenez un citron")
                        perso.element_inventaire = perso.element_inventaire + 1
                        missPacman.vivant = "Non"
                        missPacman.pdv = 0
                        with open ("mpacman", "wb") as mpacman:
                            pickle.dump(missPacman, mpacman)
                        with open ("sauvegarde", "wb") as save:
                            pickle.dump(perso, save)    
            elif attaque == 3 and perso.classe == "Archer":
                if int(starfox.pdv) <= 0:
                    print("starfox est déjà mort, visez un autre ennemi!")
                    attaques()
                elif int(starfox.pdv) > 0:
                    starfox.pdv = int(starfox.pdv) - 16
                    print("Vous infligez 16 dégâts à starfox!\nIl lui reste ",starfox.pdv,"points de vie")
                    with open ("fox", "wb") as fox:
                        pickle.dump(starfox, fox)
                    if int(starfox.pdv) <= 0:
                        print("Bravo vous avez tué starfox! \nVous obtenez un poil de renard")
                        perso.element_inventaire = perso.element_inventaire + 1
                        starfox.vivant = "Non"
                        starfox.pdv = 0
                        with open ("fox", "wb") as fox:
                            pickle.dump(starfox, fox)
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
    if perso.classe != "Guerrier":
        if int(perso.pdv) > 0 and dracula.vivant == "Oui" or missPacman.vivant == "Oui" or starfox.vivant == "Oui":
            print('Tour ennemi!\n')
            choix_action_ennemie = random.choice(action_ennemie)
            if choix_action_ennemie == 1 and int(dracula.pdv) > 0:
                perso.pdv = int(perso.pdv) - 5
                dracula.pdv = int(dracula.pdv) + 2
                print("Dracula vous inflige 5 points de dégats et vous vole 2 points de vie!\nIl vous reste", perso.pdv,"points de vie et ses points de vie remontent à", dracula.pdv,"\n")
            elif choix_action_ennemie == 2 and int(dracula.pdv) > 0:
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
            if choix_action_ennemie == 1 and int(starfox.pdv) > 0:
                if paralysie > 1:
                    perso.pdv = int(perso.pdv) - 6
                    print("starfox vous inflige 6 points de dommage!\nIl vous reste ",perso.pdv,"points de vie\n")
                else:
                    perso.pdv = int(perso.pdv) - 6
                    perso.paralyse = "Oui"
                    print("starfox vous inflige 6 points de dommage!\nIl vous reste ",perso.pdv,"points de vie\n")
                    print("Ho non cette attaque vous a paralysé! Vous devrez passer votre prochain tour")
            elif choix_action_ennemie == 2 and int(starfox.pdv) > 0:
                print("starfox passe son tour\n")  
            choix_action_ennemie = random.choice(action_ennemie)
            o_s = []
            j = 0
            for j in range (50):
                j += 1
                o_s.append(j)
            print(o_s)
            os = random.choice(o_s)
            print(os)
            if choix_action_ennemie == 1 and int(missPacman.pdv) > 0:
                if os == 1 or os == 2 or os == 3 or os == 4:
                    print("Pas de chance, Miss Pacman vous a mangé! vous perdez immédiatement la partie! :(")
                    perso.pdv = 0
                else:
                    perso.pdv = int(perso.pdv) - 3
                    print("Miss Pacman vous inflige 3 dégats!\nIl vous reste ", perso.pdv,"points de vie\n")                  
            elif choix_action_ennemie == 2 and int(missPacman.pdv) > 0:
                print("Miss Pacman passe son tour\n")  
            with open ("sauvegarde", "wb") as save:
                pickle.dump(perso, save)
    else:
        if int(perso.pdv) > 0 and dracula.vivant == "Oui" or missPacman.vivant == "Oui" or starfox.vivant == "Oui":
            print('Tour ennemi!\n')
            choix_action_ennemie = random.choice(action_ennemie)
            if choix_action_ennemie == 1 and int(dracula.pdv) > 0:
                perso.pdv = int(perso.pdv) - 2
                dracula.pdv = int(dracula.pdv) + 1
                print("Dracula vous inflige 2 points de dégats et vous vole 1 points de vie!\nIl vous reste", perso.pdv,"points de vie et ses points de vie remontent à", dracula.pdv,"\n")
            elif choix_action_ennemie == 2 and int(dracula.pdv) > 0:
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
            if choix_action_ennemie == 1 and int(starfox.pdv) > 0:
                if paralysie > 1:
                    perso.pdv = int(perso.pdv) - 3
                    print("starfox vous inflige 3 points de dommage!\nIl vous reste ",perso.pdv,"points de vie\n")
                else:
                    perso.pdv = int(perso.pdv) - 3
                    perso.paralyse = "Oui"
                    print("starfox vous inflige 3 points de dommage!\nIl vous reste ",perso.pdv,"points de vie\n")
                    print("Ho non cette attaque vous a paralysé! Vous devrez passer votre prochain tour")
            elif choix_action_ennemie == 2 and int(starfox.pdv) > 0:
                print("starfox passe son tour\n")  
            choix_action_ennemie = random.choice(action_ennemie)
            o_s = []
            j = 0
            for j in range (50):
                j += 1
                o_s.append(j)
            print(o_s)
            os = random.choice(o_s)
            print(os)
            if choix_action_ennemie == 1 and int(missPacman.pdv) > 0:
                if os == 1 or os == 2 or os == 3 or os == 4:
                    print("Pas de chance, Miss Pacman vous a mangé! vous perdez immédiatement la partie! :(")
                    perso.pdv = 0
                else:
                    perso.pdv = int(perso.pdv) - 1
                    print("Miss Pacman vous inflige 1 dégats!\nIl vous reste ", perso.pdv,"points de vie\n")                  
            elif choix_action_ennemie == 2 and int(missPacman.pdv) > 0:
                print("Miss Pacman passe son tour\n")  
            with open ("sauvegarde", "wb") as save:
                pickle.dump(perso, save)

def partie():
    if perso.potion == "Oui":
        action = int(input("Voulez vous attaquer, vous soigner ou ouvrir votre inventaire? (1 pour attaquer, 2 pour vous soigner, 3 pour ouvrir votre inventaire)\n"))
        if action == 1:
            attaques()
        elif action == 2:
            perso.pdv = int(perso.pdv) + 15
            print('Vous avez maintenant',perso.pdv,"points de vie")
            perso.potion = "Non"
            with open ("sauvegarde", "wb") as save:
                pickle.dump(perso, save)
        elif action == 3:
            print("Votre inventaire :", inventaire)
            action_inventaire = int(input("0 : Quitter votre inventaire\n"))
            if action_inventaire == 0:
                partie()
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
        action = int(input("Voulez-vous attaquer ou ouvrir votre inventaire? (1 pour attaquer; 2 pour ouvrir votre invenrtaire)\n"))
        if action == 1:
            attaques()
        elif action == 2:
            print(inventaire)
            action_inventaire = int(input("0 : Quitter votre inventaire"))
            if action_inventaire == 0:
                partie()
        else:
            print("Choisissez 1 ou 2")
            partie()
    print('\n')
    tour_ennemis()

def crea_perso():
    sexe = input("Choisissez le sexe de votre personnage (F pour femme et H pour homme): ")
    if sexe == "H" or sexe == "F" or sexe == "h" or sexe == "f":
        def crea_perso_classe():
            classe = int(input("Choisissez votre classe (1 = guerrier, 2 = mage ou 3 = archer): "))
            if classe == 1: 
                perso = Personnage(nom, sexe, 50, 8, 3, "Guerrier", "Oui", "Défense élevée", "Non", "Oui", 0)
                with open("sauvegarde", "wb") as save:
                    pickle.dump(perso, save)
                with open("Dracula", "wb") as Dracula:
                    pickle.dump(dracula, Dracula)     
                with open("mpacman", "wb") as mpacman:
                    pickle.dump(missPacman, mpacman)
                with open("fox", "wb") as fox:
                    pickle.dump(starfox, fox)                  
            elif classe == 2:
                perso = Personnage(nom, sexe, 25, 16, 0, "Mage",'Oui', "Furie", "Non", "Oui", 0)
                with open("sauvegarde", "wb") as save:
                    pickle.dump(perso, save) 
                with open("Dracula", "wb") as Dracula:
                    pickle.dump(dracula, Dracula)     
                with open("mpacman", "wb") as mpacman:
                    pickle.dump(missPacman, mpacman)
                with open("fox", "wb") as fox:
                    pickle.dump(starfox, fox)  
            elif classe == 3:
                perso = Personnage(nom, sexe, 35, 13, 0, "Archer", "Oui", "Coup critique", "Non", "Oui", 0)
                with open("sauvegarde", "wb") as save:
                    pickle.dump(perso, save) 
                with open("Dracula", "wb") as Dracula:
                    pickle.dump(dracula, Dracula)     
                with open("mpacman", "wb") as mpacman:
                    pickle.dump(missPacman, mpacman)
                with open("fox", "wb") as fox:
                    pickle.dump(starfox, fox)       
            else:
                print("Veuillez choisir entre 1, 2 et 3")
                crea_perso_classe()
            firstSave(dracula, missPacman, starfox, perso)        
        crea_perso_classe()          
    else:
        print("Veuillez choisir entre h ou f")
        crea_perso()

dracula = Personnage("Dracula", "M", 30, 5, 0, "Vampire", "Non", "Vol de vie", "Non", "Oui", 0)
missPacman = Personnage("Miss Pacman", "F", 25, 3, 0, "Boule jaune","Non", "One shot", "Non", "Oui", 0)
starfox = Personnage("Starfox", "M", 20, 6, 0, "Renard", "Non", "Paralysie", "Non", "Oui", 0)

k = 0
if os.path.exists("sauvegarde"):
    with open("sauvegarde", "rb") as save:
        perso = pickle.load(save)
        print(perso)
    with open("Dracula", "rb") as Dracula:
        dracula = pickle.load(Dracula)
        print(dracula)
    with open("mpacman", "rb") as mpacman:
        missPacman = pickle.load(mpacman)
        print(missPacman)
    with open("fox", "rb") as fox:
        starfox = pickle.load(fox)
        print(starfox)
else:
    nom = input("Choisissez le nom de votre personnage: ")  
    crea_perso()
    with open("sauvegarde", "rb") as save:
        perso = pickle.load(save)
inventaire = []        
while int(perso.pdv) > 0 or int(dracula.pdv) > 0 and int(missPacman.pdv) > 0 and int(starfox.pdv) > 0:
    print('Votre tour!\n')
    partie()
    firstSave(dracula, missPacman, starfox, perso)

    if int(perso.pdv) <= 0:
        print('Dommage vous avez perdu :(')
        os.remove("Save.csv")
        os.remove("sauvegarde")
        os.remove("dracula")
        os.remove("mpacman")
        os.remove("fox")
        break
    
    elif int(dracula.pdv) <= 0 and int(missPacman.pdv) <= 0 and int(starfox.pdv) <= 0:
        print('Bravo vous avez gagné!')
        os.remove("Save.csv")
        os.remove("sauvegarde")
        os.remove("dracula")
        os.remove("mpacman")
        os.remove("fox")
        break