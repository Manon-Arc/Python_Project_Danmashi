import pygame
import keyboard
from classes.mob import Goblini, Wolfor, Basilisc, Animal_trainer, Hydre
from classes.dungeon import Dungeon
from classes.warrior import Warrior
from classes.mage import Mage
from classes.assassin import Assassin

class Game:
    def __init__(self):
        self.dungeon = Dungeon()
        self.player = None

    def start_game(self):
        print("Bienvenue dans le jeu !")
        self.create_player()
        jouer_musique()
        self.dungeon.generate_floors()

        for i, floor in enumerate(self.dungeon.floors):
            print(f"\n======= Étage {i + 1} =======")
            self.play_floor(floor)
            
        if keyboard.is_pressed('s'):
            pygame.mixer.music.stop()
            
        print("\nFélicitations ! Vous avez terminé le donjon.")
        
    def create_player(self):
        player_name = input("Entrez le nom de votre personnage : ")
        player_class = input("Choisissez votre classe (Guerrier, Mage, Assassin) : ")

        if player_class.lower() == "guerrier":
            self.player = Warrior(player_name, player_class)
        if player_class.lower() == "mage":
            self.player = Mage(player_name, player_class)
        if player_class.lower() == "assassin":
            self.player = Assassin(player_name, player_class)

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