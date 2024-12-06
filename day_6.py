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
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        if self.x < other.x or self.y < other.y:
            return True
        return False

    def __hash__(self):
        return hash((self.x, self.y))


DIRECTIONS = [
    Vec2(0, -1),  # up
    Vec2(1, 0),  # right
    Vec2(0, 1),  # down
    Vec2(-1, 0),  # left
]


def input_reader(input_name):
    file = open(input_name, "r")
    lines = []
    for line in file:
        lines.append(line.strip())
    file.close()
    return lines


def within_bounds(vec_to_check, bounding):
    if vec_to_check < bounding_vecs[0] or vec_to_check > bounding_vecs[1]:
        return False
    return True


def find_starting_position(tiles):
    for y, tile_line in enumerate(tiles):
        for x, tile in enumerate(tile_line):
            if tile == "^":
                return Vec2(x, y)


def rotate_90_clockwise(current_direction):
    direction_index = DIRECTIONS.index(current_direction) + 1
    if direction_index >= len(DIRECTIONS):
        direction_index = 0
    return DIRECTIONS[direction_index]


def move(current_pos, current_direction, tiles, bounding):
    next_pos = current_pos + current_direction
    tiles[current_pos.y] = tiles[current_pos.y][:current_pos.x] + "X" + tiles[current_pos.y][current_pos.x + 1:]
    if within_bounds(next_pos, bounding):
        if tiles[next_pos.y][next_pos.x] == "#":
            current_direction = rotate_90_clockwise(current_direction)
        else:
            current_pos = next_pos
    else:
        return False, current_direction
    return current_pos, current_direction


def possible_rectangle_finder(changes_in_direction):
    obstructions = []
    for i in range(len(changes_in_direction) - 4):
        if changes_in_direction[i].x == changes_in_direction[i + 1].x and changes_in_direction[i + 1].y == \
                changes_in_direction[i + 2].y:
            obstructions.append(Vec2(changes_in_direction[i + 2].x, changes_in_direction[i].y))
        if changes_in_direction[i].y == changes_in_direction[i + 1].y and changes_in_direction[i + 1].x == \
                changes_in_direction[i + 2].x:
            obstructions.append(Vec2(changes_in_direction[i].x, changes_in_direction[i + 2].y))
    print(obstructions)
    print(len(obstructions))


def test_for_loop_possibility(current_pos, direction, tiles, bounding):
    starting_pos = current_pos

    checked_obstacle = current_pos + direction

    direction = rotate_90_clockwise(direction)
    starting_direction = direction
    checked = []
    while True:

        current_pos, direction = move(current_pos, direction, tiles, bounding)
        print(current_pos, direction)
        if not current_pos:
            return False
        if current_pos in checked:
            print("Ich war hier schon. Meine Start Pos war", starting_pos, starting_direction)
            print(current_pos, direction)
        elif current_pos == starting_pos:
            print("found valid obstacle")
            return checked_obstacle


def puzzle_1(tiles, bounding):
    current_pos = find_starting_position(tiles)
    current_direction = DIRECTIONS[0]
    count_tiles_entered = 0
    while True:
        current_pos, current_direction = move(current_pos, current_direction, tiles, bounding)
        if not current_pos:
            for line in tiles:
                for tile in line:
                    if tile == "X":
                        count_tiles_entered += 1
            return count_tiles_entered


def puzzle_2(tiles, bounding):
    starting_pos = find_starting_position(tiles)
    current_pos = starting_pos
    starting_direction = DIRECTIONS[0]
    current_direction = starting_direction
    possible_obstacles = set()
    entered_tiles_direction = set()
    while current_pos:
        entered_tiles_direction.add((current_pos, current_direction))
        current_pos, current_direction = move(current_pos, current_direction, tiles, bounding)

    for i, tile in enumerate(entered_tiles_direction):
        current_pos = starting_pos
        current_direction = starting_direction
        tile_direction = (starting_pos, starting_direction)
        current_entered_tiles_direction = set()
        temp_tiles = tiles.copy()
        temp_tiles[tile[0].y] = temp_tiles[tile[0].y][:tile[0].x] + "#" + temp_tiles[tile[0].y][tile[0].x + 1:]
        obstacle = Vec2(tile[0].x, tile[0].y)
        while True:
            if not current_pos:
                break
            if tile_direction in current_entered_tiles_direction:
                possible_obstacles.add(obstacle)
                break
            current_entered_tiles_direction.add(tile_direction)
            current_pos, current_direction = move(current_pos, current_direction, temp_tiles, bounding)
            tile_direction = (current_pos, current_direction)

    print(len(possible_obstacles))



read_tiles = input_reader("input_6.txt")  # individual tiles can be accessed by `tiles[y][x]`
bounding_vecs = [Vec2(0, 0),
                 Vec2(len(read_tiles[0]) - 1, len(read_tiles) - 1)]
print("Puzzle 1: The guard visited", puzzle_1(read_tiles.copy(), bounding_vecs), "distinct positions before leaving "
                                                                                 "the map.")
puzzle_2(read_tiles.copy(), bounding_vecs)
