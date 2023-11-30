from __future__ import annotations
from .character import Character
from .dice import Dice
  
class Goblini(Character):
        
    def __init__(self, name: str, classe: str, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, dice) -> None:
        super().__init__(name, classe, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, dice)
        
    @staticmethod
    def create_default_character(name, template="default") -> Goblini | None:
        if (template=="default"):
            return Goblini(name=name, classe="Goblini", max_health=10, attack_value=3, defense_value=0, attack_type_value=0, attack_special_value=0, touchable=0, dice=Dice(6))
        return None
    def attack(self, target: Character):
        print(f"{self.get_name()} lance l'attaque Fureur du gobelin !\n")
        return super().attack(target)
    
    ascii_design = r'''
             ,      ,
            /(.-""-.)\
        |\  \/      \/  /|
        | \ / =.  .= \ / |
        \( \   o\/o   / )/
         \_, '-/  \-' ,_/
           /   \__/   \
           \ \__/\__/ /
         ___\ \|--|/ /___
       /`    \      /    `\
      /       '----'       \
'''

class Wolfor(Character):
  
    def __init__(self, name: str, classe: str, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, dice) -> None:
        super().__init__(name, classe, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, dice)
        
    @staticmethod
    def create_default_character(name, template="default") -> Wolfor | None:
        if (template=="default"):
            return Wolfor(name=name, classe="Wolfor", max_health=15, attack_value=4, defense_value=0, attack_type_value=0, attack_special_value=0, touchable=0, dice=Dice(6))
        return None
    
    def attack(self, target: Character):
        print(f"{self.get_name()} lance l'attaque Morsure !\n")
        return super().attack(target)
    
    ascii_design = r'''
                                  __
                                .d$$b
                              .' TO$;\
                             /  : TP._;
                            / _.;  :Tb|
                           /   /   ;j$j
                       _.-"       d$$$$
                     .' ..       d$$$$;
                    /  /P'      d$$$$P. |\
                   /   "      .d$$$P' |\^"l
                 .'           `T$P^"""""  :
             ._.'      _.'                ;
          `-.-".-'-' ._.       _.-"    .-"
        `.-" _____  ._              .-"
       -(.g$$$$$$$b.              .'
         ""^^T$$$P^)            .(:
           _/  -"  /.'         /:/;
        ._.'-'`-'  ")/         /;/;
     `-.-"..--""   " /         /  ;
    .-" ..--""        -'          :
    ..--""--.-"         (\      .-(\
      ..--""              `-\(\/;`
        _.                      :
                                ;`-
'''
    
