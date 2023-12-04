from const import INPUT_FOLDER

INPUT_FILE = INPUT_FOLDER/"input2.1"

ALLOWED_NUMBER = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def game_is_valid(set_info: str) -> bool:
    sets = set_info.split("; ")
    for _set in sets:
        cubes = _set.split(", ")
        for cube in cubes:
            num, color = cube.split()
            if int(num) > ALLOWED_NUMBER[color]:
                return False
    return True


with open(INPUT_FILE, "r") as infile:
    result = 0
    for line in infile:
        game_id, set_info = line.strip().split(": ")
        game_id = int(game_id.split()[-1])

        if game_is_valid(set_info):
            result += game_id

print("HO! HO! HO! The right answer is", result)
