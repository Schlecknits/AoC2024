def input_reader(input_name):
    file = open(input_name, "r")
    xy = []
    updates = []
    switch_mode = False
    for line in file:
        if line == "\n":
            switch_mode = True
        elif switch_mode:
            updates.append([int(num) for num in line.strip().split(",")])
        else:
            xy_append = tuple([int(num) for num in line.strip().split("|")])
            xy.append(xy_append)

    file.close()

    return xy, updates


def find_pages_and_following(rules):
    page_dict = dict()
    for pages in rules:
        if not pages[0] in page_dict:
            pages_after = set()
            for inner_pages in rules:
                if pages[0] == inner_pages[0]:
                    pages_after.add(inner_pages[1])
            page_dict[pages[0]] = pages_after
    return page_dict


def check_for_correct_update(update, pages_following):
    end = len(update)

    for i in range(end):
        update_value = update[i]
        if update_value in pages_following:
            for j in range(i):
                if update[j] in pages_following[update_value]:
                    return False
    return True


def sort_values(update, pages_following):
    sorted_list = []
    while update:
        current_first = update[0]
        cur_first_pos = 0
        for i, entry in enumerate(update):
            if current_first in pages_following[entry]:
                current_first = entry
                cur_first_pos = i

        sorted_list.append(update[cur_first_pos])
        update.pop(cur_first_pos)

    return sorted_list


def puzzle_1(rules, updates):
    sum_of_correct_middle_values = 0
    pages_following = find_pages_and_following(rules)
    for update in updates:
        if check_for_correct_update(update, pages_following):
            sum_of_correct_middle_values += update[int(len(update) / 2)]
    return sum_of_correct_middle_values


def puzzle_2(rules, updates):
    sum_of_corrected_middle_values = 0
    pages_following = find_pages_and_following(rules)
    for update in updates:
        if not check_for_correct_update(update, pages_following):
            sum_of_corrected_middle_values += sort_values(update.copy(), pages_following)[int(len(update) / 2)]
    return sum_of_corrected_middle_values


page_rules, all_updates = input_reader("input_5.txt")
print("Puzzle 1: Sum of correct update middle values:", puzzle_1(page_rules, all_updates))
print("Puzzle 2: Sum of correct update middle values:", puzzle_2(page_rules, all_updates))
