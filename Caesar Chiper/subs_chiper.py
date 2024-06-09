"""Caesar Cipher, by Al Sweigart al@inventwithpython.com
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.
More info at: https://en.wikipedia.org/wiki/Caesar_cipher
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, cryptography, math"""

try: 
    import pyperclip 
except ImportError:
    pass

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
    print("Do you want to encrypt or decrypt?")
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break 
    print("Please enter the letter e or d")


while True:
    maxKey = len(SYMBOLS) -1
    print('Please enter the key (0 to {}) to use'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

print('Enter the message to {}'.format(mode))
message = input('>')

message = message.upper()

translated = ''


for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        translated = translated + SYMBOLS[num]

    else:
        translated = translated + symbol

print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass 