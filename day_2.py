def check_increasing_decreasing(report):
    is_increasing = True
    is_decreasing = True
    prev_number = None
    for number in report:
        if prev_number:
            if prev_number < number:
                is_decreasing = False
            elif prev_number > number:
                is_increasing = False
            else:
                return False  # returns False as identical numbers can never be increasing or decreasing
        prev_number = number
    if is_increasing or is_decreasing:
        return True
    else:
        return False


def check_adjacent_levels(report):
    prev_number = None
    for number in report:
        if prev_number:
            difference = abs(prev_number - number)
            if difference < 1 or difference > 3:
                return False
        prev_number = number
    return True


def input_reader(file):
    for line in file:
        yield [int(num) for num in line.strip().split()]

    file.close()


def puzzle_1():
    f = open("input_2.txt", "r")  # input as .txt file
    count_of_safe_reports = 0
    for current_report in input_reader(f):
        if check_increasing_decreasing(current_report) and check_adjacent_levels(current_report):
            count_of_safe_reports += 1
    return str(count_of_safe_reports)


def puzzle_2():
    f = open("input_2.txt", "r")
    count_of_safe_reports = 0
    for current_report in input_reader(f):
        if check_increasing_decreasing(current_report) and check_adjacent_levels(current_report):
            count_of_safe_reports += 1
        else:
            for number in enumerate(current_report):
                temp_report = current_report.copy()
                temp_report.pop(number[0])
                if check_increasing_decreasing(temp_report) and check_adjacent_levels(temp_report):
                    count_of_safe_reports += 1
                    break
    return str(count_of_safe_reports)


print("Safe reports found: " + puzzle_1())
print("Safe tolerant reports found: " + puzzle_2())
