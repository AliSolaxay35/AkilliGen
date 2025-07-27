from dice_utils import generate_and_save_dice_rolls, load_dice_rolls

def main():
    generate_and_save_dice_rolls()

    count = 0
    for dice in load_dice_rolls():
        print(dice)
        count += 1
        if count == 5:
            break

if __name__ == "__main__":
    main()


