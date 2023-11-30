from .mob import Goblini, Wolfor, Basilisc, Animal_trainer, Hydre, Vampire

class Floor:
    def __init__(self, level, monsters_info):
        self._level = level
        self._monsters = self.generate_monsters(monsters_info)

    def generate_monsters(self, monsters_info):
        generated_monsters = []
        for monster_type, num_monsters in monsters_info:
           
            if monster_type.lower() == "goblini":
                generated_monsters.extend([Goblini.create_default_character(f"Goblini") for _ in range(1, num_monsters + 1)])
                
            elif monster_type.lower() == "wolfor":
                generated_monsters.extend([Wolfor.create_default_character(f"Wolfor") for _ in range(1, num_monsters + 1)])
                
            elif monster_type.lower() == "basilisc":
                generated_monsters.extend([Basilisc.create_default_character(f"Basilisc") for _ in range(1, num_monsters + 1)])
                
            elif monster_type.lower() == "animal_trainer":
                generated_monsters.extend([Animal_trainer.create_default_character(f"Animal trainer") for _ in range(1, num_monsters + 1)])
                
            elif monster_type.lower() == "hydre":
                generated_monsters.extend([Hydre.create_default_character(f"Hydre") for _ in range(1, num_monsters + 1)])
                
            elif monster_type.lower() == "vampire":
                generated_monsters.extend([Vampire.create_default_character(f"Vampire") for _ in range(1, num_monsters + 1)])

            else:
                print(f"Type de monstre non reconnu. Utilisation du Goblini par défaut.")
                generated_monsters.extend([Goblini.create_default_character(f"Goblini") for _ in range(1, num_monsters + 1)])
                
        return generated_monsters