from __future__ import annotations
from .dice import Dice

class Character:

    def __init__(self, name:str, classe:str, max_health:int, attack_value:int, defense_value:int, attack_type_value:int, attack_special_value:int, touchable:int, count_protect:int, dice:Dice) -> None:
        self._name = name
        self._classe = classe
        self._max_health = max_health
        self._current_health = self._max_health
        self._attack_value = attack_value
        self._defense_value = defense_value
        self._attack_type_value = attack_type_value
        self._attack_special_value = attack_special_value
        self._touchable = touchable
        self._count_protect = count_protect
        self._dice = dice
        
    @staticmethod
    def create_default_character(name, template="default") -> Character | None:
        if (template=="default"):
            return Character(name=name, classe="Character", max_health=0, attack_value=0, defense_value=0, attack_type_value=0, attack_special_value=0, touchable=0, dice=Dice(6))
        return None  
     
    def __str__(self) -> str:
        return f"I'm {self._name} the character with attack : {self._attack_value} and defense : {self._defense_value}"
    
    def get_name(self):
        return self._name
    
    def get_classe(self):
        return self._classe
    
    def is_alive(self) -> bool:
        return self._current_health > 0
    
    def is_touchable(self) -> bool:
        return self._touchable == 0
        
    def compute_damages(self, roll, target):
        return self._attack_value 
    
    def compute_damages_type(self, roll, target):
        return self._attack_type_value
    
    def compute_damages_special(self, roll, target):
        return self._attack_special_value

    def attack(self, target: Character):
        if not self.is_alive():
            return
        roll = self._dice.roll()
        damages = self.compute_damages(roll, target)
        if target.is_touchable() and damages != 0:
            print(f"⚔️ {self._name} attaque {target.get_name()} avec {damages} de puissance !")
            target.defense(damages, self)
        else:
            if target.get_classe() == "Mage":
                print(f"{target._name} a encaissé l'attaque grâce à Protégo 🛡️")
            elif target.get_classe() == "Assassin":
                print(f"{target._name} a esquivé l'attaque grâce à son écran de fumée 🛡️")
            elif target.get_classe() == "Vampire":
                print(f"{target._name} esquive l'attaque grâce à un battement d'aile 🛡️")
            
    def attack_type(self, target: Character):
        if not self.is_alive():
            return
        roll = self._dice.roll()
        damages_type = self.compute_damages_type(roll, target)
        if target.is_touchable() and damages_type != 0:
            print(f"⚔️ {self._name} attaque {target.get_name()} avec {damages_type} de puissance !")
            target.defense(damages_type, self)
        else:
            if target.get_classe() == "Mage":
                print(f"{target._name} a encaissé l'attaque grâce à Protégo 🛡️")
            elif target.get_classe() == "Assassin":
                print(f"{target._name} a esquivé l'attaque grâce à son écran de fumée 🛡️")
            elif target.get_classe() == "Vampire":
                print(f"{target._name} esquive l'attaque grâce à un battement d'aile 🛡️")
            
    def attack_special(self, target: Character):
        if not self.is_alive():
            return
        roll = self._dice.roll()
        damages_special, blesse = self.compute_damages_special(roll, target)
        if target.is_touchable() and damages_special != 0:
            print(f"⚔️ {self._name} attaque {target.get_name()} avec {damages_special} de puissance !")
            if blesse == True:
                print(f"{self._name} a pris 5 dégâts de recul... dommage")
            target.defense(damages_special, self)
        else:
            if target.get_classe() == "Mage":
                print(f"{target._name} a encaissé l'attaque grâce à Protégo 🛡️")
            elif target.get_classe() == "Assassin":
                print(f"{target._name} a esquivé l'attaque grâce à son écran de fumée 🛡️")
            elif target.get_classe() == "Vampire":
                print(f"{target._name} esquive l'attaque grâce à un battement d'aile 🛡️")
            
    def compute_wounds(self, damages, roll):
        return damages - self._defense_value 
    
    def defense(self, damages, attacker):
        roll = self._dice.roll()
        wounds = self.compute_wounds(damages, roll)
        print(f"🛡️ {self._name} a prit {wounds} dégâts de l'attaque de {attacker.get_name()} grâce à sa défense !")
        self.decrease_health(wounds)
        
    def decrease_health(self, amount):
        if (self._current_health - amount) < 0 :
            amount = self._current_health
        self._current_health -= amount
        
    def show_healthbar(self):
        missing_hp = self._max_health - self._current_health
        healthbar = f"[{'♥'* self._current_health}{'♡' * (missing_hp)}]{self._current_health}/{self._max_health} hp]"  
        print(healthbar)

    def regenerate(self):
        self._current_health = self._max_health
        
    def res_char(self):
        self._touchable = 0
        self._count_protect = 0
        return

    def add_special(self):
        return
    
    def add_pot(self):
        if not "Potion de vie" in self.playerMove:
            self.playerMove.append("Potion de vie")
            
    def use_pot(self):
        self.regenerate()
        print(f"{self._name} à récupéré toute sa vie !")
        if "Potion de vie" in self.playerMove:
            self.playerMove.remove("Potion de vie")
            