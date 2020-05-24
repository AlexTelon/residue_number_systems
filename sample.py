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
        

def get_full_representation_table(possible_values):
    return {i:get_residue_representation(i, possible_values) for i in range(possible_values)}

# The prime facors should be relatively prime. non-square semiprimes are good candidates as they have 2 factors and they are all prime
# let us investigate what happens with different values.
for i in range(100):
    table = get_full_representation_table(i)
    def unique_were_found(values):
        return len(values) == len(set(values))
    
    # we want to check if all keys have unique values.
    if not unique_were_found(table.values()):
        print(f"{i} duplicates found! - prime factors: {prime_factors(i)}")



# for key, value in representation.items():
#         print(key, value)
# print('----')
# print(f"modulu roof: {possible_values}, prime factors of it: {prime_factors(possible_values)}")

print(get_full_representation_table(4))