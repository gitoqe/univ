key = 13
mode = 'decrypt'
original = 'Uryy2Jqn5x1r66Jz!J2yqJs5vr1q'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'abcdefghijklmnopqrstuvwxyz' + '1234567890' + ' !?.'
result = ''
for symbol in original:
    if symbol in SYMBOLS:
        symbol_index = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            translated_index = symbol_index + key
        elif mode == 'decrypt':
            translated_index = symbol_index - key
        if translated_index >= len(SYMBOLS):
            translated_index = translated_index - len(SYMBOLS)
        elif translated_index < 0:
            translated_index = translated_index + len(SYMBOLS)

        result = result + SYMBOLS[translated_index]
    else:
        result = result + symbol
print("IN: ", original)
print("OUT: ", result)
