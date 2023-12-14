import re

def check_variable(variable_name):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    match = re.match(pattern, variable_name)
    return bool(match)


def check_data_type(data_type):
    valid_data_types = ['int', 'string', 'char', 'bool', 'float']
    return data_type in valid_data_types


def check_special_character(special_character):
    valid_special_character = ['[]', '[', ']', ';', '=']
    return special_character in valid_special_character


def check_number(number):
    return number.isdigit()


prompts = [
    'int[] arr1;',
    '1int[] arr;',
    'string[] my_array = new int[];',
    'bool[] _arr = new int[];',
    'float[] float_array_1 = new int[]',
    'float[] arr Ω new int[];',
]

for prompt in prompts:
    tokens = re.findall(r'\b\w+\b|\[.*?\]|\d+|[^\w\s]', prompt)

    flag = 0
    for token in tokens:
        if not (check_variable(token) or check_data_type(token) or check_special_character(token) or check_number(token)):
            flag = 1

    if flag == 0:
        print(f'Valid RE - {prompt}')
    else:
        print(f'Invalid RE - {prompt}')
