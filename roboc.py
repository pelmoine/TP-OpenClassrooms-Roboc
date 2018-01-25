# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""


import re
# class helper contenant des fonctions
import interactionHelper
import carteHelper
import partieHelper
# class object contenant des méthodes associées
from carte import Carte
from partie import Partie 




def afficheLabyrinthes(cartes):
    """ Affiche la liste des labyrinthes existants. """
    print("Labyrinthes existants :")
    for i, carte in enumerate(cartes):
        print("  {} - {}".format(i + 1, carte.nom))
        carte.labyrinthe.display()


def play(partie):
    """ Fonction principal du jeux, gestion de l'entrée utilisateur. """
    # Tant que le joueur n'utilise pas la touche Q ou qu'il n'a pas gagner, le jeux continu
    win = False
    mouvement=""
    while not win  :
        mouvement = input("Veuillez entrer un mouvement : ")
        mouvement_rex = re.compile("^[nsoeNSOE]{1}[0-9]*$")
        
        # Si l'input est au bon format 
        if mouvement_rex.match(mouvement):
            labyrinthe.move(mouvement)
            win = labyrinthe.sortieTrouvee()
            partie.save(labyrinthe.position_robot)
        # si l'input est 'q' pour quitter on demande une confirmation avant d'arrêter le jeu         
        elif mouvement.lower() =='q' :
            if interactionHelper.confirmerStopPlay():
                break
            else:
                mouvement =''
        
        # si l'input n'est pas au bon format
        else :
            print("Erreur de saisie, merci de vous référer au rappel des commandes \n")
            
    if win is True :
        partieHelper.delete(partie.joueur_name)
        print("Félicitations !! Vous avez gagné !!")    



# On demande le pseudo du joeueur
joueur_name = interactionHelper.demandeNomJoueur()
# On vérifie si une partie est déjà en cours avec ce pseudo
partie = partieHelper.verifiePartieExiste(joueur_name)

nouvelle_partie = False
# Si oui, on propose de reprendre la partie 
if partie != False :
    reprendre_partie = False

    while not reprendre_partie and not nouvelle_partie:
        if interactionHelper.reprendrePartie() :
            reprendre_partie = True
        else: 
            # Si on ne reprend pas la partie, alors la sauvegarde sera écrasée        
            if interactionHelper.confirmerNouvellePartie() :
                print("En avant pour une nouvelle partie !") 
                nouvelle_partie = True 
            
            
if partie == False or nouvelle_partie == True :       
    # On charge les cartes existantes
    cartes= carteHelper.chargementCartes()

    # On affiche les cartes existantes
    afficheLabyrinthes(cartes)
    
    # l'utilisateur choisi une carte et commence la partie
    choix_carte = carteHelper.choixCartes(cartes)

    # Rappel des commandes
    interactionHelper.rappelDesCommandes()
    
    print("\n \n Commençons la partie ! \n \n")
    labyrinthe = cartes[choix_carte-1].labyrinthe
    partie = Partie(joueur_name, cartes[choix_carte-1].nom, labyrinthe.position_robot)
    
else :
    # On reprends la partie
    carte = carteHelper.chargementCarte(partie.carte_name) 
    # On charge le labyrinthe ainsi que la position du joueur sauvegardé
    print("\n \n Reprenons la partie ! \n \n")
    labyrinthe = carte.labyrinthe
    labyrinthe.position_robot = partie.position_robot
    
labyrinthe.display()

# Jouer le jeux 
play(partie)

    
print("\n\n A bientôt !! ")

