import random
import pickle
import os

# Dice generator
def dice():
    while True:
        yield random.randint(1, 6)

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

# Game class
class Game:
    def __init__(self, players):
        self.players = players
        self.turn = 0
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

    def move_player(self, player, steps):
        old_position = player.position
        player.position += steps
        if player.position > 100:
            player.position = old_position  # Cannot move beyond 100
        elif player.position in self.snakes:
            print(f"Oh no! {player.name} hit a snake!")
            player.position = self.snakes[player.position]
        elif player.position in self.ladders:
            print(f"Great! {player.name} climbed a ladder!")
            player.position = self.ladders[player.position]

    def save(self, filename="game.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(filename="game.pkl"):
        with open(filename, "rb") as f:
            return pickle.load(f)

# Game loop
def main():
    filename = "game.pkl"
    
    if os.path.exists(filename):
        game = Game.load(filename)
        print("Previous game loaded.")
    else:
        names = input("Enter player names (comma-separated): ").split(",")
        players = [Player(name.strip()) for name in names]
        game = Game(players)

    dice_gen = dice()

    while True:
        player = game.players[game.turn % len(game.players)]
        input(f"\n{player.name}'s turn. Press Enter to roll the dice...")
        step = next(dice_gen)
        print(f"{player.name} rolled a {step}")
        game.move_player(player, step)
        print(f"{player.name} is now on square {player.position}.")

        if player.position == 100:
            print(f"\nCongratulations! {player.name} wins the game!")
            if os.path.exists(filename):
                os.remove(filename)  # Remove saved game after winning
            break

        game.turn += 1
        game.save(filename)

if __name__ == "__main__":
    main()

