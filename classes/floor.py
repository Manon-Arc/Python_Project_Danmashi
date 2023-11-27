from .mob import Goblini, Wolfor

class Floor:
    def __init__(self, level, monsters_info):
        self.level = level
        self.monsters = self.generate_monsters(monsters_info)

    def generate_monsters(self, monsters_info):
        generated_monsters = []
        for monster_type, num_monsters in monsters_info:
           
            if monster_type.lower() == "goblini":
                generated_monsters.extend([Goblini.create_default_character(f"Goblini") for _ in range(1, num_monsters + 1)])
                
            elif monster_type.lower() == "wolfor":
                generated_monsters.extend([Wolfor.create_default_character(f"Wolfor") for _ in range(1, num_monsters + 1)])
                
            else:
                print(f"Type de monstre non reconnu. Utilisation du Goblini par défaut.")
                generated_monsters.extend([Goblini.create_default_character(f"Goblini") for _ in range(1, num_monsters + 1)])
                
        return generated_monsters

