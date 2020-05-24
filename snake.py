# Not really snake, but a dot that can move around like the snakes head.
# when it reaches a wall it is teleported to the other side (wraps around)

# The idea is to not represent positions as a (x,y) coordinate but as a single scalar value.

WIDTH = 3
HEIGHT = 5
volume = WIDTH * HEIGHT

player_pos = 0

def convert_to_tuple(player_pos):
    return (player_pos % WIDTH, player_pos % HEIGHT)

def print_player_coordinates():
    print(convert_to_tuple(player_pos))

import operator
unit_vectors = {
    'x':    6,
    'y':    10,
}
movements = {
    'up':       unit_vectors['y'],
    'down':     -unit_vectors['y'],
    'right':    unit_vectors['x'],
    'left':     -unit_vectors['x'],
}

def move(direction):
    global player_pos
    def is_multi_direction(direction):
        return ',' in direction

    if is_multi_direction:
        directions = direction.split(',')
        directions = [d.strip() for d in directions]
    else:
        directions = [direction]

    for d in directions:
        player_pos += movements[d]


print(f"width: {WIDTH}, height {HEIGHT}")
print(f'valid input: {list(movements.keys())}')
print()

last_instruction = 'up, down' # provide a nop default instruction
while True:
    print_player_coordinates()
    instruction = input()
    if instruction == '':
        instruction = last_instruction

    move(instruction)
    last_instruction = instruction