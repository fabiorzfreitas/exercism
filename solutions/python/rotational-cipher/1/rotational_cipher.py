def rotate(text, key):
    output = []
    for i in text:
        if i.isalpha():
            if i.isupper():
                if ord(i) + key > 90:
                    output.append(chr(ord(i)+key-26))
                else:
                    output.append(chr(ord(i)+key))
            else:
                if ord(i) + key > 122:
                    output.append(chr(ord(i)+key-26))
                else:
                    output.append(chr(ord(i)+key))
        else:
            output.append(i)
    return ''.join(output)
