def vigenere_decode(message, keyword):
    decoded_message = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    keyword_phrase = ""
    keyword_index = 0
    for char in message:
        if char in alphabet:
            keyword_phrase += keyword[keyword_index]
            if keyword_index < len(keyword) - 1:
                keyword_index += 1
            else:
                keyword_index = 0
        else:
            keyword_phrase += char

    for i in range(len(message)):
        if message[i] in alphabet:
            offset = alphabet.find(keyword_phrase[i])
            starting_index = alphabet.find(message[i])
            ending_index = starting_index + offset
            new_char = alphabet[ending_index % 26]
            decoded_message += new_char
        else:
            decoded_message += message[i]
    print(decoded_message)
    return decoded_message

def vigenere_encode(message, keyword):
    encoded_message = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    keyword_phrase = ""
    keyword_index = 0
    for char in message:
        if char in alphabet:
            keyword_phrase += keyword[keyword_index]
            if keyword_index < len(keyword) - 1:
                keyword_index += 1
            else:
                keyword_index = 0
        else:
            keyword_phrase += char

    for i in range(len(message)):
        if message[i] in alphabet:
            offset = alphabet.find(keyword_phrase[i])
            starting_index = alphabet.find(message[i])
            ending_index = starting_index - offset
            new_char = alphabet[ending_index % 26]
            encoded_message += new_char
        else:
            encoded_message += message[i]
    print(encoded_message)
    return encoded_message