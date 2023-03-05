import argparse

"""
Cipher text decrypter using Caesar cipher.

Example:
    Command: python decrypt.py -t cjuuv -k 1
    Output: bittu
"""

parser = argparse.ArgumentParser(
            prog = 'Cipher text decrypter',
            description = 'Decrypt any cipher text to plain text using caesar cipher.',
            epilog = 'Example: python decrypt.py -t cjuuv -k 1'
        )

parser.add_argument(
            '-c', '--cipher',
            type=str,
            required=True,
            help='The cipher text to be decrypted'
        )
parser.add_argument(
            '-k', '--key',
            type=int,
            required=True,
            help='The key by which plain text will encrypted.'
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

print(f"Ciphet Text ->\t {args.cipher}")
print(f"Key ->\t {args.key}")
print(f"Plain Text ->\t {D(k=args.key, c=args.cipher)}")
