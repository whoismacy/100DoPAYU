with open("/home/shrmrm/random.txt") as file:
    content = file.read()
    print(content)

with open("new_file.txt", mode="w") as write:
    write.write("\nThis is a new file and I am appending text.")
