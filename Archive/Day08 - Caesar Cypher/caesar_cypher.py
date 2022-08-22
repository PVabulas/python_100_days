import art

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar(text, shift, direction):
    if direction == "decode":
        shift *= -1
    output = ""
    for char in text.lower():
        if char in alphabet:
            index = alphabet.index(char)
            shift_index = (index + shift) % 26
            output += alphabet[shift_index]
        else:
            output += char
    print(output)


print(art.logo)
while True:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt, or 'exit' to quit:\n"
    )
    if direction == "exit":
        break
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
print("Goodbye!")
