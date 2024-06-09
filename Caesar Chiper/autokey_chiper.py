try: 
    import pyperclip 
except ImportError:
    pass

print('===AUTO-KEY VIGENERE CIPHER===')

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


print('Please enter the Auto KEY to use')
key = input('> ').upper()

print('Enter the message to {}'.format(mode))
message = input('>').upper()


translated = ''
key_index = 0
key_extended = key

if mode == 'encrypt':
    key_extended += message
    key_extended = key_extended[:len(message)]
elif mode == 'decrypt':
    pass


for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num += SYMBOLS.find(key_extended[key_index])
            translated_symbol = SYMBOLS[num % len(SYMBOLS)]
            translated += translated_symbol
            key_extended += symbol
        elif mode == 'decrypt':
            num -= SYMBOLS.find(key_extended[key_index])
            translated_symbol = SYMBOLS[num % len(SYMBOLS)]
            translated += translated_symbol
            key_extended += translated_symbol  

        key_index += 1
    else:
        translated += symbol

print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass 