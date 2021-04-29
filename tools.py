def encryptDecrypt(input, key):
    key = list(key)
    output = []

    for i in range(len(input)):
        xor_num = ord(input[i]) ^ ord(key[i % len(key)])
        output.append(chr(xor_num))
    return ''.join(output)
