#!/usr/bin/python

with open('C:\Users\karen\poems_for_wordcount.txt', 'r+') as sourcefile:
    wordcount = {}
    for word in sourcefile.read().lower().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

with open('C:\Users\karen\poem_words_out.txt', 'w+') as outfile:
   for k, v in wordcount.items():
       # how do I make v a str?
        outfile.write([k] + v)

sourcefile.close()
outfile.close()
