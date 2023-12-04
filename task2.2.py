from collections import defaultdict
from const import INPUT_FOLDER

INPUT_FILE = INPUT_FOLDER/"input2.1"


def get_set_power(set_info: str) -> int:
    num_by_color = defaultdict(int)
    sets = set_info.split("; ")
    for _set in sets:
        cubes = _set.split(", ")
        for cube in cubes:
            num, color = cube.split()
            num_by_color[color] = max(int(num), num_by_color[color])
    power = 1
    for num in num_by_color.values():
        power *= num
    return power


with open(INPUT_FILE, "r") as infile:
    result = 0
    for line in infile:
        _, set_info = line.strip().split(": ")
        result += get_set_power(set_info)

print("HO! HO! HO! The right answer is", result)
