import pygame
import keyboard
from .dungeon import Dungeon
from .warrior import Warrior
from .mage import Mage
from .assassin import Assassin
#import os
import pyfiglet
from time import sleep

class Game:
    playerClasseList = [
        "Mage",
        "Assassin",
        "Guerrier"
        ]

    playerClassAllows = {
        "Guerrier": Warrior.create_default_character,
        "Mage" : Mage.create_default_character,
        "Assassin" : Assassin.create_default_character,
    }
    
    def __init__(self):
        self.dungeon = Dungeon()
        self.player = None
        self.selected = 0

    def start_game(self):
        self.play_music()
        print("\n"*2)
        print("Bienvenue sur le meilleur jeu de tout les temps, l'équipe 7 va vous présenter: \nAttention roulement de tambour...")
        print(pyfiglet.figlet_format("DANMASHI !!"))
        self.create_player()
        self.dungeon.generate_floors()

        for i, floor in enumerate(self.dungeon.floors):
            print(pyfiglet.figlet_format(f"\n=== Etage {i + 1} ==="))
            self.play_floor(floor)

        print(pyfiglet.figlet_format("Felicitations !"))    
        print("\nVous avez terminé le donjon.")
        
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
        if player_name == "":
            player_name = "player"
        print("Choississez votre classe :")
        self.show_menu(self.playerClasseList)
        keyboard.add_hotkey('up',lambda: self.up(self.playerClasseList))
        keyboard.add_hotkey('down',lambda: self.down(self.playerClasseList))
        keyboard.add_hotkey('enter',lambda: self.get_selected_choice(self.playerClasseList))
        keyboard.wait('enter')
        selected_choice = self.get_selected_choice(self.playerClasseList)
        self.player = self.playerClassAllows[selected_choice](player_name)
        self.selected = 0
        print(str(self.player))

    def play_floor(self, floor):
        for monster in floor.monsters:
            print(f"\nUn monstre approche : \nC'est un {monster.get_name()} !")
            print(monster.ascii_design)
            while monster.is_alive() and self.player.is_alive():
                keyboard.clear_all_hotkeys()
                self.show_menu(self.player.playerMove)
                keyboard.add_hotkey('up', lambda: self.up(self.player.playerMove))
                keyboard.add_hotkey('down', lambda: self.down(self.player.playerMove))
                keyboard.add_hotkey('enter', lambda: self.get_selected_choice(self.player.playerMove))
                keyboard.wait('enter')

                action = self.get_index_selected_choice(self.player.playerMove)
                self.process_player_action(action, monster)

                if monster.is_alive():
                    monster.attack(self.player)
                else :
                    print(f"{monster.get_name()} a été vaincu")
                    
                if self.player._touchable > 0:
                    self.player._touchable -= 1
                    
                print(f"\nÉtat actuel de {self.player.get_name()}:")
                self.player.show_healthbar()

                print(f"État actuel de {monster.get_name()}:")
                monster.show_healthbar()

            if not self.player.is_alive():
                print(pyfiglet.figlet_format("GAME OVER"))
                print("Vous avez été vaincu...")
                break

        print(f"\nVous avez vaincu tous les monstres de l'étage {floor.level}. Bravo !")
        
        if floor.level == 3:
            self.player.add_special()
            print(f"Vous avez débloqué une nouvelle compétence : {self.player.playerMove[len(self.player.playerMove)-1]} !")

    def process_player_action(self, action, monster):
        if action == 0:
            self.player.attack(monster)
        elif action == 1:
            self.player.attack_type(monster)
        elif action == 2:
            self.player.attack_spe(monster)
    
    def show_menu(self, datas):
        #os.system("clear||cls")
        for i, option in enumerate(datas):
            print("{1} {0}. {2} {3}".format(i + 1, ">" if self.selected == i else " ", option, "<" if self.selected == i else " "))
            
    def clear_term(self, datas):
        print('\r' + ' ' * len(str(datas)), end='', flush=True)
        sleep(0.5)
        
    def up(self, datas):
        if self.selected > 0:
            self.selected -= 1
        self.show_menu(datas)
        
    def down(self, datas):
        if self.selected < len(datas) - 1:
            self.selected += 1
        self.show_menu(datas)
        
    def get_selected_choice(self, datas):
        return datas[self.selected]  
    
    def get_index_selected_choice(self, datas):
        return self.selected
    
    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("twilite.mp3")
        pygame.mixer.music.play()
        if keyboard.is_pressed('s'):
            pygame.mixer.music.stop()