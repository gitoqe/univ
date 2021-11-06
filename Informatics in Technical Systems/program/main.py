def transorm_to_notation (number):
    result = ''
    int_num_part = int(number // 1)
    float_num_part = int(number % int_num_part)
    print(int_num_part)
    print(float_num_part)
    # print(len(str(float_num_part)))
    return result

def transform_to_base (number):
    base = 7
    result = ''
    while number > 0:
        new_number = str(number % base)
        print(new_number)
        result = new_number + result
        number = number // base
    return result

print('Enter number:')
user_nubmer = float(input())
print( transorm_to_notation(user_nubmer) )
