original = 'Uryy2Jqn5x1r66Jz!J2yqJs5vr1q'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'abcdefghijklmnopqrstuvwxyz' + '1234567890' + ' !?.'
print("IN: ", original)
for key in range(len(SYMBOLS)):
    result = ''
    for symbol in original:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)
            translated_index = symbol_index - key
            if translated_index < 0:
                translated_index = translated_index + len(SYMBOLS)
            result = result + SYMBOLS[translated_index]
        else:
            result = result + symbol
    print('Key #%s: %s' % (key, result))
