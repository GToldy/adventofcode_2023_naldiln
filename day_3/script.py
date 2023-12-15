import string

FILENAME = './day_3/input.txt'

def import_input():
    with open(FILENAME, 'r') as file:
        temp_data = file.read().splitlines()
    data = []
    data.insert(0, 142 * '.')
    for line in temp_data:
        temp_line = '.' + line + '.'
        data.append(temp_line)
    data.append(142 * '.')
    return data

data = import_input()
gears = []


def check_gears(id):
    for i, gear in enumerate(gears, 1):
        if id == gear['id']:
            return i
    return 0

def get_numbers():
    numbers = []
    for i, row in enumerate(data):
        temp_number = ''
        for j, col in enumerate(row):
            if col.isnumeric():
                temp_number += col
            
            if (temp_number != '' and not col.isnumeric()) or (temp_number != '' and j == len(row) - 1):
                number = {
                    'row': i,
                    'col': j - len(temp_number),
                    'len': len(temp_number),
                    'num': temp_number
                }
                numbers.append(number)
                temp_number = ''
    return numbers

def get_valid_gears():
    gear_ratio_sum = 0
    for gear in gears:
        if len(gear['numbers']) > 1:
            temp_num = 1
            for num in gear['numbers']:
                temp_num *= num
            gear_ratio_sum += temp_num
    return gear_ratio_sum

def get_valid_numbers():
    all_numbers = get_numbers()
    valid_numbers = []
    for number in all_numbers:
        row, col, length, num = number['row'], number['col'], number['len'], number['num']
        neighbours = []


        row_1 = data[row - 1][col - 1:col + length + 1]
        print(row_1)
        if '*' in row_1:
            for i, char in enumerate(row_1):
                if char == '*':
                    gear_id = f'{row - 1}{col - 1 + i}'
                    index = check_gears(gear_id)
                    if index:
                        gears[index - 1]['numbers'].append(int(num))
                        break
                    else:
                        gear = {
                            'id': f'{row - 1}{col - 1 + i}',
                            'row': row - 1,
                            'col': col - 1 + i,
                            'numbers': []
                        }
                        gear['numbers'].append(int(num))
                        gears.append(gear)
                        break
        neighbours.extend(row_1)

        row_2 = data[row][col - 1:col + length + 1]
        print(row_2)
        if '*' in row_2:
            for i, char in enumerate(row_2):
                if char == '*':
                    gear_id = f'{row}{col - 1 + i}'
                    index = check_gears(gear_id)
                    if index:
                        gears[index - 1]['numbers'].append(int(num))
                        break
                    else:
                        gear = {
                            'id': f'{row}{col - 1 + i}',
                            'row': row,
                            'col': col - 1 + i,
                            'numbers': []
                        }
                        gear['numbers'].append(int(num))
                        gears.append(gear)
                        break
        neighbours.extend([data[row][col - 1], data[row][col + length]])

        row_3 = data[row + 1][col - 1:col + length + 1]
        print(row_3)
        if '*' in row_3:
            for i, char in enumerate(row_3):
                if char == '*':
                    gear_id = f'{row + 1}{col - 1 + i}'
                    index = check_gears(gear_id)
                    if index:
                        gears[index - 1]['numbers'].append(int(num))
                        break
                    else:
                        gear = {
                            'id': f'{row + 1}{col - 1 + i}',
                            'row': row + 1,
                            'col': col - 1 + i,
                            'numbers': []
                        }
                        gear['numbers'].append(int(num))
                        gears.append(gear)
                        break
        neighbours.extend(row_3)
        
        if len(set(neighbours)) > 1:
            valid_numbers.append(int(num))

    

    return sum(valid_numbers)




print(get_valid_numbers())
print(get_valid_gears())