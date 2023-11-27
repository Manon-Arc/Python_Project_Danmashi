from __future__ import annotations
from .character import Character
from .dice import Dice

class Mage(Character):
    playerMove = [
        "Boule de feu",
        "Protego"
        ]
        
    def __init__(self, name: str, classe: str, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, dice) -> None:
        super().__init__(name, classe, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, dice)
        
    @staticmethod
    def create_default_character(name, template="default") -> Mage | None:
        if (template=="default"):
            return Mage(name=name, classe="Mage", max_health=50, attack_value=5, defense_value=4, attack_type_value=3, attack_special_value=4, touchable=0, dice=Dice(6))
        return None
        
    def __str__(self) -> str:
        return f"Super ! Bienvenue {self._name} le mage 🧙\n"

    def compute_damages(self, roll, target):
        print(f" {self._name} lance l'attaque Boule de feu sur {target.get_name()}.\n")
        return super().compute_damages(roll, target)

    def compute_damages_type(self, roll, attacker):
        print(f" {self._name} se protège grâce à son sort Protego {attacker.get_name()}.\n")
        self.is_touchable += 2
    
    # soit le rayon rend insensible 1 tour + dégat
    # def compute_damages_special(self, roll, target):
    #     print(f" {self._name} lance le sort Rayon cosmique sur {target.get_name()}.\n")
    #     self.is_touchable += 1
    #     return super().compute_damages_special(roll, target)

    #  OU ALORS

    # soit le rayon donne du shield en plus + dégat
    # def compute_damages_special(self, roll, target):
    #     print(f" {self._name} lance le sort Rayon cosmique sur {target.get_name()}.\n")
    #     for i in range(0, 1):
    #       self.defense_value += 2 + roll
    #       i += 1
    #     return super().compute_damages_special(roll, target)

    def compute_wounds(self, damages, roll, attacker):
        if super().compute_wounds(damages, roll, attacker) - roll <= 0:
            return 0
        else :
            return super().compute_wounds(damages, roll, attacker) - roll
    
    def add_special(self):
        return self.playerMove.append("Rayon cosmique")
