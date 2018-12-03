
def find_checksum(file_name):
    file = open(file_name,"r")
    strings = [x[:-1] for x in file.readlines()]
    file.close()
    cnt_twos = 0
    cnt_threes = 0

    for i_d in strings:
        letters = set(i_d)
        counts = [i_d.count(letter) for letter in letters]
        reduced = set(counts)
        if 2 in reduced:
            cnt_twos += 1
        if 3 in reduced:
            cnt_threes += 1

    return cnt_twos * cnt_threes

file_name = "my_input.txt"

print(find_checksum(file_name))

