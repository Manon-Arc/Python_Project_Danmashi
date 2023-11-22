from floor import Floor

class Dungeon:
    def __init__(self):
        self.joueur = Joueur("NomDuJoueur")
        self.floors = [Floor(niveau) for niveau in range(1, 6)]  # Exemple : 5 niveaux de floors

    def passer_au_niveau_suivant(self):
            if self.joueur.points_de_vie > 0:
                print("Bravo ! Vous avez vaincu les monstres de ce niveau.")
                self.joueur.niveau += 1
                print(f"Vous passez au niveau {self.joueur.niveau}.")
            else:
                print("Game Over. Vous avez été vaincu.")
                # Vous pourriez également réinitialiser le jeu ou afficher un écran de fin.
