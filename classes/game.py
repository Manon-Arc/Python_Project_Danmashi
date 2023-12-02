import pygame
import keyboard
from .dungeon import Dungeon
from .warrior import Warrior
from .mage import Mage
from .assassin import Assassin
import pyfiglet

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
        self._dungeon = Dungeon()
        self._player = None
        self._selected = 0
        self._nbr_floor = 10

    def start_game(self):
        self.play_music()
        print("\n"*2)
        print("Bienvenue sur...")
        print(pyfiglet.figlet_format("DANMASHI !!\n"))
        print("Un jeu d'aventure en CLI !\nPréparez-vous à monter les étages d'un donjon plein de monstres.\nChaque niveau est un défi de plus en plus difficile avec des créatures vicieuses à vaincre.\nDébloquez de nouvelles compétences pour surmonter les épreuves qui vous attendent.\nOserez-vous affronter les mystères du donjon et ressortir victorieux de DANMASHI ?\nC'est le moment de tester votre courage !\n")
        self.create_player()
        self._dungeon.generate_floors(self._nbr_floor)

        for i, floor in enumerate(self._dungeon._floors):
            print(pyfiglet.figlet_format(f"\n=== Etage {i + 1} ==="))
            self.play_floor(floor)

        print(pyfiglet.figlet_format("Felicitations !"))    
        print("\nVous avez terminé le donjon.")
                
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
        self._player = self.playerClassAllows[selected_choice](player_name)
        self._selected = 0
        print("\n")
        print(str(self._player))

    def play_floor(self, floor):
        for monster in floor._monsters:
            print(f"\nUn monstre approche... \nC'est un {monster.get_name()} !")
            print(monster.ascii_design)
            while monster.is_alive() and self._player.is_alive():
                keyboard.clear_all_hotkeys()
                self.show_menu(self._player.playerMove)
                keyboard.add_hotkey('up', lambda: self.up(self._player.playerMove))
                keyboard.add_hotkey('down', lambda: self.down(self._player.playerMove))
                keyboard.add_hotkey('enter', lambda: self.get_selected_choice(self._player.playerMove))
                keyboard.wait('enter')

                print("\n")
                action = self.get_index_selected_choice(self._player.playerMove)
                self.process_player_action(action, monster)

                if monster.is_alive():
                    print("\n")
                    monster.attack(self._player)
                else :
                    print(f"{monster.get_name()} a été vaincu")
                    
                if self._player._touchable > 0:
                    self._player._touchable -= 1   
                if monster._touchable > 0:
                    monster._touchable -= 1
                    
                if self._player._count_protect > 0:
                    self._player._count_protect -= 1
                if monster._count_protect > 0:
                    monster._count_protect -= 1
                
                if self._player.is_alive():   
                    print(f"\nÉtat actuel de {self._player.get_name()}:")
                    self._player.show_healthbar()
                
                if monster.is_alive():
                    print(f"\nÉtat actuel de {monster.get_name()}:")
                    monster.show_healthbar()
                
                print("\n----------------------------------------\n")
                
            if not self._player.is_alive():
                print(pyfiglet.figlet_format("GAME OVER"))
                print("Vous avez été vaincu...\n")
                exit()

        print(f"\nVous avez vaincu tous les monstres de l'étage {floor._level}. Bravo !")
        
        if floor._level == 3:
            self._player.add_special()
            print(f"Vous avez débloqué une nouvelle compétence : {self._player.playerMove[len(self._player.playerMove)-1]} !")
        if floor._level == 5:
            self._player.add_pot()
            print(f"Vous avez récupéré une potion de vie dans votre inventaire !")
            
    def process_player_action(self, action, monster):
        if action == 0:
            self._player.attack(monster)
        elif action == 1:
            self._player.attack_type(monster)
        elif action == 2:
            self._player.attack_special(monster)
        elif action == 3:
            self._player.use_pot()
    
    def show_menu(self, datas):
        for i, option in enumerate(datas):
            selected_indicator = ">" if self._selected == i else " "
            print(f"{selected_indicator} {i + 1}. {option}")
        print("\n")
        
    def up(self, datas):
        if self._selected > 0:
            self._selected -= 1
        self.show_menu(datas)
        
    def down(self, datas):
        if self._selected < len(datas) - 1:
            self._selected += 1
        self.show_menu(datas)
        
    def get_selected_choice(self, datas):
        return datas[self._selected]  
    
    def get_index_selected_choice(self, datas):
        return self._selected
    
    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("twilite.mp3")
        pygame.mixer.music.play()
        if keyboard.is_pressed('s'):
            pygame.mixer.music.stop()