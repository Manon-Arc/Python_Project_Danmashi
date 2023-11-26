from __future__ import annotations
from dice import Dice 

class Character:
    def __init__(self, name:str, classe:str) -> None:
        self._name = name
        self._classe = classe
        self._max_health = 0
        self._current_health = self._max_health
        self._attack_value = 0
        self._defense_value = 0
        self._attack_type_value = 0
        self._attack_special_value = 0
        self._dice = Dice(6)
        
    def __str__(self) -> str:
        return f"I'm {self._name} the character with attack : {self._attack_value} and defense : {self._defense_value}"
    
    def get_name(self):
        return self._name
    
    def is_alive(self) -> bool:
        return self._current_health > 0
    
    def decrease_health(self, amount):
        if (self._current_health - amount) < 0 :
            amount = self._current_health
        self._current_health -= amount
        self.show_healthbar()
        
    def show_healthbar(self):
        missing_hp = self._max_health - self._current_health
        healthbar = f"[{'♥'* self._current_health}{'♡' * (missing_hp)}]{self._current_health}/{self._max_health} hp]"  
        print(healthbar)
        
    def compute_damages(self, roll, target):
        return self._attack_value 
    
    def compute_damages_type(self, roll):
        return self._attack_type_value
    
    def compute_damages_special(self, roll):
        return self._attack_special_value

    def attack(self, target: Character):
        if not self.is_alive():
            return
        roll = self._dice.roll()
        damages = self.compute_damages(roll, target)
        print(f"⚔️ {self._name} attack {target.get_name()} with {damages} damages in your face ! (attack: {self._attack_value} + roll: {roll})")
        target.defense(damages, self)
        
    def attack_type(self, target: Character):
        if not self.is_alive():
            return
        roll = self._dice.roll()
        damages_type = self.compute_damages_type(roll, target)
        print(f"⚔️ {self._name} attack {target.get_name()} with {damages_type} damages in your face ! (attack: {self._attack_type_value} + roll: {roll})")
        target.defense(damages_type, self)
        
    def attack_special(self, target: Character):
        if not self.is_alive():
            return
        roll = self._dice.roll()
        damages_special = self.compute_damages_special(roll, target)
        print(f"⚔️ {self._name} attack {target.get_name()} with {damages_special} damages in your face ! (attack: {self._attack_special_value} + roll: {roll})")
        target.defense(damages_special, self)
    
    def compute_wounds(self, damages, roll, attacker):
        return damages - self._defense_value - roll
    
    def defense(self, damages, attacker):
        roll = self._dice.roll()
        wounds = self.compute_wounds(damages, roll, attacker)
        print(f"🛡️ {self._name} take {wounds} wounds from {attacker.get_name()} in his face ! (damages: {damages} - defense: {self._defense_value} - roll: {roll})")
        self.decrease_health(wounds)

    def regenerate(self):
        self._current_health = self._max_health
