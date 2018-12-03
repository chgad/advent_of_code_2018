

def calculate_frequenzy(input_file):
    num = 0
    freq_chain = open(input_file, "r").readlines()

    for instruction in map(lambda x: int(x), freq_chain):
        num += instruction

    return num


file_name = "my_input.txt"

end_freq = calculate_frequenzy(file_name)

print(end_freq)
