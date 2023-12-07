import regex as re
from const import INPUT_FOLDER

INPUT_FILE = INPUT_FOLDER/"input3.1"

num_pattern = re.compile(r"\d+")
symbol_pattern = re.compile(r"[^\.]+")

with open(INPUT_FILE, "r") as infile:
    _map = [
        f".{line.strip()}."
        for line
        in infile
    ]

_map = ["." * len(_map[0])] + _map + ["." * len(_map[0])]

result = 0
for i in range(1, len(_map) - 1):
    num = num_pattern.search(_map[i])
    while num is not None:
        left, right = num.start() - 1, num.end()
        if _map[i][right] != "." or _map[i][left] != ".":
            result += int(_map[i][left + 1:right])
        elif symbol_pattern.search(_map[i - 1][left:right + 1]) or symbol_pattern.search(_map[i + 1][left:right + 1]):
            result += int(_map[i][left + 1:right])
        _map[i] = _map[i][:left + 1] + "#" * (right - left - 1) + _map[i][right:]
        num = num_pattern.search(_map[i])

print("HO! HO! HO! The right answer is", result)
