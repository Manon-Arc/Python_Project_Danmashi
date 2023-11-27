from __future__ import annotations
from .character import Character
from .dice import Dice
from random import random

class Assassin(Character):
    playerMove = [
        "Coup de dague",
        "hachettes des ombres"
        ]
        
    def __init__(self, name: str, classe: str, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, dice) -> None:
        super().__init__(name, classe, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, dice)
        
    @staticmethod
    def create_default_character(name, template="default") -> Assassin | None:
        if (template=="default"):
            return Assassin(name=name, classe="Assassin", max_health=35, attack_value=6, defense_value=3, attack_type_value=10, attack_special_value=0, touchable=0, dice=Dice(4))
        return None
        
    def __str__(self) -> str:
        return f"Super ! Bienvenue {self._name} l'assassin 🥷"
    
    def compute_damages(self, roll, target):
        print(f"{self._name} donne un coup de dague sur {target.get_name()} ")
        return super().compute_damages(roll, target)

    def compute_damages_type(self, roll, target):
        type_attack = self._attack_value
        print(f" {self._name} lancement des hachettes des ombres sur {target.get_name()}")
        i == 2
        for i in range : Dice()
        type_attack += 3
        i += 1
        return type_attack
    
    def compute_damages_special(self, target):
        print(f"{self._name} utilise son écran de fumée 🌫️ qui rend confus {target.get_name()} et le fait rater tout ces coups")
        self._is_touchable += 2

    def esquive(self):
        if random(1 - 4) <= 4 :
            self._is_touchable += 1
            
    def add_special(self):
        self.playerMove.append("écran de fumée")
            