class Animal_trainer(Character):

    def __init__(self, name: str, classe: str, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, dice) -> None:
        super().__init__(name, classe, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, dice)
        
    @staticmethod
    def create_default_character(name, template="default") -> Animal_trainer | None:
        if (template=="default"):
            return Animal_trainer(name=name, classe="Animal_trainer", max_health=15, attack_value=5, defense_value=1, attack_type_value=0, attack_special_value=0, touchable=0, dice=Dice(6))
        return None
    
    def attack(self, target: Character):
        print(f"{self.get_name()} lance l'attaque Domination bestiale !\n")
        return super().attack(target)
    
    ascii_design = r'''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⠤⠤⠴⠶⠒⠋⠉⠁⠀⠀⢀⣴⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⠴⠒⠒⠋⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣯⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣀⠴⠚⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡞⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⡼⠁⠀⠀⢀⣀⣀⣀⣀⣤⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⣀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣓⢤⣤⡤⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢩⣿⣿⡿⠟⢛⣛⢿⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢻⡍⢿⡯⠁⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⡇⢰⣾⢸⡈⣆⢹⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⡇⠀⡇⠀⢀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠉⠉⠛⢧⢈⣧⣧⣷⠿⣎⣿⡘⣿⣿⣿⡿⠛⡻⣿⣿⣿⣿⣿⣿⣧⠰⠥⠴⡟⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠈⠳⣦⠘⡞⡎⠛⢢⡄⢹⣸⣇⡿⠛⢉⣵⣶⣷⣿⣿⣿⣿⣿⡻⣝⡛⢿⡟⠁⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠸⡀⠀⢀⡄⣹⡇⣣⠹⣸⣿⠿⢾⠉⣀⣤⣖⣋⣾⣷⣾⣿⣿⣿⠻⣝⣎⡐⡄⣁⢱⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢳⣀⠀⠀⠀⠀⠀⠀⠀⣤⣾⠥⠿⢷⠛⣋⣩⣤⠶⣾⡿⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣧⣷⢸⡻⠇⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⣉⣉⣏⣉⣉⣉⣏⣉⣭⣤⠴⠶⠞⠛⠋⣉⣤⠾⣫⣴⣿⣟⣛⡧⣦⣽⣿⣿⣿⠋⣿⣿⣿⣿⣿⣀⠳⣤⠆⣀⡀⠀⠀
    ⠀⠀⠀⠀⠀⢠⠎⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⣀⣠⣶⡾⣋⣷⣿⣏⣻⣷⠿⣗⣲⡾⣿⣿⣿⡇⣸⣿⣿⢹⣿⣷⠺⢍⠭⠟⠉⠀⠀⢀
    ⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⣀⣀⣀⣤⣴⣶⣾⣿⣿⣫⣷⣾⣿⡷⡿⡿⢿⣋⡏⣀⣼⣿⣿⣿⣿⣿⠙⣿⣿⣾⢿⠻⣷⠈⡇⠀⠀⡠⠒⢉
    ⠀⠀⣠⠎⠀⠀⠀⠈⠙⠛⠛⠛⠛⣛⣻⡿⢿⣿⣿⡿⠛⣺⣯⣾⣛⣧⠤⠞⠊⠁⠀⢸⣿⣿⣿⣿⣾⠿⡟⣿⣌⣧⣹⡧⠜⣦⠞⢀⣴⣾
    ⣠⠾⠁⠀⠀⠀⠀⢀⣀⣤⣶⠾⠟⣋⣵⣾⣿⣿⣿⠟⢿⡟⠁⠀⠙⢏⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⠀⣠⡾⣿⣿⣿⣿⣷⣘⡏⣰⣿⣿⣿
    ⠋⢀⣀⣤⣴⠶⠟⢛⣋⡭⠴⠚⠋⢻⣿⣿⣿⠿⠿⡆⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⡟⣾⣿⣧⣿⠀⣶⣶⣶⣾⣿⣿⣿⣿⣿
    ⠚⢛⣉⣩⡴⠶⠚⠋⠉⠀⠀⠀⠀⠸⡿⡏⠁⠀⢰⠃⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣏⣉⣁⣀⡀⠀⠀⢀⣀⣀⣀⣀⣀⠤⢷⢱⠀⠀⠸⢤⣤⣶⡿⠟⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⣿⣿⣿⣿⠀⢿⣿⣿⣿⣿⡿⠋⢁⣴
    ⡇⠀⢦⣬⣭⣭⣍⣍⣀⣀⣤⣤⣤⠶⠞⢣⡀⠀⠀⠀⠈⢉⠠⣀⣀⣀⡀⠀⠀⠀⠀⢀⣿⣿⡟⣽⣿⣿⣿⣿⡇⢸⣿⣿⡿⠃⠀⣴⣿⣿
    ⣧⠀⢸⣿⣩⣉⣉⣉⣩⠭⢭⣥⣴⣶⣾⣿⣷⡄⠀⠀⡼⠛⠛⠛⠉⠉⠉⠉⠀⠀⠀⣸⡿⢋⣼⠋⣿⣿⣿⣿⣷⠀⣿⣿⠃⠀⢸⣿⣿⡏
    ⣿⠀⢸⣿⣷⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⢢⣤⣶⣶⣶⣶⠎⠀⠀⢸⢏⣴⣿⡏⠀⣿⣿⡏⠀⠘⡄⣿⣿⠀⠀⣿⣿⣿⣿
    ⣿⡄⠘⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣆⠀⠀⠉⠉⠉⠉⠁⠀⠀⢠⣿⣿⠿⣿⠁⠀⣿⣿⣧⠀⠀⣧⢸⣿⠀⠀⣿⣿⣿⣿
    ⣿⡇⠀⡿⠿⠮⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠙⣦⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⢀⡏⠀⠀⢻⣿⣿⡄⠀⣿⣼⣿⡆⠀⢻⣿⣿⣄
    ⣿⣇⠀⢳⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠘⣷⣤⣤⣤⣴⣶⡿⠋⠁⠀⠀⡜⠀⠀⠀⠸⣿⣿⣿⣦⡏⣿⣿⠙⣄⠀⢻⣿⣿
    ⣿⣿⠀⢸⣿⡇⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢿⠙⠿⣿⠿⠋⠀⠀⠀⠀⡜⠀⣠⠀⠀⠀⠟⠛⠻⠿⠿⣿⠇⠀⣾⣦⣀⢹⣿
    ⣿⣿⠀⢸⣿⣇⣼⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠘⡆⠀⢸⣧⡀⠀⠀⠀⠀⠀⠀⡼⠁⠀⡟⠀⢠⣶⣶⣶⣶⣾⣿⣿⠀⠀⣿⣿⣿⣿⣽
    ⠛⠉⠀⠉⠉⣉⣽⣿⣿⣿⠿⢿⣿⣿⡿⠁⠀⢀⣰⠁⠀⢸⠏⢻⣿⠆⠀⠀⡠⠊⠀⠀⢀⠇⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⣠⠟⠉⢉⣿⣿
    ⢀⣤⣶⣾⣿⣿⣿⣿⡿⠁⠀⠀⠈⠛⠷⠤⠤⣀⡀⠀⠀⣸⠀⠀⠁⢀⠴⠊⠀⢀⣀⡤⠞⡄⢀⣿⣿⣿⡫⣵⣿⣿⡿⠋⠀⢀⣴⣿⣿⠟
    ⣿⣿⣿⣿⣿⣋⠵⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣦⠀⠁⢀⡠⠴⠧⠤⠄⠊⠉⠁⢀⡰⠁⠘⣡⡟⣩⣿⣿⣿⣿⠁⠀⣰⣿⡿⠋⠁⠀
'''

