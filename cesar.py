
alphabet = 'abcdefghijklmnopqrstuvwxyz'
sample_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


def decrypt(to_decrypt, shift):
    # Tranlate the alphabet
    translated = alphabet[shift:] + alphabet[:shift]

    # Add result in a dictionary
    decode_dict = dict(zip(alphabet, translated))

    # Apply transformation to every character and store in a list
    list = []
    for char in to_decrypt:
        decoded_char = decode_dict.get(char)
        if decoded_char is not None:
            list.append(decoded_char)
        else:
            list.append(char)
    result = "".join(list)
    return result


def decryp_alt(to_decrypt, shift):
    # Translate the alphabet
    translated = alphabet[shift:] + alphabet[:shift]
    transtab = str.maketrans(alphabet, translated)

    # Translate string
    return to_decrypt.translate(transtab)
