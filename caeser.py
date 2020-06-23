low_ascii = 65
high_ascii = 90
magic_number = 7
alpha = [chr(i) for i in range(low_ascii, high_ascii+1)]

def encode(inString):
    inString = inString.upper()
    outString = []
    for char in inString:
        try:
            index = alpha.index(char)
        except ValueError:
            outString.append(char)
            continue

        if (index + low_ascii) > (high_ascii - magic_number):
            valid_char = alpha[index - (len(alpha) - magic_number)]
            outString.append(valid_char)
        else:
            outString.append(chr(index + low_ascii + magic_number))
    return outString


def decode(inString):
    outString = []
    for char in inString:
        try:
            index = alpha.index(char)
        except ValueError:
            outString.append(char)
            continue

        if index < magic_number:
            decoded_char = (alpha.index(char) + len(alpha) - magic_number) + low_ascii
        else:
            decoded_char = alpha.index(char) + low_ascii - magic_number
        outString.append(chr(decoded_char))
    return outString

