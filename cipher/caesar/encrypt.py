import argparse

"""
Plain text encrypter using Caesar cipher.

Example:
    Command: python encrypt.py -t bittu -k 1
    Output: cjuuv 
"""

parser = argparse.ArgumentParser(
            prog = 'Plain text encrypter',
            description = 'Encrypt any plain text to cipher text using caesar cipher.',
            epilog = 'Example: python encrypt.py -t bittu -k 1'
        )

parser.add_argument(
            '-t', '--text',
            type=str,
            required=True,
            help='The plain text that will encrypted'
        )
parser.add_argument(
            '-k', '--key',
            type=int,
            required=False,
            default=1,
            help='The key by which plain text will encrypted. (default: 1)'
        )

args = parser.parse_args() # parsing arguments

def E(k: int, p: str):
    """
    Caesar cipher encryption logic
    """
    p = p.lower()
    k %= 26 # mod of 26 because of only 26 latters exists

    cipher_text = ""

    encrypt = [
                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
            ]

    for char in p:
        cipher_text += encrypt[
            (encrypt.index(char)+k)%26
        ] # mod of 26 because error will IndexOutOfRange will generated if it cross the z alpabet

    return cipher_text

print(f"Plain Text ->\t {args.text}")
print(f"Key ->\t {args.key}")
print(f"Cipher Text ->\t {E(k=args.key, p=args.text)}")
