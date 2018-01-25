# -*-coding:Utf-8 -*


"""Ce module contient les interactions avec l'utilisateur."""

import re

def demandeNomJoueur():
    """ Sauvegarde le nom du joueur dans une variable globale. """
    
    nom_joueur = input("Saisissez votre pseudo : ")
    while len(nom_joueur) < 1 :
        nom_joueur = input("Merci de réessayer, saisissez votre pseudo : ")
    
    return nom_joueur


def rappelDesCommandes():
    """ Affiche le rappel des commandes. """
    print("\n \n Rappel des commandes : \n \
    Le robot est contrôlable grâce à des commandes entrées au clavier. Il doit exister les commandes suivantes :\n\n \
    Q qui doit permettre de sauvegarder et quitter la partie en cours ;\n \
    N qui demande au robot de se déplacer vers le nord (c'est-à-dire le haut de votre écran) ;\n \
    E qui demande au robot de se déplacer vers l'est (c'est-à-dire la droite de votre écran) ;\n \
    S qui demande au robot de se déplacer vers le sud (c'est-à-dire le bas de votre écran) ;\n \
    O qui demande au robot de se déplacer vers l'ouest (c'est-à-dire la gauche de votre écran) ;\n\n \
    Chacune des directions ci-dessus suivies d'un nombre permet d'avancer de plusieurs cases (par exemple E3 pour avancer de trois cases vers l'est).\n\n")

def confirmerStopPlay():
    """ Demande une confirmation à l'utilisateur lorsqu'il veut quitter ça partie. """
    
    if yesNoQuestion("Etes-vous vraiment sûr de vouloir quitter le jeu ? O/N : ") :
        return True
    print("Continuons la partie !")
    return False

def confirmerNouvellePartie():
    """ Demande une confirmation à l'utilisateur lorsqu'il veut commencer une nouvelle partie. """
    
    if yesNoQuestion("Etes-vous vraiment sûr de vouloir commencer une nouvelle partie ? \
    \nCela entrainera la suppression de votre sauvegarde sur les précédantes partie avec ce pseudo. O/N : ") :
        print("Ancienne partie supprimée. Commençons une nouvelle partie !")
        return True
    
    return False

def yesNoQuestion(question):
    """ Fonction générique utilisée pour les yes no question à l'utilisateur """
    confirmation = ''
    yes_no_rex = re.compile("^[oOyYnN]{1}$")    
    while not yes_no_rex.match(confirmation):
        confirmation = input(question)
        if confirmation.lower() == 'o' or confirmation.lower() == 'y' :
            return True
        else :
            return False

def reprendrePartie():
    """ Demdande si l'utilisateur souhaire reprendre ou continuer la partie"""
    return yesNoQuestion("Voulez-vous reprendre votre partie ? O/N : ")
