from itertools import chain


def DecToBin(hex):
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
    output = []
    reversed_binary = binary[::-1]
    for i in range(0, len(reversed_binary), 7):
        output.append(reversed_binary[i:i + 7][::- 1].zfill(7))
    return output


def encode(numbers):
    binary_chunks = []
    for binary in DecToBin(numbers):
        with_eigth = []
        chunks = cutter(binary)
        for i, sequence in enumerate(chunks):
            if i == 0:
                sequence = '0' + sequence
            else:
                sequence = '1' + sequence
            with_eigth.append(sequence)
        binary_chunks.append(with_eigth[::-1])    
    output = list(chain.from_iterable(BinToHex(binary_chunks)))
    return [int(x, 16) for x in output]


def decode(bytes_):
    number = []
    full_binaries = []
    for binary in DecToBin(bytes_):
        if binary.zfill(8)[0] == '1':
            number.append(binary.zfill(8)[1:])
        elif binary.zfill(8)[0] == '0':
            number.append(binary.zfill(8)[1:])
            full_binaries.append(''.join(number))
            number = []
    if full_binaries == []:
        raise ValueError("incomplete sequence")
    return [int(x, 2) for x in full_binaries]

