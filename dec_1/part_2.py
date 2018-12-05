import numpy as np

def calculate_frequenzy(input_file):
    num = 0
    reached_freq = [0, ]
    file = open(input_file, "r")
    freq_chain = file.readlines()
    file.close()
    instructions = list(map(lambda x: int(x), freq_chain))
    re_do_for = 0
    while True:
        for inst in instructions:
            num += inst
            if num in reached_freq:
                return num, re_do_for
            reached_freq.append(num)
        re_do_for += 1

def calculate_frequenzy_two(input_file):
    num = 0
    reached_freq = [0, ]
    file = open(input_file, "r")
    freq_chain = file.readlines()
    file.close()
    instructions = list(map(lambda x: int(x), freq_chain))
    S_list = np.cumsum(instructions)
    N = len(S_list)
    S_N_1 = S_list[-1]
    m = 1
    while True:

        for n in range(m):
            res = (m-n) // N * S_N_1 + S_list[m % N] - S_list[n % N]

            if not res:
                return n // N * S_N_1 + S_list[n % N]
        m += 1


def calculate_frequenzy_three(input_file):
    file = open(input_file, "r")
    freq_chain = file.readlines()
    file.close()
    instructions = list(map(lambda x: int(x), freq_chain))
    S_list = np.cumsum(instructions)

    X, Y = np.meshgrid(S_list, S_list)
    res = (X-Y) % S_list[-1]
    alpha = np.where(res == 0)
    res_int = (X-Y) // S_list[-1]
    dummy = res_int[alpha]
    res_set = np.where(dummy == np.min(dummy[dummy > 0]))

    n_mod_N, m_mod_N = alpha[0][res_set[0][0]], alpha[1][res_set[0][0]]

    one, two = S_list[n_mod_N], S_list[m_mod_N]

    if one > two:
        print(one)
    else:
        print(two)


file_name = "my_input.txt"

# end_freq, re_do = calculate_frequenzy(file_name)
#
# print(end_freq)
# print("With {} re-do's".format(re_do))
#
# end_freq = calculate_frequenzy_another(file_name)
#
# print(end_freq)

calculate_frequenzy_three(file_name)