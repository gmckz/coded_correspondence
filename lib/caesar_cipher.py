def caesar_decode(message, offset):
    decoded_message = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in message:
        if char in alphabet:
            starting_index = alphabet.find(char)
            ending_index = starting_index + offset
            new_char = alphabet[ending_index % 26]
            decoded_message += new_char
        else:
            decoded_message += char
    print(decoded_message)
    return decoded_message

def caesar_encode(message, offset):
    encoded_message = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in message:
        if char in alphabet:
            starting_index = alphabet.find(char)
            ending_index = starting_index - offset
            new_char = alphabet[ending_index % 26]
            encoded_message += new_char
        else:
            encoded_message += char
    print(encoded_message)
    return encoded_message