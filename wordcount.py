#!/usr/bin/python

# open the source file containing all poems
with open('C:\Users\karen\poems_for_wordcount.txt', 'r+') as sourcefile:
    wordcount = {}
    # count occurrence of each word, lowercase to avoid Hello and hello being distinct
    for word in sourcefile.read().lower().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

# open the outfile where the lines will be written
with open('C:\Users\karen\poem_words_out.txt', 'w+') as outfile:
    # write each line to the outfile
    for k, v in wordcount.items():
        outfile.write(str(k) + " " + str(v) + "\n")

# close the files
sourcefile.close()
outfile.close()
