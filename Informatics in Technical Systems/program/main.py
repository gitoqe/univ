import math

def transorm_to_notation (number):
    result = ''
    if number < 0:
        number *= -1
        result = '-'
    fract_part, whole_part = math.modf(number)
    whole_part = find_whole_part(int(whole_part))
    fract_part = find_fract_part(fract_part)
    print('Whole part: ', whole_part)
    if len(fract_part):
        print('Fractional part: ', fract_part)
    return result + str(whole_part) + '.' + str(fract_part)

def find_whole_part (number, base = 7):
    '''Returns formatted number as string
    
    Parameters:
    number (int): given number
    base (int): given base

    Returns:
    result (str): formed number
    '''
    result = ''
    while number > 0:
        new_digit = str(number % base)
        result = new_digit + result
        number = number // base
    return result

def find_fract_part(number, base = 7, digit = 5):
    print(number)
    result = ''
    while (digit):
        number = number * base
        fract_part, whole_part = math.modf(number)
        number = fract_part
        result += str(int(whole_part))
        digit = digit - 1
    return result

def main():
    print('Enter number:')
    user_nubmer = float(input())
    print('\nYour number with base 7:')
    transformed_number = transorm_to_notation(user_nubmer)
    print('Result: ', transformed_number)

main()
