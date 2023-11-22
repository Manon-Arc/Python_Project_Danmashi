import random
     
class Floor:
    def __init__(self, niveau):
        self._name
        self.niveau = niveau
        self._win = False
        self.monstres = self.generer_monstres()
        
    def generer_monstres(self):
           if self.niveau == 1:
               return [Goblini(self.niveau)]
           elif self.niveau == 2:
               return [Rador(self.niveau)]
           else:
               # Gestion des autres niveaux
               pass
           
