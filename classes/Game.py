class Game:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.joueur = Joueur("NomDuJoueur")
        self.current_floor = 0  # Indice du floor actuel
        self.current_monster = 0  # Indice du monstre actuel