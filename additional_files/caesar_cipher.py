from caesar_name import LOGO
"Caesar Cipher in py"
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(text, offset):
    encrypted_text = ""
    for letter in text:
        new = (alphabet.index(letter) + offset) % len(alphabet)
        encrypted_text += alphabet[new]
    print("The encrypted text is: " + encrypted_text)

def decrypt(text, offset):
    decrypted_text = ""
    for letter in text:
        new = (alphabet.index(letter) - offset) % len(alphabet)
        decrypted_text += alphabet[new]
    print("The decrypted text is: " + decrypted_text)

def caesar_cipher(direction, text, offset):
    output = ""

    if direction == "decode":
        offset *= -1

    for letter in text:
        if letter not in alphabet:
            output += letter
        else:
            new = (alphabet.index(letter) + offset) % len(alphabet)
            output += alphabet[new]
    print(f"The {direction}d text is : {output}")


PLAY_AGAIN = True

print(LOGO)

while PLAY_AGAIN:
    user_choice = input("Would you like to 'encode' or 'decode ?\n").lower()
    offset = int(input("What is the offset you would like to apply ?\n"))
    text = input("Input your text below:\n").lower()

    caesar_cipher(direction=user_choice, offset=offset, text=text)

    user_choice1 = input("Would you like to play again ? 'yes' or 'no' ? ").lower()

    if user_choice1 == "yes":
        PLAY_AGAIN = True
    else:
        PLAY_AGAIN = False
