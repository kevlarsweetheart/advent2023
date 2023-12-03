import re
from const import INPUT_FOLDER

INPUT_FILE = INPUT_FOLDER/"input1.1"

with open(INPUT_FILE, "r") as infile:
    result = 0
    for line in infile:
        line = re.sub(r"\D", "", line.strip())
        if line:
            result += int(f"{line[0]}{line[-1]}")

print("HO! HO! HO! The right answer is", result)
