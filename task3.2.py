from const import INPUT_FOLDER

INPUT_FILE = INPUT_FOLDER/"input3.1"

with open(INPUT_FILE, "r") as infile:
    _map = [
        f".{line.strip()}."
        for line
        in infile
    ]

_map = ["." * len(_map[0])] + _map + ["." * len(_map[0])]
map_width = len(_map[0])


def get_number(row: str, pos: int) -> int:
    """
    Restore the number from an arbitrary digit in a map row
    :param row: a string from the map
    :param pos: position of the given digit
    :return: restored number
    """
    num = ""
    slider = pos
    while row[slider].isdigit():
        num = row[slider] + num
        slider -= 1
    slider = pos + 1
    while row[slider].isdigit():
        num += row[slider]
        slider += 1
    return int(num)


result = 0
for i in range(1, len(_map) - 1):
    for j in range(1, map_width - 1):
        if _map[i][j] == "*":
            nums = []
            # Up
            if _map[i - 1][j].isdigit():
                nums.append(get_number(_map[i - 1], j))
            elif _map[i - 1][j - 1].isdigit() or _map[i - 1][j + 1].isdigit():
                if _map[i - 1][j - 1].isdigit():
                    nums.append(get_number(_map[i - 1], j - 1))
                if _map[i - 1][j + 1].isdigit():
                    nums.append(get_number(_map[i - 1], j + 1))
            # Down
            if _map[i + 1][j].isdigit():
                nums.append(get_number(_map[i + 1], j))
            elif _map[i + 1][j - 1].isdigit() or _map[i + 1][j + 1].isdigit():
                if _map[i + 1][j - 1].isdigit():
                    nums.append(get_number(_map[i + 1], j - 1))
                if _map[i + 1][j + 1].isdigit():
                    nums.append(get_number(_map[i + 1], j + 1))
            # Left
            if _map[i][j - 1].isdigit():
                nums.append(get_number(_map[i], j - 1))
            # Right
            if _map[i][j + 1].isdigit():
                nums.append(get_number(_map[i], j + 1))
            if len(nums) == 2:
                result += nums[0] * nums[1]

print("HO! HO! HO! The right answer is", result)
