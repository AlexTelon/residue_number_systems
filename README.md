# Trying out Residu number systems.

Chapter 4.7 in Concrete Mathematics.

Example from p 127 coded

Can generate an alternative representation for values now.

If we know 254 is the max number, so we have [0-254], then we can
represent each of those values with the result of:

(n % 3, n % 5, n % 17) where n is [0-254].

The claim from Graham et. al. is that we can perform addition,
subtraction and multiplication on the components of the tuple
independently.

Their example is:

7 * 13 modulu 15.
The format is: (n % 3, n % 5)
7   = (1, 2)
13  = (1, 3)
(1, 2) * (1, 3) = (1*1 % 3, 2*3 % 5) = (1, 1).

(1, 1) is a unique representation for the number 1 here.

This is intersting in of itself. But it is also interesting if it is
sometimes possible to go the other way around.

Imagine having a 2D graph, and that given that you know what ranges
x and y values can be in we could represent any position (x,y) with a
single scalar value. This is ofc trivial if we just assign a strategy in
which order to visit all possible points in the graph. But that might be
too slow and cumbersome if the number of potential solutions is large.

This might give us another way to go about it.

Why is a single number better than a tuple? Well if we have 64bit
numbers we might have an efficient way of encoding all positions in a
single scalar without creating cumbersome bitpatterns yourself.

Or maybe this is just for fun, duno. We will see!


## Does this work for any modulu?

The book explains that the prime factors need to be relatively prime.
So the factors for 15: (3, 5) work fine, but 256 (2, 2, 2, 2, 2, 2, 2, 2) wont.

A simple test shows that this seems to indeed be the case.

For numbers between 0-99 these are the only max_modulus in which duplicates were found.
Meaning that two values within that modulus had the same tuple representation.

The table below does not say which numbers had duplicates, on if there were any and what the prime factors are.

    4 duplicates found! - prime factors: [2, 2]
    8 duplicates found! - prime factors: [2, 2, 2]
    9 duplicates found! - prime factors: [3, 3]
    12 duplicates found! - prime factors: [2, 2, 3]
    16 duplicates found! - prime factors: [2, 2, 2, 2]
    18 duplicates found! - prime factors: [2, 3, 3]
    20 duplicates found! - prime factors: [2, 2, 5]
    24 duplicates found! - prime factors: [2, 2, 2, 3]
    25 duplicates found! - prime factors: [5, 5]
    27 duplicates found! - prime factors: [3, 3, 3]
    28 duplicates found! - prime factors: [2, 2, 7]
    32 duplicates found! - prime factors: [2, 2, 2, 2, 2]
    36 duplicates found! - prime factors: [2, 2, 3, 3]
    40 duplicates found! - prime factors: [2, 2, 2, 5]
    44 duplicates found! - prime factors: [2, 2, 11]
    45 duplicates found! - prime factors: [3, 3, 5]
    48 duplicates found! - prime factors: [2, 2, 2, 2, 3]
    49 duplicates found! - prime factors: [7, 7]
    50 duplicates found! - prime factors: [2, 5, 5]
    52 duplicates found! - prime factors: [2, 2, 13]
    54 duplicates found! - prime factors: [2, 3, 3, 3]
    56 duplicates found! - prime factors: [2, 2, 2, 7]
    60 duplicates found! - prime factors: [2, 2, 3, 5]
    63 duplicates found! - prime factors: [3, 3, 7]
    64 duplicates found! - prime factors: [2, 2, 2, 2, 2, 2]
    68 duplicates found! - prime factors: [2, 2, 17]
    72 duplicates found! - prime factors: [2, 2, 2, 3, 3]
    75 duplicates found! - prime factors: [3, 5, 5]
    76 duplicates found! - prime factors: [2, 2, 19]
    80 duplicates found! - prime factors: [2, 2, 2, 2, 5]
    81 duplicates found! - prime factors: [3, 3, 3, 3]
    84 duplicates found! - prime factors: [2, 2, 3, 7]
    88 duplicates found! - prime factors: [2, 2, 2, 11]
    90 duplicates found! - prime factors: [2, 3, 3, 5]
    92 duplicates found! - prime factors: [2, 2, 23]
    96 duplicates found! - prime factors: [2, 2, 2, 2, 2, 3]
    98 duplicates found! - prime factors: [2, 7, 7]
    99 duplicates found! - prime factors: [3, 3, 11]


The full representation when max_modulus is 4 is the following:
    0: (0, 0),
    1: (1, 1),
    2: (0, 0),
    3: (1, 1)
It is clear that the tuple representation is not enough to disambuigate which number it is representing.
(1, 1) could represent both 1 and 3 for instance.

So when choosing max_modulus a tip is to look at tables of non-square semiprimes for example as they are good candidates.
See this [oeis AOO6881 link](https://oeis.org/A006881/b006881.txt) for a list of all such numbers between 1 and 10 000.
