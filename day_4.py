import dataclasses


@dataclasses.dataclass()
class Vec2:
    x: int
    y: int

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) == int:
            return Vec2(self.x * other, self.y * other)
        else:
            return Vec2(self.x * other.x, self.y * other.y)

    #  The following implementations might not be correct for generic Vectors but are useful in this particular use-case
    def __gt__(self, other):
        if self.x > other.x or self.y > other.y:
            return True
        return False

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __lt__(self, other):
        if self.x < other.x or self.y < other.y:
            return True
        return False


DIRECTIONS = [
    Vec2(0, 1),  # up
    Vec2(1, 1),  # up-right
    Vec2(1, 0),  # right
    Vec2(1, -1),  # down-right
    Vec2(0, -1),  # down
    Vec2(-1, -1),  # down-left
    Vec2(-1, 0),  # left
    Vec2(-1, 1)  # up-left
]


def input_reader(input_name):
    file = open(input_name, "r")
    lines = []
    for line in file:
        lines += line.strip().split()
    file.close()
    return lines


def find_starts(input_lines, starting_character):
    x_pos = []
    for y, line in enumerate(input_lines):
        for x, character in enumerate(line):
            if character == starting_character:
                x_pos.append(Vec2(x, y))
    return x_pos


def within_bounds(vec_to_check, bounding_vecs):
    if vec_to_check < bounding_vecs[0] or vec_to_check > bounding_vecs[1]:
        return False
    return True


def puzzle_1(input_lines, bounding_vecs):
    starting_pos = find_starts(input_lines, "X")
    count_of_xmas = 0
    for pos in starting_pos:
        for direction in DIRECTIONS:
            destination = pos + direction * 3
            current_pos = pos
            if not within_bounds(destination, bounding_vecs):
                continue
            else:
                xmas = ""
                xmas += input_lines[pos.y][pos.x]
                while current_pos != destination:
                    current_pos += direction
                    xmas += input_lines[current_pos.y][current_pos.x]
                if xmas == "XMAS":
                    count_of_xmas += 1
    return str(count_of_xmas)


def puzzle_2(input_lines, bounding_vecs):
    directions_to_check = [
        Vec2(1, 1),  # up-right
        Vec2(1, -1)  # down-right
    ]

    starting_pos = find_starts(input_lines, "A")
    count_of_mas_x = 0
    for pos in starting_pos:
        mas_x = ["A", "A"]
        for i, direction in enumerate(directions_to_check):
            pos_to_check = pos + direction
            if not within_bounds(pos_to_check, bounding_vecs):
                break
            mas_x[i] += input_lines[pos_to_check.y][pos_to_check.x]
            pos_to_check = pos - direction
            if not within_bounds(pos_to_check, bounding_vecs):
                break
            mas_x[i] = input_lines[pos_to_check.y][pos_to_check.x] + mas_x[i]
        if (mas_x[0] == "MAS" or mas_x[0] == "SAM") and (mas_x[1] == "MAS" or mas_x[1] == "SAM"):
            count_of_mas_x += 1
    return str(count_of_mas_x)


read_lines = input_reader("input_4.txt")
bounding = [Vec2(0, 0),
            Vec2(len(read_lines[0]) - 1, len(read_lines) - 1)]
print("The word 'XMAS' was found ", puzzle_1(read_lines, bounding), " times.")
print("The X of 'MAS' was found ", puzzle_2(read_lines, bounding), " times.")
