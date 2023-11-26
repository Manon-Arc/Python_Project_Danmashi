import pygame
import keyboard
from character import Character
from dungeon import Dungeon
from warrior import Warrior
from mage import Mage
from assassin import Assassin
from mob import Goblini, Wolfor, Basilisc, Animal_trainer, Hydre
import os

class Game:
    playerClasseAllow = [
        "Mage",
        "Assassin",
        "Warrior"
        ]
    
    def __init__(self):
        self.dungeon = Dungeon()
        self.player = None
        self.selected = 0

    def start_game(self):
        print("Bienvenue sur Danmashi !")
        self.create_player()
        self.dungeon.generate_floors()

        for i, floor in enumerate(self.dungeon.floors):
            print(f"\n======= Étage {i + 1} =======")
            self.play_floor(floor)
            
        print("\nFélicitations ! Vous avez terminé le donjon.")
        
#    def create_player(self):
#        player_name = input("Entrez le nom de votre personnage : ")
#        player_class = ""
#        while player_class == "":
#            player_class = input("Choisissez votre classe (Guerrier, Mage, Assassin) : ").capitalize()
#            if player_class in self.playerClasseAllow:
#                self.player = eval(f"{player_class}('{player_name}')")
#            else:
#                print("Classe invalide. Veuillez choisir parmi :", end=" ") 
#                for index,classe in enumerate(self.playerClasseAllow):
#                    if index < len(self.playerClasseAllow)-1:
#                        print(classe, end=", ")
#                    else:
#                        print(classe)
#                player_class = ""
                
    def create_player(self):
        player_name = input("Entrez le nom de votre personnage : ")
        print("Choississez votre classe :")
        self.show_menu(self.playerClasseAllow)
        keyboard.add_hotkey('up',lambda: self.up(self.playerClasseAllow))
        keyboard.add_hotkey('down',lambda: self.down(self.playerClasseAllow))
        keyboard.add_hotkey('enter',lambda: self.get_selected_choice(self.playerClasseAllow))
        keyboard.wait('enter')
        selected_choice = self.get_selected_choice(self.playerClasseAllow)
        self.player = eval(f"{selected_choice}('{player_name}')")
        print(str(self.player))

    def play_floor(self, floor):
            print(f"Vous êtes à l'étage {floor.level}. Préparez-vous à combattre !")

            for monster in floor.monsters:
                print(f"\nUn monstre approche : {monster.get_name()} !")

                while monster.is_alive() and self.player.is_alive():
                    self.show_menu(self.player.playerMove)
                    self.bind_keyboard_actions()

                    if not keyboard.is_pressed('enter'):
                        continue

                    action = self.get_index_selected_choice(self.player.playerMove)
                    self.process_player_action(action, monster)

                    if monster.is_alive():
                        monster.attack(self.player)

                    print(f"\nÉtat actuel de {self.player.get_name()}:")
                    self.player.show_healthbar()

                    print(f"État actuel de {monster.get_name()}:")
                    monster.show_healthbar()

                if not self.player.is_alive():
                    print("Vous avez été vaincu. Game Over.")
                    break

            print(f"\nVous avez vaincu tous les monstres de l'étage {floor.level}. Bravo !")

    def process_player_action(self, action, monster):
        if action == 1:
            self.player.attack(monster)
        elif action == 2:
            self.player.attack_special(monster)
        elif action == 3:
            self.player.attack_type(monster)

    def bind_keyboard_actions(self):
        keyboard.add_hotkey('up', lambda: self.up(self.player.playerMove))
        keyboard.add_hotkey('down', lambda: self.down(self.player.playerMove))
        keyboard.add_hotkey('enter', lambda: self.get_selected_choice(self.player.playerMove))
        keyboard.wait('enter')
    
    def show_menu(self, list):
        os.system('cls||clear')
        for i, option in enumerate(list):
            print("{1} {0}. {2} {3}".format(i + 1, ">" if self.selected == i else " ", option, "<" if self.selected == i else " "))
            
    def up(self, list):
        if self.selected > 0:
            self.selected -= 1
        self.show_menu(list)
        
    def down(self, list):
        if self.selected < len(list) - 1:
            self.selected += 1
        self.show_menu(list)
        
    def get_selected_choice(self, list):
        return list[self.selected]  
    
    def get_index_selected_choice(self, list):
        return self.selected
    

def jouer_musique():
    pygame.mixer.init()
    pygame.mixer.music.load("twilite.mp3")
    pygame.mixer.music.play()
    
game = Game()
game.start_game()