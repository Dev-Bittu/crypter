# Caesar Cipher
The Caesar Cipher technique is one of the earliest and simplest methods of encryption technique.
It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter with a fixed number of positions down the alphabet.
For example with a shift of 1, A would be replaced by B, B would become C, and so on.
The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials.

Thus to cipher a given text we need an integer value, known as a shift which indicates the number of positions each letter of the text has been moved down.
The encryption can be represented using modular arithmetic by first transforming the letters into numbers, according to the scheme, A = 0, B = 1,…, Z = 25. Encryption of a letter by a shift n can be described mathematically as.

![Caesar cipher example image](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZmHqYQP9IDlzp5a21-1eDLwVb-rm8KQrYig&usqp=CAU)

---

### Advantages & Disadvantages
##### Advantages
  1. Easy to implement and use thus, making suitable for beginners to learn about encryption.
  2. Can be physically implemented, such as with a set of rotating disks or a set of cards, known as a scytale, which can be useful in certain situations.
  3. Requires only a small set of pre-shared information.
  4. Can be modified easily to create a more secure variant, such as by using a multiple shift values or keywords.

##### Disadvantages
  1. It is not secure against modern decryption methods.
  2. Vulnerable to known-plaintext attacks, where an attacker has access to both the encrypted and unencrypted versions of the same messages.
  3. The small number of possible keys means that an attacker can easily try all possible keys until the correct one is found, making it vulnerable to a brute force attack.
  4. It is not suitable for long text encryption as it would be easy to crack.
  5. It is not suitable for secure communication as it is easily broken.
  6. Does not provide confidentiality, integrity, and authenticity in a message.

---

### Algorithm for Caesar Cipher: 
##### Input: 
  - A String of lower case letters, called Text.
  - An Integer between 0-25 denoting the required shift.
##### Procedure
Traverse the given text one character at a time .
For each character, transform the given character as per the rule, depending on whether we’re encrypting or decrypting the text.
Return the new string generated.

---

### How to encrypt, decrypt & brute force?
##### Encrypt
For encryption,
Type this on your terminal:
```bash
python encrypt.py -t bittu -k 1
```
If you get the following output, means it correctly working:
```bash
Plain Text ->    bittu
Key ->   1
Cipher Text ->   cjuuv
```
##### Decryt
For decryption,
Type this on your terminal:
```bash
python decrypt.py -c cjuuv -k 1
```
If you get the following output, means it correctly working:
```bash
Ciphet Text ->   cjuuv
Key ->   1
Plain Text ->    bittu
```

##### Brute force
For brute force,
Type this on your terminal:
```bash
python brute_force.py -c ovggh
```
If you get the following output, means it correctly working:
```bash
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
...
```

