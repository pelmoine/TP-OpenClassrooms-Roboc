# -*-coding:Utf-8 -*


"""Ce module contient les fonctions liées au partie."""

from partie import Partie 
from pathlib import Path
import pickle
import os

file_name_partie_saved = "parties.save"

def verifiePartieExiste( joueur_name):
    """ On vérifie si une partie existe le fichier parties.save avec ce nom de joueur."""
    my_file = Path("./"+file_name_partie_saved)
    if not my_file.is_file():
        print ("Le fichier 'partie.save' n'existe pas, il sera créé.")
        open(file_name_partie_saved, "wb").close()        
        
    if os.path.getsize(file_name_partie_saved) > 0: 
        with open(file_name_partie_saved, "rb") as file:
            parties = pickle.load(file)
            #Si le fichier de sauvegarde existe, on vérifie si le nom du joueur est présent
            if parties is not None and isinstance(parties,dict) and joueur_name in parties and isinstance(parties.get(joueur_name),Partie):
                return parties.get(joueur_name)
            else:
                print("Aucun partie sauvegardé pour {}".format(joueur_name))
    else : 
        print ("Le fichier 'partie.save' est vide.")
       
        
    return False

def delete(joueur_name):
    """ supprime une partie terminée"""
    
    with open(file_name_partie_saved, "rb") as file:
        
        score_recupere = pickle.load(file)
        del score_recupere[joueur_name]
    
    with open(file_name_partie_saved,'wb') as file:
        pickle.dump(score_recupere, file)    