class Vampire(Character):

    def __init__(self, name: str, classe: str, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, dice) -> None:
        super().__init__(name, classe, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, dice)
        
    @staticmethod
    def create_default_character(name, template="default") -> Vampire | None:
        if (template=="default"):
            return Vampire(name=name, classe="Vampire", max_health=20, attack_value=5, defense_value=1, attack_type_value=0, attack_special_value=0, touchable=1, dice=Dice(6))
        return None
    
    def attack(self, target: Character):
        print(f"{self.get_name()} lance l'attaque Soif de sang !\n")
        return super().attack(target)
    
    ascii_design = r'''    
                       __,-----,,,,  ,,,--------,__ 
                    _-/|\\/|\\/|\\\|\//\\\//|/|//|\\_ 
                   /|\/\//\\\\\\\\\\//////////////\\\\ 
                 //|//           \\\///            |\\|\ 
                ///|\/             \/               \|\|\ 
               |/|//                                 |\\|\  
              |/|/                                    \|\|\
              ///;    ,,=====,,,  ~~-~~  ,,,=====,,    ;|\|\
             |/|/   '"          `'     '"          "'   ;|\|
             ||/`;   _--~~~~--__         __--~~~~--_   ;/|\|
             /|||;  :  /       \~~-___-~~/       \  :  ;|\| 
             /\|;    -_\  (o)  / ,'; ;', \  (o)  /_-    ;|| 
             |\|;      ~-____--~'  ; ;  '~--____-~      ;\| 
              ||;            ,`   ;   ;   ',            ;|| 
            __|\ ;        ,'`    (  _  )    `',        ;/|__ 
        _,-~###\|/;    ,'`        ~~ ~~        `',    ;|\###~-,_ 
      ,'#########||;  '                           '  ;\|/#######`, 
     .############; ,         _--~~-~~--_           ;#############'.
    ,-' `;-,########;        ,; |_| | |_| ;,       ;;########,-;' `-,
          ;@`,######;       ;_| :%`~'~'%: |_;       ;######,'@;
           ;@@`,#####;     :%%`\/%%%%%%%\/'%%:     ;#####,'@@;
            ;@@@`,####;     :%%%%%%%%%%%%%%%;     ;####,'@@@;
             ;@@@@`,###;     ;./\_%%%%%_/\.;     ;####,@@@@;
          _-'@@@@@@@@;-~;     ~~--|~|~|--~~     ;~--;@@@@@@@'-_
      _,-'@@@@@@@@@@@@;  ;        ~~~~~        ;   ;@@@@@@@@@@@`-,_
    ,~@@@@@@@@@@@@@@@@@;  \`~--__         __--~/  ;@@@@@@@@@@@@@@@@~,
    @@@@@@@@@@@@@@@@@@@@;   \   ~~-----~~    /   ;@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@~-_  \  /  |  \   /  _-~@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@~~-\/   |   \/ -~~@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@(=)=;==========;=(=)@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@;    |     ;@@@@@@@@@@@@@@@@@@@@@@@@@@
'''    

    
    
