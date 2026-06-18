from art import logo

print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet = alphabet + alphabet

"""OR alphabet = alphabet * 2 to repeat the list"""


def caesar(original_text, shift_amount, encode_or_decode):
    encrypted_word = ""

    if encode_or_decode == "encode":

        for char in original_text:
            if char in alphabet:
                letter_shift = alphabet[alphabet.index(char) + shift_amount]

                encrypted_word += letter_shift

            else:
                encrypted_word += char

        print(f"Here is the encode result {encrypted_word}")

    elif encode_or_decode == "decode":
        decrypted_word = ""
        for char in original_text:
            if char in alphabet:
                letter_shift = alphabet[alphabet.index(char) - shift_amount]

                decrypted_word += letter_shift

            else:
                decrypted_word += char

        print(f"Here is the decoded result: {decrypted_word}")

    else:
        print("Invalid command")





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







