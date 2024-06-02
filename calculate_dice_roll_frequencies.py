import random


def simulate_dice_roll():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2


def calculate_dice_roll_frequencies(num_rolls=1000):
    roll_counts = {total: 0 for total in range(2, 13)}

    for _ in range(num_rolls):
        roll_total = simulate_dice_roll()
        roll_counts[roll_total] += 1

    print("Dice Roll Frequencies:")
    for roll_total in sorted(roll_counts):
        frequency_percentage = (roll_counts[roll_total] / num_rolls) * 100
        print(f"{roll_total}: {frequency_percentage:.2f}%")
    print()


calculate_dice_roll_frequencies()
