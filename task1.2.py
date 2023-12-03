import regex as re
from const import INPUT_FOLDER

INPUT_FILE = INPUT_FOLDER/"input1.1"

STR2DIGIT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

pattern = re.compile(r"(\d{1}|one|two|three|four|five|six|seven|eight|nine)")

with open(INPUT_FILE, "r") as infile:
    result = 0
    for line in infile:
        digits = pattern.findall(line.strip(), overlapped=True)
        if digits:
            first = STR2DIGIT.get(digits[0]) if STR2DIGIT.get(digits[0]) is not None else digits[0]
            last = STR2DIGIT.get(digits[-1]) if STR2DIGIT.get(digits[-1]) is not None else digits[-1]
            result += int(f"{first}{last}")

print("HO! HO! HO! The right answer is", result)
