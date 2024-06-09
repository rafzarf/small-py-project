try: 
    import pyperclip 
except ImportError:
    pass

print('===VIGENERE CHIPER===')

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


print('Please enter the key to use')
key = input('> ').upper()

print('Enter the message to {}'.format(mode))
message = input('>').upper()

translated = ''

key_index = 0
key = key.upper()

for symbol in message:
    num = SYMBOLS.find(symbol)
    if num != -1:  # -1 means symbol was not found in SYMBOLS
        if mode == 'encrypt':
            num += SYMBOLS.find(key[key_index])
        elif mode == 'decrypt':
            num -= SYMBOLS.find(key[key_index])

        num %= len(SYMBOLS)  # Handle the wrap-around

        translated += SYMBOLS[num]
        key_index = (key_index + 1) % len(key)  # Move to the next letter in the key
    else:
        translated += symbol

print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass 