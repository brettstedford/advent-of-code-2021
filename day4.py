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

def check_card(numbers: list[int], card: list[list[int]]):
    bingo = False
    
    complete_card = []

    # for _, current_num in enumerate(numbers):
    #     for _, line in enumerate(card):
    #         for _, number in enumerate(line):

    
    return bingo

def get_score(number: int, card: list[list[int]]):
    return 0

def play_bingo(numbers:list[int], cards: list[list[list[int]]]):
    called:list[int] = []

    for _, current_num in enumerate(numbers):
        called.append(current_num)

        for _, card in enumerate(cards):
            bingo = check_card(called, card)

            if(bingo):
                return get_score(current_num, card)

    return 0


input = list(filter(lambda line: line != '', map(lambda line: line.strip('\n'), get_input('day4').readlines())))
random_numbers = parse_called_numbers(input)
bingo_cards = parse_bingo_cards(input)

print(play_bingo(random_numbers, bingo_cards))