class Hydre(Character):

    def __init__(self, name: str, classe: str, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, dice) -> None:
        super().__init__(name, classe, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, dice)
        
    @staticmethod
    def create_default_character(name, template="default") -> Hydre | None:
        if (template=="default"):
            return Hydre(name=name, classe="Hydre", max_health=30, attack_value=8, defense_value=3, attack_type_value=0, attack_special_value=0, touchable=0, dice=Dice(6))
        return None
    
    def attack(self, target: Character):
        print(f"{self.get_name()} lance l'attaque Souffle hydrique !\n")
        return super().attack(target)
    
    ascii_design = r'''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠀⢸⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣠⣦⣤⣀⣀⣤⣤⣀⡀⠀⣀⣠⡆⠀⠀⠀⠀⠀⠀⠤⠒⠛⣛⣛⣻⣿⣶⣾⣿⣦⣄⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠸⠿⢿⣿⣿⣿⣯⣭⣿⣿⣿⣿⣋⣀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣓⠢⠄⢠⡾⢻⣿⣿⣿⣿⡟⠁⠀⠀⠈⠙⢿⣿⣿⣯⡻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠙⢿⣿⣿⣿⣷⣄⠁⠀⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣷⣌⢧⠀⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⢀⠉⠙⠛⠛⠿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡀⠠⢻⡟⢿⣿⣿⣿⣿⣧⣄⣀⠀⠘⢶⣄⣀⠀⠀⠈⢻⠿⠁⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣾⠀⠀⠀⠻⣈⣙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠈⠲⣄⠀⠀⣀⡤⠤⠀⠀⠀⢠⣿⣿⣿⡿⣿⠇⠀⠀⠐⠺⢉⣡⣴⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣶⣿⣿⣿⣶⣶⡀⠀⠀⠀
    ⠀⠀⠀⠀⢠⣿⣴⣿⣷⣶⣦⣤⡀⠀⢸⣿⣿⣿⠇⠏⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⠟⢿⣿⣿⣿⣷⠀⠹⣿⣿⠿⠿⠛⠻⠿⣿⠇⠀⠀⠀
    ⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣷⣯⡂⢸⣿⣿⣿⠀⠀⠀⠀⢀⠾⣻⣿⣿⣿⠟⠀⠀⠈⣿⣿⣿⣿⡇⠀⠀⣀⣀⡀⠀⢠⡞⠉⠀⠀⠀⠀
    ⠀⠀⢸⣟⣽⣿⣯⠀⠀⢹⣿⣿⣿⡟⠼⣿⣿⣿⣇⠀⠀⠀⠠⢰⣿⣿⣿⣿⡄⠀⠀⠀⣸⣿⣿⣿⡇⠀⢀⣤⣼⣿⣷⣾⣷⡀⠀⠀⠀⠀
    ⠀⢀⣾⣿⡿⠟⠋⠀⠀⢸⣿⣿⣿⣿⡀⢿⣿⣿⣿⣦⠀⠀⠀⢺⣿⣿⣿⣿⣿⣄⠀⠀⣿⣿⣿⣿⡇⠐⣿⣿⣿⣿⠿⣿⣿⡿⣦⠀⠀⠀
    ⠀⢻⣿⠏⠀⠀⠀⠀⢠⣿⣿⣿⡟⡿⠀⠀⢻⣿⣿⣿⣷⣤⡀⠘⣷⠻⣿⣿⣿⣿⣷⣼⣿⣿⣿⣿⣇⣾⣿⣿⣿⠁⠀⢼⣿⣿⣿⣆⠀⠀
    ⠀⠀⠈⠀⠀⠀⠀⠀⢸⣿⣿⣿⡗⠁⠀⠀⠀⠙⢿⣿⣿⣿⣿⣷⣾⣆⡙⣿⣿⣿⣿⣿⣿⣿⣿⣿⠌⣾⣿⣿⣿⣆⠀⠀⠀⠉⠻⣿⡷⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠘⣟⣿⣿⣿⡆⠀⠀⠀⠀⠙⠁⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣶⣤⣤⣤⣀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⢈⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣠⣤⣤⣶⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⣠⣤⣄⠀⠠⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢀⣀⠀⣠⣀⡠⠞⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⣷⣦⣄⣀⢿⡽⢻⣦
    ⠻⠶⠾⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠋
'''

