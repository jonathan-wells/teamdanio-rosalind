#!/usr/bin/env python3

from collections import defaultdict

def frequency_count(s):
    """Counts case-insensitive frequency of words in a string, s"""
    freq_dict = {}  # This is an empty dictionary
    split_string = s.split()
    for word in split_string:
        # .lower() and .split() are examples of string methods. A method is a 
        # function that "belongs to" an object; in this case the "object" is a
        # string.
        word = word.lower()
        if word not in freq_dict:  # First check is word already in dict
            freq_dict[word] = 1
        else:
            freq_dict[word] += 1  # If so, just add 1 to the existing count
    return freq_dict

def frequency_count_2(s):
    """Same as above, but using 'defaultdict' from collections module."""
    freq_dict = defaultdict(int)
    split_string = s.split()
    for word in split_string:
        freq_dict[word] += 1
    return freq_dict

def pretty_print(any_dict):
    for key in any_dict:
        print(key, any_dict[key])

    
diff_freq_dict = frequency_count_2('We tried list and we tried dicts also we tried Zen')
pretty_print(diff_freq_dict)
