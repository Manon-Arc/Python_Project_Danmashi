from __future__ import annotations

class Mob:
    
    def __init__(self, name:str, max_health = 10, attack = 3, defense = 0) -> None:
        self._name = name
        self._max_health = max_health
        self._current_health = max_health
        self._attack_value = attack
        self._defense_value = defense
        
    def show_healthbar(self):
        missing_hp = self._max_health - self._current_health
        healthbar = f"[{'♥'* self._current_health}{'♡' * (missing_hp)}]{self._current_health}/{self._max_health} hp]"  
        print(healthbar)
    
    def is_alive(self) -> bool:
        return self._current_health > 0


class Goblini(Mob):
    def __init__(self, name: str, max_health: int, attack: int, defense: int) -> None:
        super().__init__(name, max_health, attack, defense)
        self._name = "Goblini"

class Wolfor(Mob):
    def __init__(self, name: str, max_health: int, attack: int, defense: int) -> None:
        super().__init__(name, max_health, attack, defense)
        self._name = "Wolfor"
        self._max_health = 20
        self._attack_value = 4

class Basilisc(Mob):
    def __init__(self, name: str, max_health: int, attack: int, defense: int) -> None:
        super().__init__(name, max_health, attack, defense)
        self._name = "Basilisc"
        self._max_health = 25
        self._attack_value = 6
        self._defense_value = 2

class Animal_trainer(Mob):
    def __init__(self, name: str, max_health: int, attack: int, defense: int) -> None:
        super().__init__(name, max_health, attack, defense)
        self._name = "Animal_trainer"
        self._max_health = 12
        self._attack_value = 4

class Hydre(Mob):
    def __init__(self, name: str, max_health: int, attack: int, defense: int) -> None:
        super().__init__(name, max_health, attack, defense)
        self._name = "Hydre"
        self._max_health = 30
        self._attack_value = 8
        self._defense_value = 3
