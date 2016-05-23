'''
Frequency Dictionary
'''

from collections import Counter, OrderedDict

def freq_distribution(infile, distfile):
    file = open("poem.txt", 'r')
    FD = Counter()
    for line in file:
        line = line.rstrip('\n')
        for word in line.split(' '):
            FD[word] += 1
    file.close()
    file = open("distfile.txt", 'w')
    a = OrderedDict(sorted(FD.items(), key = lambda t: t[0]))
    for (keys, values) in a.items():
        [file.write('{0},{1}\n'.format(keys, values))]
        
    
def ordered_freq_distribution(infile, ordered_distfile):
    
    file = open("poem.txt", 'r')
    FD = Counter()
    for line in file:
        line = line.rstrip('\n')
        for word in line.split(' '):
            FD[word] += 1
    file.close()
    file = open("distfile.txt", 'w')
    a = OrderedDict(sorted(FD.items(), key = lambda t: t[1], reverse=True))
    for (keys, values) in a.items():
        [file.write('{0},{1}\n'.format(keys, values))]

def freq_dictionary(infile):
    file = open("poem.txt", 'r')
    FD = Counter()
    for line in file:
        line = line.rstrip('\n')
        for word in line.split(' '):
            FD[word] += 1
    return FD
   
