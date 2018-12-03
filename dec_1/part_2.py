def calculate_frequenzy(input_file):
    num = 0
    reached_freq = [0, ]
    freq_chain = open(input_file, "r").readlines()
    instructions = map(lambda x: int(x), freq_chain)
    re_do_for = 1
    while True:
        for inst in instructions:
            num += inst
            if num in reached_freq:
                return num, re_do_for
            reached_freq.append(num)
        re_do_for += 1


file_name = "my_input.txt"

end_freq, re_do = calculate_frequenzy(file_name)

print(end_freq)
print("With {} re-do's".format(re_do))
