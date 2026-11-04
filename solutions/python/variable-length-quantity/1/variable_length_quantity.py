from itertools import chain


def HexToBin(hex):
    output = [format(number, 'b') for number in hex]
    return output


def BinToHex(bin):
    output = []
    for octets in bin:
        vlq = []
        for octet in octets:
            vlq.append(format(int(octet, 2), 'X'))
        output.append(vlq)
    return output


def cutter(binary):
    reversed_binary = binary[::-1]
    for i in range(0, len(reversed_binary), 7):
        yield reversed_binary[i:i + 7][::- 1].zfill(7)


def encode(numbers):
    output = []
    for binary in HexToBin(numbers):
        with_eigth = []
        chunks = list(cutter(binary))
        for i, sequence in enumerate(chunks):
            if i == 0:
                sequence = '0' + sequence
            else:
                sequence = '1' + sequence
            with_eigth.append(sequence)
        output.append(with_eigth[::-1])    
    final = list(chain.from_iterable(BinToHex(output)))
    return list(map(lambda x: int(x, 16), final))


def decode(bytes_):
    number = []
    full_binaries = []
    for binary in HexToBin(bytes_):
        if binary.zfill(8)[0] == '1':
            number.append(binary.zfill(8)[1:])
        elif binary.zfill(8)[0] == '0':
            number.append(binary.zfill(8)[1:])
            full_binaries.append(''.join(number))
            number = []
    if full_binaries == []:
        raise ValueError("incomplete sequence")
    return list(map(lambda x: int(int(x, 2)), full_binaries))

