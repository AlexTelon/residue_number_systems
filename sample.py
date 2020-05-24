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

# # checking the A006881.txt file
# with open('A006881.txt', 'r') as f:
#     lines = f.read().splitlines()
#     data = []
#     for line in lines:
#         _, value =  line.split()
#         data.append(int(value))

# for i in data:
#     print(i)
#     table = get_full_representation_table(i)
#     def unique_were_found(values):
#         return len(values) == len(set(values))
    
#     # we want to check if all keys have unique values.
#     if not unique_were_found(table.values()):
#         print(f"{i} duplicates found! - prime factors: {prime_factors(i)}")



# for key, value in representation.items():
#         print(key, value)
# print('----')
# print(f"modulu roof: {possible_values}, prime factors of it: {prime_factors(possible_values)}")

representation = get_full_representation_table(253)
# for key, value in representation.items():
#         print(key, value)
print(representation.values())

import matplotlib.pyplot as plt
import numpy as np

values = list(representation.values())
data = np.array(values)
data = data.T
x, y = data

color = (0,0,0)
area = np.pi*3
# plt.scatter(x, y, s=area, c=color, alpha=0.5)
# plt.title('Scatter plot pythonspot.com')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

animation_time = 10
step_time = animation_time / len(x)
# for i in range(len(x)):
#     print(int((i / len(x)) * 255))
# exit()

for i in range(len(x)):
    color = (0,((i / len(x)) * 1) ,0)
    print(color)
    plt.plot(x[i], y[i], color=color, marker='o', alpha=0.5)
    plt.pause(step_time)
plt.show()