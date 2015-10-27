import sys


def kmp_get_pos(pattern):
    """
    Generate a sequence of positive integers,
    and use Knuth-Morris-Pratt algorithm
    to find first substring position in this sequence,
    based on calculated shifts.
    From:
    http://code.activestate.com/recipes/117214-knuth-morris-pratt-string-matching/
    Python Cookbook (O'Reilly), recipe 5.13. Finding Subsequences

    Args:
        pattern (str): target substring A.
    Returns:
        start_pos+1 (int): first ocurrence of pattern A
        in integer_char_sequence S, starting from 1.
    """
    shift = compute_shifts(pattern)
    start_pos = 0
    match_len = 0
    pattern_len = len(pattern)
    for c in integer_char_sequence():
        while match_len >= 0 and pattern[match_len] != c:
            start_pos += shift[match_len]
            match_len -= shift[match_len]
        match_len += 1
        if match_len == pattern_len:
            return start_pos + 1


def integer_char_sequence():
    """
    Iterate through characters of sequental integers.
    Generate infinite sequence S.

    for n in integer_char_sequence()
    >>> 1 2 3 4 5 6 7 8 9 1 0 1 1 1 2 1 3 1 4 1 5 ...

    Returns (yelds):
        char (str): numerical character
    """
    integer = 1
    while True:
        str_int = str(integer)
        for char in str_int:
            yield char
        integer += 1


def compute_shifts(pattern):
    """
    Generate shift list for provided substring pattern.
    Part of Knuth-Morris-Pratt algorithm.
    KMP algorithm makes character shift desicions based on this list.

    Args:
        pattern (str): substring A.
    Returns:
        shifts (list): list of integer shift data.
    """
    shifts = [None] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern) + 1):
        while shift < pos and pattern[pos-1] != pattern[pos-shift-1]:
            shift += shifts[pos-shift-1]
        shifts[pos] = shift
    return shifts


def main(pattern):
    if pattern.isdigit():
        # Search for sequence A position in the infinite sequence S
        pos = kmp_get_pos(pattern)
        print "Input " + pattern + " positioned at " + str(pos)
    else:
        print "Invalid input. Please enter a numeric sequence A as an argument"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Read sequence A
        main(str(sys.argv[1]))
    else:
        print "Error: no sequence entered."
        print "Please enter a numeric sequence A as an argument"
