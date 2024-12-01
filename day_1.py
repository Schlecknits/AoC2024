f = open("input_1.txt", "r")  # input as .txt file   


def sort_list(list_to_sort):
    sorted_list = []
    while list_to_sort:
        current_lowest = list_to_sort[0]
        index_lowest = 0
        for i, entry in enumerate(list_to_sort):
            if entry < current_lowest:
                current_lowest = entry
                index_lowest = i

        sorted_list.append(list_to_sort[index_lowest])
        list_to_sort.pop(index_lowest)

    return sorted_list


def puzzle_1(sorted_left, sorted_right):
    total_distance = 0
    for i, entry in enumerate(sorted_left):
        current_distance = abs(entry - sorted_right[i])
        total_distance += current_distance
    return str(total_distance)


def puzzle_2(left_column, right_column):
    total_similarity = 0
    for left_entry in left_column:
        current_similarity = 0
        for right_entry in right_column:
            if left_entry == right_entry:
                current_similarity += int(left_entry)
        total_similarity += current_similarity
    return str(total_similarity)


# column reader

left_side = []
right_side = []
while True:
    if line := f.readline().split():
        left, right = map(int, line)
        left_side.append(left)
        right_side.append(right)
    else:
        break

distance = puzzle_1(sort_list(left_side.copy()), sort_list(right_side.copy()))
print("Total distance is: " + distance)
similarity = puzzle_2(left_side.copy(), right_side.copy())
print("Total similarity is: " + similarity)
