def add_commas(val):
    empty_string = ""
    for i in range(0, len(val), 3):
        empty_string += str([0:i]) + ","
    return empty_string

print(add_commas{1234})
