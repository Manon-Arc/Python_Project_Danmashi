from character import Character
from dice import Dice

class Warrior(Character): 

    def __init__(self, name, max_health, attack, attack_type, attaque_special, defense, dice):
        super().__init__(name, defense, max_health, attack, attack_type, attaque_special, dice)
        self._max_health = 50
        self._health = max_health
        self._attack_value = 6
        self._attack_type_value = 3
        self._defense_value = 3
        self._dice = Dice(4)

    def compute_damages(self, roll, target):
        print(f" {self._name} lance l'attaque déferlement sur {target.get_name()}.")
        return super().compute_damages(roll, target) + roll
    
    def compute_damages_type(self, roll, target):
        print(f" {self._name} lance le sort maîtrise de soi...")
        self._attack_value += self._attack_type_value
        return self._attack_value
    
    
    def compute_damages_special(self, roll, target):
        if self._current_health <= 0.3 * self._max_health:
            return 1.2 * self._attack_value 
        elif self._current_health <= 0.15 * self._max_health:
            return 1.3 * self._attack_value  
        else:
            return self._attack_value

    