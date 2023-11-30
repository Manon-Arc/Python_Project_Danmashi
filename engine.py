from classes.game import Game
from classes.warrior import Warrior

def main():
    game = Game()
    game.start_game()

def test():
    char=Warrior.create_default_character("toto")
    print((char._max_health * 0.4))
 
if __name__ == "__main__":
    main()
    # test()