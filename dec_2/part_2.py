import difflib

def find_closest_id(file_name):
    file = open(file_name, "r")
    strings = [x[:-1] for x in file.readlines()]
    file.close()
    closest_length = 0
    closest_string = ""
    list_len = len(strings)
    for i_d in strings:

        close_matches = difflib.get_close_matches(i_d, strings, n=2)  # get string which is closest to current
        # i_d = "".join([c for c in i_d if c in close_matches[1]])
        for i in difflib.ndiff(i_d, close_matches[1]):  # remove different chars
            # print(i_d)
            if i[:-1] == "  ":
                continue
            i_d = i_d.replace(i[-1], "")

        id_len = len(i_d)
        if id_len > closest_length:
            closest_length = id_len
            closest_string = i_d

    return closest_string


file_name = "my_input.txt"
# list(difflib.ndiff("abvc", "abtc"))
print(find_closest_id(file_name))
