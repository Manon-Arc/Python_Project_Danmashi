from __future__ import annotations
from .character import Character
from .dice import Dice

class Warrior(Character): 
    playerMove = [
        "Déferlement",
        "Canalisation"
        ]
        
    def __init__(self, name: str, classe: str, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, dice) -> None:
        super().__init__(name, classe, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, dice)
      
    @staticmethod    
    def create_default_character(name, template="default") -> Warrior | None:
        if (template=="default"):
            return Warrior(name=name, classe="Warrior", max_health=50, attack_value=6, defense_value=3, attack_type_value=3, attack_special_value=9, touchable=0, dice=Dice(6))
        return None

    def __str__(self) -> str:
        return f"Super ! Bienvenue {self._name} le guerrier 🤺\n"
    
    def compute_damages(self, roll, target):
        print(f" {self._name} lance l'attaque déferlement sur {target.get_name()}.\n")
        return super().compute_damages(roll, target) + roll
    
    # def compute_damages_type(self, roll, target):
    #     print(f" {self._name} lance le sort Canalisation...\n")
    #     self._attack_value += self._attack_type_value
    #     return self._attack_value
    
    def compute_damages_special(self, roll, target):
        if self._current_health <= 0.3 * self._max_health:
            return 1.2 * self._attack_value 
        elif self._current_health <= 0.15 * self._max_health:
            return 1.3 * self._attack_value  
        else:
            return self._attack_value
        
    def add_special(self):
        self.playerMove.append("Colère du Berserkeur")