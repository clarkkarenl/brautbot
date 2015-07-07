#!/usr/bin/env python

from __future__ import print_function

from collections import Counter
from operator import itemgetter
import os


_path = os.path.abspath(os.path.dirname(__file__))
SOURCE = os.path.join(_path, 'poems_for_wordcount.txt')
DESTINATION = os.path.join(_path, 'poem_words_out.txt')


def sort_word_counts(word_dict):
    # first sort to get k by alpha
    sorted_by_key = sorted(word_dict.items(), key=itemgetter(0))
    # then reverse sort on number of occurrences (v) to get list in desc order
    return sorted(sorted_by_key, key=itemgetter(1), reverse=1)


def main():
    with open(SOURCE, 'rb') as source, open(DESTINATION, 'wb') as destination:
        word_counts = Counter(source.read().lower().split())
        for item in sort_word_counts(word_counts):
            print("{} {}".format(*item), file=destination)


def test_sort_word_counts():
    word_list = 'you watch the brown fox jumped over the fence'.split()
    word_counts = Counter(word_list)
    sorted_list = sort_word_counts(word_counts)
    assert sorted_list[0][0] == 'the'
    assert sorted_list[1][0] == 'brown'
    assert sorted_list[-1][0] == 'you'


def test_output():
    main()
    output = open(DESTINATION, 'rb').readlines()
    word, count = output[0].split()
    assert len(output) == 3518
    assert word == 'the'
    assert int(count) == 1085


if __name__ == '__main__':
    main()
