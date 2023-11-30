from random import randint

class Dice:
    
    def __init__(self, nbr_face = 6):
        self._faces = nbr_face
        self._value = 1
        
    def roll(self):
        return randint(1, self._faces)
    
    def set_value(self):
        self._value = self.roll()
        
    def __str__(self) -> str:
        return(f"I'm a dice of {self._faces} faces et my value is : {self._value} ")
