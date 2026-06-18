# Caesar Cipher
#
# This program can encode (encrypt) or decode (decrypt) messages
# using the Caesar Cipher technique.
#
# How it works:
# - Each letter is shifted by a user-specified amount.
# - Encoding shifts letters forward through the alphabet.
# - Decoding shifts letters backward through the alphabet.
# - Spaces, numbers, and punctuation are preserved.
#
# This project was built to practice:
# - Lists
# - Loops
# - Functions
# - String manipulation
# - User input
# - Basic encryption concepts

from art import logo

print(logo)

# Duplicate the alphabet to simplify letter shifting
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet = alphabet + alphabet

"""OR alphabet = alphabet * 2 to repeat the list"""


# Performs either encoding or decoding based on user choice
def caesar(original_text, shift_amount, encode_or_decode):
    encrypted_word = ""

    if encode_or_decode == "encode":

        # Shift letters forward through the alphabet
        for char in original_text:
            if char in alphabet:
                letter_shift = alphabet[alphabet.index(char) + shift_amount]

                encrypted_word += letter_shift

            else:
                encrypted_word += char

        print(f"Here is the encode result {encrypted_word}")

    elif encode_or_decode == "decode":
        decrypted_word = ""

        # Shift letters backward through the alphabet
        for char in original_text:
            if char in alphabet:
                letter_shift = alphabet[alphabet.index(char) - shift_amount]

                decrypted_word += letter_shift

            else:
                decrypted_word += char

        print(f"Here is the decoded result: {decrypted_word}")

    else:
        print("Invalid command")


# Continue running until the user chooses to exit
keep_running = True

while keep_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    continue_or_not = input("Do you want to continue? Type 'yes' or 'no' \n")

    if continue_or_not == "no":
        keep_running = False
        print("GOODBYE")