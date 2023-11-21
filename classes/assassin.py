from character import Character
from dice import Dice

class Assassin(Character):
    
    def __init__(self, name: str, max_health: int, attack: int, attack_type: int, attack_special: int, defense: int, dice) -> None:
        super().__init__(name, max_health, attack, attack_type, attack_special, defense, dice)
        self._name = "Assassin"
        self._max_health = 35
        self._attack_value = 6
        self._defense_value = 3
    
    def compute_damages(self, roll, target):
        basic_attack = self.attack - 3
        print(f"{self._name} lancement des hachettes des ombres sur {target.get_name()} ")
        return super().compute_damages(roll, target)
