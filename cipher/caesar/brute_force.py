import argparse

"""
Brute force for Caesar cipher to convert cipher text into plain text without using key.
Example:
    Command: python brute.py -c ovggh
    Output: 
        KEY -> DECRYPTED MESSAGE
        0 -> ovggh
        1 -> nuffg
        2 -> mteef
        3 -> lsdde
        4 -> krccd
        5 -> jqbbc
        6 -> ipaab
        7 -> hozza
        8 -> gnyyz
        9 -> fmxxy
        10 -> elwwx
        11 -> dkvvw
        12 -> cjuuv
        13 -> bittu
        14 -> ahsst
        15 -> zgrrs
        16 -> yfqqr
        17 -> xeppq
        18 -> wdoop
        19 -> vcnno
        20 -> ubmmn
        21 -> tallm
        22 -> szkkl
        23 -> ryjjk
        24 -> qxiij
        25 -> pwhhi
"""

parser = argparse.ArgumentParser(
            prog = 'Cipher text decrypter without key',
            description = 'Decrypt any cipher text to plain text without key',
            epilog = 'Example: python brute_force.py -c ovggh'
        )

parser.add_argument(                                          '-c', '--cipher',
            type=str,
            required=True,
            help='The cipher text to be decrypted'
        )

args = parser.parse_args() # parsing arguments

def D(k: int, c: str):
    """
    Caesar cipher decryption logic
    """
    c = c.lower()
    k %= 26 # mod of 26 because of only 26 latters exists

    plain_text = ""

    decrypt = [
                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
            ]

    for char in c:
        plain_text += decrypt[
            (decrypt.index(char)-k)%26
        ] # mod of 26 because error will IndexOutOfRange will generated if it cross the z alpabet

    return plain_text

print("KEY -> DECRYPTED MESSAGE")
for i in range(26):
    print(f"{i} -> {D(i, args.cipher)}")


