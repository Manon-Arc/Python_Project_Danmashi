import random
from .floor import Floor

class Dungeon:
    def __init__(self):
        self._floors = []
        
    basics_monsters = ["Goblini", "Wolfor"]
    elaborated_monsters = ["Animal_trainer", "Vampire"]
    boss_monsters = ["Basilisc", "Hydre"]
    
    def generate_floors(self, num_floor):
        for i in range(1, num_floor + 1):
            monsters_info = self.generate_specific_configuration(i)
            self._floors.append(Floor(i, monsters_info))

    def generate_specific_configuration(self, floor_number):
        if floor_number%5 == 0:
            return [(random.choice(self.boss_monsters), 1)]
        elif floor_number%2 == 0:
            return [(random.choice(self.basics_monsters), 1), (random.choice(self.elaborated_monsters), 1)]
        elif floor_number%3 == 0:
            return [(random.choice(self.elaborated_monsters), 1), (random.choice(self.elaborated_monsters), 1)]
        else:
            return [(random.choice(self.basics_monsters), 2)]
