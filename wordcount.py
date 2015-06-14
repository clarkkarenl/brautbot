#!/usr/bin/python

from __future__ import print_function

from collections import Counter
from operator import itemgetter
import os


_path = os.path.abspath(os.path.dirname(__file__))
SOURCE = os.path.join(_path, 'poems_for_wordcount.txt')
DESTINATION = os.path.join(_path, 'poem_words_out.txt')


def main():
    with open(SOURCE, 'rb') as source, open(DESTINATION, 'wb') as destination:
        word_counts = Counter(source.read().lower().split())
        sorted_count_list = sorted(
            word_counts.items(), key=itemgetter(1), reverse=True
        )
        for item in sorted_count_list:
            print("{} {}".format(*item), file=destination)


def test_output():
    main()
    output = open(DESTINATION, 'rb').readlines()
    word, count = output[0].split()
    assert len(output) == 3518
    assert word == 'the'
    assert int(count) == 1085


if __name__ == '__main__':
    main()
