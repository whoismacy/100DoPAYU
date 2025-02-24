with open("Letters/invited_names.txt") as file:
    new_list = [line.strip() for line in file]

with open("Letters/starting_letter.txt") as file:
    template = file.read()

for name in new_list:
    pers_letter = template.replace('[name]', name)
    file_path = f"Letters/Output/{name}.txt"

    with open(file_path, "w") as temp_path:
        temp_path.write(pers_letter)
