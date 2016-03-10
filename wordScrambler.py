# wordScrambler.py scrambles individual words in words.txt. Keeps periods at
# the ends of words.

from random import shuffle

f = open('words.txt', 'r')

l = f.read().split(' ')

for x in range (0,len(l)):
    word1 = l[x]
    word = list(word1)
    shuffle(word)
    l[x] = ''.join(word)

for x in range (0,len(l)):
    if '.' in l[x]:
        l[x] = l[x].replace('.','')
        l[x] += '.'

print ' '.join(l)
