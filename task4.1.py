import regex as re

from const import INPUT_FOLDER

INPUT_FILE = INPUT_FOLDER/"input4.1"

result = 0
with open(INPUT_FILE, "r") as infile:
    for line in infile:
        card_points = 0
        line = re.sub(r"\s+", " ", line.strip())
        winning, received = line.split(": ")[-1].strip().split(" | ")
        winning = list(map(int, winning.split()))
        received = list(map(int, received.split()))

        for i, num in enumerate(winning):
            if num in received:
                card_points = 1
                break
        winning = winning[i + 1:]
        for num in received:
            if num in winning:
                card_points *= 2
        result += card_points

print("HO! HO! HO! The right answer is", result)
