from character import Character
from dice import Dice

class Assassin(Character):
    playerMove = [
        "Attack",
        "Attaque spe"
        ]
    
    def __init__(self, name: str) -> None:
        super().__init__(name, "Assassin")
        self._max_health = 35
        self._attack_value = 6
        self._defense_value = 3
        self._attack_type_value = 10
        self._defense_value = 3
        self._dice = Dice(4)
        
    def __str__(self) -> str:
        return f"Super ! Bienvenue {self._name} l'assassin 🥷"
    
    def compute_damages(self, roll, target):
        basic_attack = self._attack_value - 3
        print(f"{self._name} lancement des hachettes des ombres sur {target.get_name()} ")
        return super().compute_damages(roll, target)
