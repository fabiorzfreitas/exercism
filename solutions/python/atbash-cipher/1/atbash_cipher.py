cipher = 'abcdefghijklmnopqrstuvwxyz'

def encode(plain_text):
    count = 0
    output = []
    for char in plain_text.lower():
        if char.isalnum():
            count += 1
            if char.isnumeric():
                output.append(char)
            else:
                output.append(cipher[- cipher.index(char) - 1])
            if count == 5:
                output.append(' ')
                count = 0
    return ''.join(output).rstrip()


def decode(ciphered_text):
    output = []
    for char in ciphered_text:
        if char.isalnum():
            if char.isnumeric():
                output.append(char)
            else:
                output.append(cipher[- cipher.index(char) - 1])
    return ''.join(output)
