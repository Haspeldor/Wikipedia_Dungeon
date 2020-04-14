import wikipedia
from level import Level
from game import Game



def main():
    level = Level()
    game = Game(level)
    game.start_game()


if __name__ == "__main__":
    main()