class Basilisc(Character):

    def __init__(self, name: str, classe: str, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, dice) -> None:
        super().__init__(name, classe, max_health, attack_value, defense_value, attack_type_value, attack_special_value, touchable, dice)
        
    @staticmethod
    def create_default_character(name, template="default") -> Basilisc | None:
        if (template=="default"):
            return Basilisc(name=name, classe="Basilisc", max_health=25, attack_value=6, defense_value=3, attack_type_value=0, attack_special_value=0, touchable=0, dice=Dice(6))
        return None
    
    def attack(self, target: Character):
        print(f"{self.get_name()} lance l'attaque Venin !\n")
        return super().attack(target)
    
    ascii_design = r'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⣲⢾⣭⠽⠏⠉⠑⠒⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⡟⠁⠀⣼⡧⠊⠁⣠⠔⠒⠒⠒⠢⡝⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢾⡕⢹⠇⠀⠐⠋⠀⢠⣾⠵⠒⠋⠉⠉⠉⠻⣌⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢞⣱⠈⢧⣸⡄⠀⠀⠀⠀⠉⠀⠀⣀⣤⠤⣄⡀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠟⣿⡀⠀⠉⠓⠀⣀⣤⣬⡆⢰⣯⣥⣤⣤⣤⣙⣦⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠫⢧⣄⠘⣿⡄⠀⢴⡺⠗⠊⣹⠟⠀⠀⠀⠀⠀⠀⠀⠉⠁⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣻⣇⠀⠈⠉⠉⠉⡴⠋⠑⢦⡴⣣⠶⠒⠉⠉⠑⠲⢤⡀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠏⡇⠈⢧⡀⠀⢀⡾⣄⣀⡴⠋⠚⠉⠉⠓⠶⠒⠒⠉⠙⠃⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠓⠒⠒⠛⠁⡞⢀⡤⠾⣦⣤⠤⠤⢤⡤⠤⠤⣄⣴⠶⣤⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠳⣄⡀⠀⢸⠁⢸⣱⡀⡠⠙⡧⠤⠄⠀⠤⣴⠳⣄⢀⣎⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⢻⣀⠤⠝⠁⢸⣴⠛⢻⡏⢷⡤⠙⢦⠀⠀⣤⠊⢤⡾⢻⣟⢛⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢠⣤⡀⠀⠀⢸⣿⣠⠚⣻⣻⣷⡶⠾⣀⢀⠿⣶⣼⣟⣿⡛⣄⡟⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣮⣇⣉⠟⠂⢸⣽⡷⡄⠀⣈⡻⠿⠚⠍⠩⠇⠽⢿⣁⠀⢡⢼⣥⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣌⠁⠀⠀⠀⠉⢻⣷⠤⣀⣀⣀⣀⣰⣦⣂⣀⣀⣀⡤⣾⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⢲⠒⠚⢛⡟⠀⢹⣷⢶⠓⣿⣷⣾⣷⣿⣿⡒⣿⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣳⡤⠋⠀⠀⠀⢻⡼⣆⣿⣿⣯⣭⣿⣿⣷⢧⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡤⡶⠖⠒⣲⠎⣿⣸⣿⣿⡧⣿⣿⣿⡃⣿⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣞⠢⡔⠁⠀⣸⣯⠙⠙⢳⡘⣏⡟⣽⠇⠀⠈⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣝⠫⣭⡿⣍⠉⠉⢙⣇⡟⣩⡥⠄⠀⢀⣤⠌⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣌⠀⠙⠯⣲⣎⣸⣻⡏⢀⡠⠞⠉⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢤⡀⠈⡆⢀⠇⠹⡍⠀⠀⠀⠀⢀⡰⠆⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣋⠹⡶⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡉⠉⠀⠀⠘⢦⣀⣠⠞⠁⠀⠀⠀⠀⠀⠘⢧⡀⠀⠀⠀⠀⠀⠀
