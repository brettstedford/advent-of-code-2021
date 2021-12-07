from common import get_input_as_lines

lines: list[str] = get_input_as_lines('day2')

x = 0
y = 0
aim = 0

for (i, val) in enumerate(lines):  
    command = val.split(' ')[0]
    velocity = int(val.split(' ')[1])

    if(command == 'down'):
        aim += velocity

    if(command == 'up'):
        aim -= velocity

    if(command == 'forward'):
        x += velocity
        y += velocity*aim

print(x * y)
