import re

# DATA = "data/01_test_a.txt"
# DATA = "data/01_test_b.txt"
DATA = "data/01.txt"

DIGITS_DICT = {
    "one": "1",
    "1": "1",
    "two": "2",
    "2": "2",
    "three": "3",
    "3": "3",
    "four": "4",
    "4": "4",
    "five": "5",
    "5": "5",
    "six": "6",
    "6": "6",
    "seven": "7",
    "7": "7",
    "eight": "8",
    "8": "8",
    "nine": "9",
    "9": "9",
}


def read_data(data):
    with open(file=data, mode="r") as f:
        l = f.readlines()
    return [ll.strip() for ll in l]


def find_first_substr_in_str(str_to_find, substrs):
    idx_found = 1000000  # assume no line longer than this
    substr_found = None
    for ss in substrs:
        idx = str_to_find.find(ss)
        if idx != -1 and idx < idx_found:
            idx_found = idx
            substr_found = ss
    if substr_found is not None:
        return substr_found, idx_found
    else:
        return None, None


def find_last_substr_in_str(str_to_find, substrs):
    idx_found = -1
    substr_found = None
    for ss in substrs:
        idx = str_to_find.rfind(ss)
        if idx != -1 and idx > idx_found:
            idx_found = idx
            substr_found = ss
    if substr_found is not None:
        return substr_found, idx_found
    else:
        return None


def a(data):
    l = read_data(data)
    digits = [re.findall(r"\d", ll) for ll in l]
    ints_first_last = [int(d[0] + d[-1]) for d in digits]
    return sum(ints_first_last)


def b(data):
    lines = read_data(data)
    sum_digits = 0
    for l in lines:
        substr_found_first, _ = find_first_substr_in_str(
            str_to_find=l, substrs=DIGITS_DICT.keys()
        )
        if substr_found_first is not None:
            digit_first = DIGITS_DICT[substr_found_first]
        else:
            digit_first = None
        substr_found_last, _ = find_last_substr_in_str(
            str_to_find=l, substrs=DIGITS_DICT.keys()
        )
        if substr_found_last is not None:
            digit_last = DIGITS_DICT[substr_found_last]
        else:
            digit_last = None
        digits_pair = digit_first + digit_last
        sum_digits = sum_digits + int(digits_pair)
    return sum_digits


sol_a = a(data=DATA)
print("sol 01a:", sol_a)
assert sol_a == 54968

sol_b = b(data=DATA)
print("sol_01b:", sol_b)
assert sol_b == 54094
