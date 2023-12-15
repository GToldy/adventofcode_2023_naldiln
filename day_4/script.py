FILENAME = './day_4/input.txt'

def import_input():
    with open(FILENAME, 'r') as file:
        lines = file.read().splitlines()

    data = []
    for line in lines:
        temp_line = line.split(': ')[1].strip().split(' | ')
        temp_line[0] = temp_line[0].replace('  ', ' ').strip().split(' ')
        temp_line[1] = temp_line[1].replace('  ', ' ').strip().split(' ')
        data.append(temp_line)

    return data

data = import_input()
all_cards = []

def sum_of_winning_cards():
    total_sum = 0
    for i, line in enumerate(data):
        winning_nums = line[0]
        my_nums = line[1]
        count = 0
        for num in my_nums:
            if num in winning_nums:
                count += 1
        total_sum += pow(2, count - 1) if count else 0
        all_cards.append({
            'index': i,
            'quantity': 1,
            'count': count,
            'line': line
        })
    return total_sum

def get_number_of_cards():
    for card in all_cards:
        line = card['index']
        count = card['count']
        quantity = card['quantity']

        for i in range(1, count + 1):
            all_cards[line + i]['quantity'] += 1 * card['quantity']

def count_all_cards():
    get_number_of_cards()
    sum = 0
    for card in all_cards:
        sum += card['quantity']
    return sum


print(sum_of_winning_cards())
print(count_all_cards())