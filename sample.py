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

# for i in range(250, 256):
#     print(i, prime_factors(i))
# exit()

def get_residue_representation(num, possible_values):
    """Given a number return "num mod p_i" for all prime factors p_i of possible_values. Returned as a tuple, in order."""
    # it is taken for given that if possible_values is 15 then valid num are [0-14] inclusive.
    return tuple([num % p for p in prime_factors(possible_values)])
        

# representation = {i:(i % 3, i % 5) for i in range(n)}
possible_values = 255
representation = {i:get_residue_representation(i, possible_values) for i in range(possible_values)}

for key, value in representation.items():
    print(key, value)

print('----')
print(f"modulu roof: {possible_values}, prime factors of it: {prime_factors(possible_values)}")