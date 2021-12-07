from common import get_input_as_lines


lines: list[str] = get_input_as_lines('day2')

x = 0
y = 0

for (i, val) in enumerate(lines):  
    axis = val.split(' ')[0]
    velocity = int(val.split(' ')[1])

    if(axis == 'down'):
        y += velocity

    if(axis == 'up'):
        y -= velocity

    if(axis == 'forward'):
        x += velocity

print(x * y)
