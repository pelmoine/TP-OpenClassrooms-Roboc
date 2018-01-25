# -*-coding:Utf-8 -*

"""Ce module contient la classe Partie. Elle permet de sauvegarder une partie en cours et de la récupérer par la suite."""

import pickle
from pathlib import Path
import os

class Partie:

    file_name_partie_saved = "parties.save"
    
    def __init__(self,joueur_name,carte_name, position_robot):
        self.joueur_name = joueur_name
        self.carte_name = carte_name + "txt"
        self.position_robot = position_robot
        self.saveNouvellePartie()
        
    def saveNouvellePartie(self):
        """ sauvegarde une nouvelle partie dans un fichier 'parties.save' """
        
        score_recupere = {}
        if os.path.getsize(Partie.file_name_partie_saved) > 0: 
            with open(Partie.file_name_partie_saved, "rb") as file:
                score_recupere = pickle.load(file)
                
        score_recupere[self.joueur_name] = self
        with open(Partie.file_name_partie_saved,'wb') as file:
            pickle.dump(score_recupere, file)  
            
    def save(self, position_robot):
        """ sauvegarde une nouvelle partie dans un fichier 'parties.save' """
  
        with open(Partie.file_name_partie_saved, "rb") as file:
            score_recupere = pickle.load(file)
            score_recupere[self.joueur_name] = self
        
        with open(Partie.file_name_partie_saved,'wb') as file:
            pickle.dump(score_recupere, file)      

         
   
        

            