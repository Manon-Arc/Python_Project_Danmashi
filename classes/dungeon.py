from .floor import Floor

class Dungeon:
    def __init__(self):
        self.floors = []

    def generate_floors(self):
    
        floor_configurations = [
            [("Goblini", 3)],
            [("Wolfor", 1)],
            [("Goblini", 1), ("Wolfor", 1)]
        ]

        for i, monsters_info in enumerate(floor_configurations, start=1):
            self.floors.append(Floor(i, monsters_info))
