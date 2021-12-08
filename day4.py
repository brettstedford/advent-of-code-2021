from io import TextIOWrapper

from common import get_input

def parse_called_numbers(input: list[str]):
    numbers = list(map(int, input[0].strip('\n').split(',')))
    return numbers

def parse_bingo_cards(input: list[str]):
    cards: list[list[list[int]]] = []  
    
    start = 1

    while(start < len(input)):
        card: list[list[int]] = []

        for i in range(start, start+5):
            line = list(map(int, filter(lambda l: l != '', input[i].split(' '))))
            card.append(line)

        cards.append(card)
        start += 5

    return cards

def check_card(numbers: list[int], card: list[list[(int, bool)]]):
    bingo = False
    
    complete_card: list[list[(int, bool)]] = []

    for _, line in enumerate(card):
        complete_line: list[(int,bool)] = []

        for _, number in enumerate(line):
            complete_line.append((number, number in numbers))

        complete_card.append(complete_line)
    
    bingo = any(all(row[idx][1] for row in complete_card) for idx in range(0,4))

    if(bingo == False):
        bingo = any(all(number[1] for number in line) for line in complete_card)

    return (bingo, complete_card)

def get_score(number: int, card: list[list[(int, bool)]]):
    flattened = list(filter(lambda item: item[1] == False, [item for sublist in card for item in sublist]))
    unused = sum(list(map(lambda item: item[0], flattened)))
    print(number, unused)
    return number * unused

def play_bingo(numbers:list[int], cards: list[list[list[(int, bool)]]]):
    called:list[int] = []

    for i, current_num in enumerate(numbers):
        called.append(current_num)

        for j, card in enumerate(cards):
            bingo = check_card(called, card)
            print(i, j, current_num)

            if(bingo[0]):
                print(i, j)
                print(bingo[1])
                return get_score(current_num, bingo[1])

    return 0


input = list(filter(lambda line: line != '', map(lambda line: line.strip('\n'), get_input('day4').readlines())))
random_numbers = parse_called_numbers(input)
bingo_cards = parse_bingo_cards(input)

print(play_bingo(random_numbers, bingo_cards))
