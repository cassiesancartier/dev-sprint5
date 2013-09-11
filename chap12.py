# Cassie Sancartier
# Chapter 12

# 12.4



def signature(string):
    sig_word = list(string)
    sig_word.sort()
    sig_word= ''.join(t)
    return sig_word


def all_anagrams(filename):
    anagram_dict = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        if t not in anagram_dict:
            anagram_dict[t] = [word]
        else:
            anagram_dict[t].append(word)
    return anagram_dict


def print_anagram_sets(dictionary):
    for v in dictionary.values():
        if len(v) > 1:
            print len(v), v       

def print_anagram_sets_in_order(dictionary):
    t = []
    for v in dictionary.values():
        if len(v) > 1:
            t.append((len(v), v))

    t.sort()

    for x in t:
        print x


def filter_length(dictionary, num_letters):
    res = {}
    for word, anagrams in dcitionary.iteritems():
        if len(word) == num_letters:
            res[word] = anagrams
    return res


if __name__ == '__main__':
    dictionary = all_anagrams('words.txt')
    print_anagram_sets_in_order(d)

    eight_letters = filter_length(dictionary, 8)
    print_anagram_sets_in_order(eight_letters)
