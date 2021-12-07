import os

def get_cwd():
    return os.getcwd()

def get_input(day:str):
    return open(f'{get_cwd()}\\input\\{day}.txt', 'r')

def parseInt(val: str):
    return int(val.strip('\n'))

def parseStr(val: str):
    return val.strip('\n')

def get_input_as_lines(day:str, mapFunc=parseStr):
    input = get_input(day)
    return list(map(mapFunc, input.readlines()))