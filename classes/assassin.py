from __future__ import annotations
from .character import Character
from .dice import Dice

class Assassin(Character):
    playerMove = [
        "Coup de dague",
        "Hachettes des ombres"
        ]
        
    def __init__(self, name: str, classe: str, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, count_protect, dice) -> None:
        super().__init__(name, classe, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, count_protect, dice)
        
    @staticmethod
    def create_default_character(name, template="default") -> Assassin | None:
        if (template=="default"):
            return Assassin(name=name, classe="Assassin", max_health=40, attack_value=6, defense_value=1, attack_type_value=3, attack_special_value=0, touchable=0, count_protect=0, dice=Dice(4))
        return None
        
    def __str__(self) -> str:
        return f"Super ! Bienvenue {self._name} l'assassin 🥷\n"
    
    def compute_damages(self, roll, target):
        print(f"{self._name} donne un coup de dague !\n")
        return super().compute_damages(roll, target)

    def compute_damages_type(self, roll, target):
        type_attack_damages = self._attack_value
        print(f"{self._name} lance {roll} hachettes des ombres !\n")
        for _ in range(2, roll):
            type_attack_damages += self._attack_type_value
        return type_attack_damages
    
    def compute_damages_special(self, roll, target):
        if self._count_protect == 0:
            print(f"{self._name} utilise son écran de fumée 😶‍🌫️ qui rend confus {target.get_name()}\n")
            self._touchable += 2
            self._count_protect += 4
        else:
            print(f"{self._name} ne peut utiliser son écran de fumée que tous les 3 tours... dommage ")
        return 0, False
    
    def defense(self, damages, attacker):
        if self._dice.roll() == 1:
            print(f"{self._name} a esquivé l'attaque avec habilité")
            self.decrease_health(0)
        else:
            return super().defense(damages, attacker)
            
    def add_special(self):
        if not "Ecran de fumée" in self.playerMove:
            self.playerMove.append("Ecran de fumée")
    