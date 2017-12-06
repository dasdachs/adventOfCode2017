#! /usr/bin/env python3
from collections import Counter

# Copy the input from you https://adventofcode.com/2017/day/4/input
# we will assume that the input is saved as input
puzzle = [pass_phrase.split() for pass_phrase in input.splitlines()]

# We will use a really short filter function
# The idea is that if the len of the Counter
# is equal to the len of the list
# than all the values are unique
res = list(filter(lambda x: len(Counter(x).values()) == len(x), puzzle)

# The result is the length of the res list
# a list conataining only correct pass phrases
len(res)
