# -*-coding:Utf-8 -*


"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self,max_largeur,max_hauteur, position_robot, position_sortie,grille):
        self.max_largeur = max_largeur
        self.max_hauteur = max_hauteur
        self.position_robot = position_robot
        self.position_sortie = position_sortie
        self.grille = grille

    def display(self):
        """Permet d'afficher la grille du labyrinthe"""
        j=1
        i=1
        chaine = ""
        while (j<=self.max_hauteur):
            i=1
            while(i<=self.max_largeur):
                
                if self.position_robot[0] == i and self.position_robot[1] == j:
                    chaine += 'X'
                else:
                    chaine += self.grille[i,j]
                    
                i += 1
            chaine +="\n"
            j += 1
        
        print(chaine)
    
    def move(self, commande):
        """Permet de déplacer votre robot sur la carte du labyrinthe et affiche la grille mise à jour"""
        # Récupération de la direction ainsi que du nombre de déplacement
        direction = commande[0].lower()
        # si l'utilisateur n'a pas saisie de nombre de déplacement alors il est de 1 par défaut.
        nb_deplacement = 1
        if len(commande) > 1:
            nb_deplacement = int(commande[1:])
            
        if not self.deplacementPossible(direction, nb_deplacement):
            print("Déplacement impossible, un mûr vous empêche d'effectuer ce déplacement")
        else:
            print("Déplacement possible")
            self.calculNouvellePosition( direction,nb_deplacement)
        
        self.display()
            
    def sortieTrouvee(self):
        """Renvoi True si le joueur a trouvé la sortie, False sinon"""
        return self.position_robot == self.position_sortie
        
    def calculNouvellePosition(self, direction,nb_deplacement):
        """Calcul la nouvelle position du robot en fonction de la direction et du nombre de déplacement saisie"""
        if direction=='n':
            self.position_robot[1] -=  nb_deplacement
        elif direction=='s':
            self.position_robot[1] +=  nb_deplacement
        elif direction=='e':
            self.position_robot[0] += nb_deplacement
        elif direction=='o':
            self.position_robot[0] -=  nb_deplacement        
        

    def deplacementPossible(self,direction, nb_deplacement):
        """Retourne True si  si le déplacement est possible, False sinon"""
        
        deplacement_possible = True
        
        if direction == "n":
            deplacement_possible=self.deplacementNordPossible(nb_deplacement)
        elif direction == 's':
            deplacement_possible=self.deplacementSudPossible(nb_deplacement)
        elif direction == 'e':
            deplacement_possible=self.deplacementEstPossible(nb_deplacement)
        elif direction == 'o':
            deplacement_possible=self.deplacementOuestPossible(nb_deplacement)
        else :
            raise Exception("La direction rentrée est différente des lettres autorisées ('n','s','e','o')")

        return deplacement_possible
            
    def deplacementNordPossible(self, nb_deplacement):
        """On vérifie si le déplacement vers le Nord est possible"""
        
        # si le déplacement n'est pas sur la carte on retourne false
        if self.position_robot[1] - nb_deplacement < 1 :
            return False
        # si il y a un mûr sur la trajectoire on retourne false
        i=1
        while i<=nb_deplacement:
            if self.grille[self.position_robot[0], self.position_robot[1]-i] == 'O':
                return False
            i+=1
         # si rien ne bloque la trajectoire on retourne True
        return True
        
    def deplacementSudPossible(self, nb_deplacement):
        """On vérifie si le déplacement vers le Sud est possible"""
        
        # si le déplacement n'est pas sur la carte on retourne false
        if self.position_robot[1] + nb_deplacement < 1 :
            return False
        # si il y a un mûr sur la trajectoire on retourne false
        i=1
        while i<=nb_deplacement:
            if self.grille[self.position_robot[0], self.position_robot[1]+i] == 'O':
                return False
            i+=1
         # si rien ne bloque la trajectoire on retourne True
        return True
                 
    def deplacementOuestPossible(self, nb_deplacement):
        """On vérifie si le déplacement vers l'Ouest est possible"""
    
        # si le déplacement n'est pas sur la carte on retourne false
        if self.position_robot[0] - nb_deplacement > self.max_largeur  :
            return False
        # si il y a un mûr sur la trajectoire on retourne false
        i=1
        while i<=nb_deplacement:
            if self.grille[self.position_robot[0]-i, self.position_robot[1]] == 'O':
                return False
            i+=1
        # si rien ne bloque la trajectoire on retourne True
        return True
    
    def deplacementEstPossible(self, nb_deplacement):
        """On vérifie si le déplacement vers l'Est est possible""" 
                    
        # si le déplacement n'est pas sur la carte on retourne false
        if self.position_robot[0] + nb_deplacement > self.max_largeur  :
            return False
        # si il y a un mûr sur la trajectoire on retourne false
        i=1
        while i<=nb_deplacement:
            if self.grille[self.position_robot[0]+i, self.position_robot[1]] == 'O':
                return False
            i+=1
         # si rien ne bloque la trajectoire on retourne True
        return True