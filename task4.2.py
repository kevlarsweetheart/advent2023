import regex as re
from collections import defaultdict

from const import INPUT_FOLDER

INPUT_FILE = INPUT_FOLDER/"input4.1"

card_cnt = defaultdict(int)
with open(INPUT_FILE, "r") as infile:
    for line in infile:
        line = re.sub(r"\s+", " ", line.strip())
        curr_card = int(line.split(": ")[0].split()[-1])
        card_cnt[curr_card] += 1
        winning, received = line.split(": ")[-1].strip().split(" | ")
        winning = set(map(int, winning.split()))
        received = set(map(int, received.split()))
        steps = len(winning & received)
        if steps > 0:
            for i in range(curr_card + 1, curr_card + steps + 1):
                card_cnt[i] += card_cnt[curr_card]

result = sum(list(card_cnt.values()))
print("HO! HO! HO! The right answer is", result)
