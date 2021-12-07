from common import get_input_as_lines, parseInt
   
def get_window(list: list[int], idx: int, size: int):
    if(idx + size > len(list)):
        return []

    return list[idx:idx+size]   

lines = get_input_as_lines('day1', parseInt)

prevWindow = 0
increases = 0
window_size = 3

for i, val in enumerate(lines):
    if(i == 0):
        prevWindow = get_window(lines, i, window_size)
        continue

    currentWindow = get_window(lines, i, window_size)
    prev = sum(prevWindow)
    cur = sum(currentWindow)

    if(cur > prev):
        increases += 1

    prevWindow = currentWindow

print(increases)

