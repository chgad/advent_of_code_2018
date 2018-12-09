import re
import numpy as np


def find_max(list_of_rect):
    max_x = 0
    max_y = 0

    for rect in list_of_rect:
        x_coord = rect[1] + rect[3]
        y_coord = rect[2] + rect[4]
        if x_coord > max_x:
            max_x = x_coord
        if y_coord > max_y:
            max_y = y_coord

    return max_x, max_y


def get_id(x, y, list_of_rect):
    for shape in list_of_rect:
        if (y, x) == (shape[1], shape[2]):
            print(shape)

    return 0


def calc_overlap_id(file_name):

    pattern = re.compile(r"#([0-9]*) @ ([0-9]*),([0-9]*): ([0-9]*)x([0-9]*)")
    with open(file_name, "r") as f:
        shapes = [tuple(map(lambda i: int(i), pattern.match(line).groups())) for line in f.readlines()]
    # max_x, max_y = find_max(shapes)

    fabric = np.zeros(find_max(shapes))
    for shape in shapes:
        i_d, y_start, x_start, y_diff, x_diff = shape
        muster = np.ones((y_diff, x_diff))
        fabric[y_start:y_start+y_diff, x_start:x_start+x_diff] += muster

    overlap_cnt = np.where(fabric == 1)

    y, x = overlap_cnt[0][0], overlap_cnt[1][0]
    return get_id(x,y,shapes)


file_name = "my_input.txt"

print(calc_overlap_id(file_name))