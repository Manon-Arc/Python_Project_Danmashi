from __future__ import annotations
from .character import Character
from .dice import Dice
from random import randint

class Warrior(Character): 
    playerMove = [
        "Déferlement",
        "Canalisation"
        ]
        
    def __init__(self, name: str, classe: str, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, count_protect, dice) -> None:
        super().__init__(name, classe, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, count_protect, dice)
      
    @staticmethod    
    def create_default_character(name, template="default") -> Warrior | None:
        if (template=="default"):
            return Warrior(name=name, classe="Warrior", max_health=50, attack_value=4, defense_value=2, attack_type_value=6, attack_special_value=3, touchable=0, count_protect=0, dice=Dice(4))
        return None

    def __str__(self) -> str:
        return f"Super ! Bienvenue {self._name} le guerrier 🤺\n"
    
    def compute_damages(self, roll, target):
        print(f"{self._name} lance l'attaque Déferlement !\n")
        return super().compute_damages(roll, target) + roll
    
    def compute_damages_type(self, roll, target):
        print(f"{self._name} lance le sort Canalisation...\n")
        if self._attack_value < 7:
            self._attack_value += self._attack_type_value
        else:
            print("Ton attaque a déjà été augmentée, dommage tu perds un tour ^^")
        return 0
    
    def compute_damages_special(self, roll, target):
        blesse = False
        print(f"{self._name} déclenche sa Colère du Berserkeur ! au risque d'être blessé...\n")
        if self._current_health <= 10:
            self._current_health = round(self._max_health * 0.3)
           
        if randint(1,2) == 1:
            self._current_health -= 4
            blesse = True
             
        if self._current_health <= 0.4 * self._max_health:
            return int(round(1.5 * self._attack_special_value)), blesse
        
        elif self._current_health <= 0.2 * self._max_health:
            return int(round(2 * self._attack_special_value)), blesse
        
        else:
            return self._attack_special_value, blesse
        
    def add_special(self):
        if not "Colère du Berserkeur" in self.playerMove:
            self.playerMove.append("Colère du Berserkeur")