⠀⣿⣄⡝⠆⣨⠟⢳⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣜⣿⣛⡟⠻⣄⠀⠀⠀⠀⠀⣠⠄⠀⠀⠙⣄⠀⠀⠀⠀⠀
⠀⠈⠹⣷⣼⠉⠣⣔⠉⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢭⡁⠀⠈⢳⡀⣠⠴⠋⠀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠀
⠀⠀⠀⠈⠻⣤⡏⠀⡱⣄⢠⠟⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢟⠿⠟⠙⢦⠀⠀⠀⠀⠀⢀⣠⠄⠀⢻⡄⠀⠀
⠀⠀⠀⠀⠀⠘⢿⣾⡁⣨⠓⢄⡘⠋⣙⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡴⣖⡶⠳⣄⣀⡤⠞⠋⠀⠀⠀⠀⢻⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠿⣧⣀⡆⣽⠋⠉⠉⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢯⣀⣀⣙⣧⡀⠀⠀⠀⠀⠀⠀⠀⢳⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢷⣯⡀⢀⣤⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡳⠟⠉⢳⡀⢀⣀⠠⠀⠀⠀⠈⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠙⢣⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣤⣄⣀⡻⡍⠁⠀⠀⠀⠀⠀⢷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣷⠶⠭⠇⠀⢸⣤⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⠷⠛⠁⢹⡄⠀⠀⠀⠀⠀⢸
⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⢶⣞⣋⢩⡇⠀⡠⢴⠀⠘⡆⠹⡒⢦⡍⠉⢩⣭⣿⣒⠒⠦⣤⣤⣄⡀⠀⠀⢸⠀⠀⠀⠀⢻⡤⠒⠂⠀⠀⢸
⠀⠀⠀⠀⣠⡶⢛⣽⣤⣤⠈⠱⣽⢸⠀⠚⠒⠺⠀⠀⢧⠀⠑⠋⠀⠀⠀⢹⣄⠔⠋⠀⠐⡖⠚⢯⡝⢲⡟⡾⡆⠀⠀⠀⢷⠀⠀⠀⠀⢸
⠀⢀⣴⠟⠁⠞⠛⠉⠓⢾⠀⠀⠀⠸⡄⠀⢀⣴⡛⢆⠘⢷⡀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠷⠒⠋⢀⡾⠿⣄⣈⢢⣄⠀⢸⠀⠤⠖⠀⢸
⢠⡟⠁⠀⠀⠀⣀⣀⣀⣦⠀⠀⠀⠀⣷⡀⠈⠁⠈⢹⣄⠀⠙⢶⡶⠶⠤⢤⣀⣀⠀⠀⠀⠀⣠⠖⣋⣤⠀⠀⠈⠉⠁⠀⠘⡇⠀⠀⠀⡏
⣿⠀⠀⠀⠀⡼⢃⡠⠾⠛⢲⣮⣍⣁⣬⣷⣄⡀⠤⠾⠭⠷⠄⠀⠙⠳⢦⣄⣀⡠⠽⢿⠚⠉⢰⡏⠁⠻⡀⠀⠀⠀⠀⠀⢠⠇⠀⠀⢸⠃
⢿⠀⠀⠀⠀⡟⠋⠀⠀⡴⠋⢉⡿⠀⠀⢠⠾⠿⣿⡍⠉⠉⡯⠭⠽⣽⠉⠀⡴⠖⠚⠙⡇⠀⠀⠳⣄⠀⠻⣄⠀⠀⠀⠀⡼⠒⠒⣰⠏⠀
⠘⢧⠀⠀⠀⠀⠀⠀⠀⡇⢀⠞⠀⠀⠀⡞⠀⣰⠏⠀⠀⢸⡅⠀⣰⠏⠀⠀⢹⡀⠀⠀⡇⠀⠀⠀⠀⠙⠓⠾⠆⠀⠀⣼⠃⢀⣼⠃⠀⠀
⠀⠈⠳⡀⠀⠀⠀⠀⠀⢷⡟⠀⠀⠀⠀⣇⣰⠏⠀⠀⠀⠀⡇⠀⡇⠀⠀⠀⠀⠳⡀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠓⣤⠟⠁⠀⠀⠀
⠀⠀⠀⠈⠲⣄⡀⠀⠀⠈⠀⠀⠀⠀⠀⠘⠛⠀⠀⠀⠀⠀⠹⣾⠀⠀⠀⠀⠀⠀⠙⢾⠀⠀⠀⠀⠀⠀⠀⣀⠔⣫⡴⠞⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠓⠦⢄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡾⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠒⠒⠶⠤⠤⠤⠤⣤⣤⣤⣤⣤⣤⣤⠤⠤⠤⠤⠴⠶⠒⠒⠛⢉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''
