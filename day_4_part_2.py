#! /usr/bin/env python3
from collections import Counter

# Copy the input from you https://adventofcode.com/2017/day/4/input
# we will assume that the input is saved as input
puzzle = [pass_phrase.split() for pass_phrase in input.splitlines()]

def anagram_in_list(array):
     """Checks if a anagram of a word is in a list.
     
     The solution is a bit brute force. A better way would be
     to split the list into sublists according to the length of
     the words. Then check only the sublist that have more then
     one element.
     
     Parameters
     ----------
     array: list
         Array is a list of strings. No check is in place to verify that.
     
     Returns
     -------
     bool
         True if there is an anagram, false if there is not.
     """
     
     
     while array:
         if len(array) < 2:
             break
         val = array.pop(0)
         check = list(filter(
           lambda x: len(x) == len(val) and Counter(x).items() == Counter(val).items(), 
           array)
         )
         if check:
             return True
     return False
     
# Solution
len(list(filter(lambda x: anagram_in_list(x), puzzle)))
