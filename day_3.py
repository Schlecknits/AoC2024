import re


def input_reader(file):
    for line in file:
        yield [int(num) for num in line.strip().split()]

    file.close()


def multiplicator(pairs):
    result = 0
    for pair in pairs:
        result += pair[0] * pair[1]
    return result


def puzzle_1(re_mul):
    f = open("input_3.txt", "r")  # input as .txt file
    mul_pairs = [[int(num) for num in pair] for pair in re.findall(re_mul, f.read())]
    f.close()
    return str(multiplicator(mul_pairs))


def puzzle_2(re_mul, re_start, re_closed_do_dont, re_last):
    f = open("input_3.txt", "r")  # input as .txt file
    text = f.read()
    first_match = re.match(re_start, text)
    code_to_be_executed = first_match.groups()[0]
    text = text[first_match.span()[1]:]
    for part in re.findall(re_closed_do_dont, text):
        code_to_be_executed += part
    code_to_be_executed += re.match(re_last, text).groups()[0]
    mul_pairs = [[int(num) for num in pair] for pair in re.findall(re_mul, code_to_be_executed)]
    return str(multiplicator(mul_pairs))



re_multiplication = re.compile(r"(?:mul\()(\d{1,3}),(\d{1,3})\)")
re_until_dont = re.compile(r"([\s\S]*?)don't\(\)")
re_closed_blocks = re.compile(r"do\(\)([\s\S]*?)don't\(\)")
re_do_after_last_dont = re.compile(r"[\s\S]+don't\(\)[\s\S]+?do\(\)([\s\S]+)")
print("The combined result of all multiplications is: " + puzzle_1(re_multiplication))
print("The combined result of all enabled multiplications is: " + puzzle_2(re_multiplication, re_until_dont,
                                                                           re_closed_blocks, re_do_after_last_dont))