#!/usr/bin/python

from operator import itemgetter
import os
import pytest


_path = os.path.abspath(os.path.dirname(__file__))
SOURCE = os.path.join(_path, 'poems_for_wordcount.txt')
DESTINATION = os.path.join(_path, 'poem_words_out.txt')


def count_words(word_list):
    word_count = {}
    for word in word_list:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count


def sort_word_count(word_dict):
    # first sort to get k by alpha
    y = sorted(word_dict.items(), key=itemgetter(0))
    # then reverse sort on number of occurrences (v) to get list in desc order
    return sorted(y, key=itemgetter(1), reverse=1)


def main():
    # open the source file containing all poems
    # with open() closes after, no need to do that separately
    with open(SOURCE, 'r+') as sourcefile:
        # count occurrence of each word, lowercase to avoid Hello and hello
        # being distinct
        word_count = count_words(sourcefile.read().lower().split())

    x = sort_word_count(word_count)

    # open the outfile where the lines will be written
    with open(DESTINATION, 'w+') as outfile:
        # write each line to the outfile
        for k, v in x:
            outfile.write(str(k) + " " + str(v) + "\n")


@pytest.fixture
def word_list():
    return 'you watch the brown fox jumped over the fence'.split()


def test_count_words(word_list):
    assert count_words(word_list)['the'] == 2


def test_sort_word_count(word_list):
    word_count = count_words(word_list)
    assert sort_word_count(word_count)[0][0] == 'the'


def test_output():
    main()
    output = open(DESTINATION, 'rb').readlines()
    word, count = output[0].split()
    assert len(output) == 3518
    assert word == 'the'
    assert int(count) == 1085


if __name__ == '__main__':
    main()
