# Not really snake, but a dot that can move around like the snakes head.
# when it reaches a wall it is teleported to the other side (wraps around)

# The idea is to not represent positions as a (x,y) coordinate but as a single scalar value.

def prime_factors(n):
    #https://stackoverflow.com/a/22808285/1723886
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def get_residue_representation(num, possible_values):
    """Given a number return "num mod p_i" for all prime factors p_i of possible_values. Returned as a tuple, in order."""
    # it is taken for given that if possible_values is 15 then valid num are [0-14] inclusive.
    return tuple([num % p for p in prime_factors(possible_values)])

def get_full_representation_table(possible_values):
    return {i:get_residue_representation(i, possible_values) for i in range(possible_values)}

def gcd(m, n):
    if m == 0:
        return n
    else:
        return gcd(n % m, m)

def extended_gcd(a,b):
    # https://www.discoverbits.in/post/extended-euclid-algorithm-for-gcd-in-python/
	if (b == 0):
        # if b = 0, then return g = a, m=1, n=0
		return (a,1,0)	
	else:
        # if b is not 0, then recursively call the function to get the value of
        # g,m,n at each step.
		(g,m,n) = extended_gcd(b, a%b)
		return(g, n, m-(a//b)*n )

# find m' and n' such that m * m' + n * n' = 1
# m = 3
# n = 83

# print(extended_gcd(n, m))

# exit()

# 253 = 11 * 23
# 249 = 3 * 83
WIDTH = 11
HEIGHT = 23
volume = WIDTH * HEIGHT
m = WIDTH
n = HEIGHT

_, m_, n_ = extended_gcd(m, n)
print(extended_gcd(m, n))

unit_vectors = {
    'x':    WIDTH*m_,
    'y':    HEIGHT*n_,
}

# get all combinations to brute force find which values represent the unit vectors
for key, value in get_full_representation_table(volume).items():
    x, y = value
    if value == (0, 1):
        unit_vectors['y'] = key
    if value == (1, 0):
        unit_vectors['x'] = key


player_pos = 0

def convert_to_tuple(player_pos):
    return (player_pos % WIDTH, player_pos % HEIGHT)

def print_player_coordinates():
    print(convert_to_tuple(player_pos))


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