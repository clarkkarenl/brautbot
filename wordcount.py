#!/usr/bin/python

from operator import itemgetter
import os


_path = os.path.abspath(os.path.dirname(__file__))
SOURCE = os.path.join(_path, 'poems_for_wordcount.txt')
DESTINATION = os.path.join(_path, 'poem_words_out.txt')


def count_words(word_list):
    wordcount = {}
    for word in word_list:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return wordcount


def main():
    # open the source file containing all poems
    # with open() closes after, no need to do that separately
    with open(SOURCE, 'r+') as sourcefile:
        # count occurrence of each word, lowercase to avoid Hello and hello
        # being distinct
        wordcount = count_words(sourcefile.read().lower().split())

    # first sort to get k by alpha
    y = sorted(wordcount.items(), key=itemgetter(0))
    # then reverse sort on number of occurrences (v) to get list in desc order
    x = sorted(y, key=itemgetter(1), reverse=1)

    # open the outfile where the lines will be written
    with open(DESTINATION, 'w+') as outfile:
        # write each line to the outfile
        for k, v in x:
            outfile.write(str(k) + " " + str(v) + "\n")


def test_count_words():
    word_list = 'the brown fox jumped over the fence'.split()
    assert count_words(word_list)['the'] == 2


def test_output():
    main()
    output = open(DESTINATION, 'rb').readlines()
    word, count = output[0].split()
    assert len(output) == 3518
    assert word == 'the'
    assert int(count) == 1085


if __name__ == '__main__':
    main()
