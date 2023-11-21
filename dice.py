import random

class Dice:
    
    def __init__(self, nbr_face = 6):
        self._faces = nbr_face
        self._value = 1
        
    def roll(self):
        return random.randint(1, self._faces)
    
    def set_value(self):
        self._value = self.roll()
        
    def __str__(self) -> str:
        return(f"I'm a dice of {self._faces} faces et my value is : {self._value} ")
    
class RiggedDice(Dice):
    
    def roll(self, rigged = False):
        return self._faces if rigged else super().roll()
    
if __name__ == "__main__":     
    dice = Dice()
    dice.set_value()
    print(dice.__str__())

    a_rigged_dice = RiggedDice()
    print(a_rigged_dice.roll(True))
else :
    pass