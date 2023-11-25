import pygame
import keyboard
from character import Character
from dungeon import Dungeon
from warrior import Warrior
from mage import Mage
from assassin import Assassin
from mob import Goblini, Wolfor, Basilisc, Animal_trainer, Hydre

class Game:
    playerClasseAllow = [#penser à bien mettre en minuscule les clés
        "Mage",
        "Assassin",
        "Warrior"
        ]
    
    def __init__(self):
        self.dungeon = Dungeon()
        self.player = None

    def start_game(self):
        print("Bienvenue dans le jeu !")
        self.create_player()
        self.dungeon.generate_floors()

        for i, floor in enumerate(self.dungeon.floors):
            print(f"\n======= Étage {i + 1} =======")
            self.play_floor(floor)
            
        print("\nFélicitations ! Vous avez terminé le donjon.")
        
    def create_player(self):
        player_name = input("Entrez le nom de votre personnage : ")
        player_class = ""
        while player_class == "":
            player_class = input("Choisissez votre classe (Guerrier, Mage, Assassin) : ").capitalize()
            if player_class in self.playerClasseAllow:
                self.player = eval(f"{player_class}('{player_name}')")
            else:
                print("Classe invalide. Veuillez choisir parmi :", end=" ") 
                for index,classe in enumerate(self.playerClasseAllow):
                    if index < len(self.playerClasseAllow)-1:
                        print(classe, end=", ")
                    else:
                        print(classe)
                player_class = ""

    def play_floor(self, floor):
        print(f"Vous êtes à l'étage {floor.level}. Préparez-vous à combattre !")

        for monster in floor.monsters:
            print(f"\nUn monstre approche : {monster.get_name()} !")
            while monster.is_alive() and self.player.is_alive():
                self.player.attack(monster)
                if monster.is_alive():
                    monster.attack(self.player)

                print(f"\nÉtat actuel de {self.player.get_name()}:")
                self.player.show_healthbar()

                print(f"État actuel de {monster.get_name()}:")
                monster.show_healthbar()

                input("Appuyez sur Entrée pour continuer...")

            if not self.player.is_alive():
                print("Vous avez été vaincu. Game Over.")
                return

        print(f"\nVous avez vaincu tous les monstres de l'étage {floor.level}. Bravo !")

def jouer_musique():
    pygame.mixer.init()
    pygame.mixer.music.load("twilite.mp3")
    pygame.mixer.music.play()
    
game = Game()
game.start_game()