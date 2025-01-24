"""A practice on how to create and modify functions."""
def print_lyrics():
    print("I'm a lumberjack and I'm okay.")
    print("I sleep all night and I work all day.")

def repeat(word, n):
    print(word * n)

def print_right(string):
    string_len = len(string)
    diff = 40 - string_len
    print(" " * diff, string)

def triangle(string, integer):
    for i in range(1, (integer+1)):
        print(string * i)

def rectangle(string, width, height):
    for i in range(1, (height+1)):
        print(string * width)

def bottle_verse(value):
    for i in range(value, 0, -1):
        print(f"{i} bottles of beer on the wall,")
        print(f"{i} bottles of beer.")
        print("Take one down, pass it around,")
        print(f"{i -1} bottles of beer on the wall.")
        print("\n")
