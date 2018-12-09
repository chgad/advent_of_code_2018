import re
import numpy as np

def find_max(list_of_rect):
    max_x = 0
    max_y = 0

    for rect in list_of_rect:
        x_coord = rect[0] + rect[2]
        y_coord = rect[1] + rect[3]
        if x_coord > max_x:
            max_x = x_coord
        if y_coord > max_y:
            max_y = y_coord

    return max_x, max_y


def calc_overlap(file_name):

    pattern = re.compile(r"#[0-9]* @ ([0-9]*),([0-9]*): ([0-9]*)x([0-9]*)")
    with open(file_name, "r") as f:
        shapes = [tuple(map(lambda x: int(x), pattern.match(line).groups())) for line in f.readlines()]
    # max_x, max_y = find_max(shapes)

    fabric = np.zeros(find_max(shapes))
    for shape in shapes:
        y_start, x_start, y_diff, x_diff = shape
        muster = np.ones((y_diff, x_diff))
        fabric[y_start:y_start+y_diff, x_start:x_start+x_diff] += muster

    overlap_cnt = len(np.where(fabric > 1)[0])

    return overlap_cnt


def calc_overlap_two(file_name, test_string=""):
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()
    pattern = re.compile(r"#[0-9]* @ ([0-9]*),([0-9]*): ([0-9]*)x([0-9]*)")
    shapes = [tuple(map(lambda x: int(x), pattern.match(line).groups())) for line in lines]
    print(shapes)
    overlap = 0
    i = 0

    for shape in shapes:
        dagger_x = shape[0]
        dagger_y = shape[1]
        star_x = dagger_x + shape[2]
        minus_y = dagger_y + shape[3]
        for an_shape in shapes:

            if shape is an_shape[i:]:
                continue

            zero_x = an_shape[0]
            zero_y = an_shape[1]
            one_x = zero_x + an_shape[2]
            two_y = zero_y + an_shape[3]
            if zero_x >= star_x or dagger_x >= one_x or dagger_y >= two_y or zero_y >= minus_y:
                continue

            if zero_x > dagger_x:
                if dagger_y > zero_y:
                    overlap += (star_x - zero_x) * (two_y - dagger_y)
                else:
                    overlap += (star_x - zero_x) * (minus_y - zero_x)
            elif zero_x < dagger_x:
                if dagger_y > zero_y:
                    overlap += (one_x - dagger_x) * (two_y - dagger_y)
                else:
                    overlap += (one_x - dagger_x) * (minus_y - zero_y)
            else:
                overlap += shape[2] * an_shape[3]
        i += 1
    return overlap


file_name = "my_input.txt"

print(calc_overlap(file_name))

