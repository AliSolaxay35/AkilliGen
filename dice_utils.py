import random
import pickle
import os

def generate_and_save_dice_rolls(filename="dice_rolls.pkl", count=10_000):
    if os.path.exists(filename):
        print(f"File '{filename}' already exists. Skipping generation.")
        return

    data_list = [(random.randint(1,6), random.randint(1,6)) for _ in range(count)]
    with open(filename, "wb") as output_file:
        pickle.dump(data_list, output_file)
    print(f"Generated and saved {count} dice rolls to '{filename}'.")

def load_dice_rolls(filename="dice_rolls.pkl"):
    with open(filename, "rb") as data_file:
        data = pickle.load(data_file)
        for roll in data:
            yield roll
