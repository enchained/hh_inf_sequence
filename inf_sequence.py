import sys


def get_pos(a):
    """
    a: user input string to look for, numbers only.
    ---
    This function generates a sequence of positive integers as a string.
    ---
    returns: first ocurrence of 'a' in the sequence (int pos, starting from 1)
    """
    found = False
    n = 1  # sequence start
    seq = ""

    while not found:
        seq += str(n)
        if a in seq:
            found = True
            return seq.index(a) + 1
        n += 1


def main(a):
    if a.isdigit():
        # search sequence A position in the infinite sequence S
        pos = get_pos(a)
        print "Input " + a + " positioned at " + str(pos)
    else:
        print "Invalid input. Please enter a numeric sequence A as an argument"


if __name__ == '__main__':
    # read sequence A
    if len(sys.argv) > 1:
        main(str(sys.argv[1]))
    else:
        print "Error: no sequence entered."
        print "Please enter a numeric sequence A as an argument"
