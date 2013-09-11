# Cassie Sancartier

# 13.1

# import string

# def process_file(filename):
#     hist = dict()
#     fp = open(filename)
#     for line in fp:
#         process_line(line, hist)
#     return hist

# def process_line(line, hist):
#     line = line.replace('-', ' ')

#     for word in line.split():  # keeping this in for now, but may remove later?
#         word = word.strip(string.whitespace + string.punctuation)
#         word = word.lower()

#         hist[word] = hist.get(word, 0) + 1

# hist = process_file('emma.txt')   

# print hist



# 13.8 - Markov Analysis

# Was working on the above, then took a look at the example code:


import sys
import string
import random

suffix_map = {}        # map from prefixes to a list of suffixes
prefix = ()            # current tuple of words


def process_file(filename, order=2):
    fp = open(filename)
    skip_gutenberg_header(fp)

    for line in fp:
        for word in line.rstrip().split():
            process_word(word, order)


def skip_gutenberg_header(fp):
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_word(word, order=2):
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return
    try:
        suffix_map[prefix].append(word)
    except KeyError:
        suffix_map[prefix] = [word]

    prefix = shift(prefix, word)


def random_text(n=100):
    start = random.choice(suffix_map.keys())
    
    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            random_text(n-i)
            return

        word = random.choice(suffixes)
        print word,
        start = shift(start, word)


def shift(t, word):
    return t[1:] + (word,)


def main(name, filename='emma.txt', n=100, order=2, *args):
    try:
        n = int(n)
        order = int(order)
    except:
        print 'Usage: randomtext.py filename [# of words] [prefix length]'
    else: 
        process_file(filename, order)
        random_text(n)


if __name__ == '__main__':
    main(*sys.argv)






