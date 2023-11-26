from __future__ import annotations
from character import Character
from dice import Dice

    
class Goblini(Character):
    def __init__(self, name: str="Goblini") -> None:
        super().__init__(name, "Mob")
        self._max_health = 10
        self._current_health = self._max_health
        self._attack_value = 3
        self._dice = Dice(6)

class Wolfor(Character):
    def __init__(self, name: str="Wolfer") -> None:
        super().__init__(name, "Mob")
        self._max_health = 20
        self._current_health = self._max_health
        self._attack_value = 4
        self._dice = Dice(6)

class Basilisc(Character):
    def __init__(self, name: str="Basilisc") -> None:
        super().__init__(name, "Mob")
        self._max_health = 25
        self._current_health = self._max_health
        self._attack_value = 6
        self._defense_value = 2
        self._dice = Dice(6)

class Animal_trainer(Character):
    def __init__(self, name: str="Animal trainer") -> None:
        super().__init__(name, "Mob")
        self._max_health = 12
        self._current_health = self._max_health
        self._attack_value = 4
        self._dice = Dice(6)


class Hydre(Character):
    def __init__(self, name: str="Hydre") -> None:
        super().__init__(name, "Mob")
        self._max_health = 30
        self._current_health = self._max_health
        self._attack_value = 8
        self._defense_value = 3
        self._dice = Dice(6)