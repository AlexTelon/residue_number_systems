# Not really snake, but a dot that can move around like the snakes head.
# when it reaches a wall it is teleported to the other side (wraps around)

# The idea is to not represent positions as a (x,y) coordinate but as a single scalar value.
import time

WIDTH = 3
HEIGHT = 5
volume = WIDTH * HEIGHT

player_pos = 0

def convert_to_tuple(player_pos):
    return (player_pos % WIDTH, player_pos % HEIGHT)

def print_player_coordinates():
    print(convert_to_tuple(player_pos))

import operator
movements = {
    'up':    10,
    'down':  -10,
    'right': 6,
    'left':  -6,
}

def move(direction):
    global player_pos
    player_pos += movements[direction]

print(f"width: {WIDTH}, height {HEIGHT}")
print(f'valid input: {list(movements.keys())}')
print()

last_instruction = ''
while True:
    print_player_coordinates()
    instruction = input()
    if instruction == '':
        instruction = last_instruction

    move(instruction)
    last_instruction = instruction