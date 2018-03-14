#!/usr/bin/python3

# importing classes and libraries
import sys
import string
import operator
import math
from collections import defaultdict

# assigning the argument to a variable
file = sys.argv[1]

# printing the arguments and no.of arguments
print('\nno. of arguments =  ' + str(len(sys.argv)))
print("arguments are:  ['" + sys.argv[0] + "', '" +
      file.split('/')[-1] + "']\n")


def printTable(x_label, y_label, value):    # Function to print 5 Column wise
    no_of_rows = math.ceil(len(value)/5.0)
    i = 0
    print((x_label + ' ' + y_label + '   ')*5)
    while(i < no_of_rows):
        for j in range(0, len(value), no_of_rows):
            if i+j < len(value):
                print(str(value[i+j][0]).rjust(3),
                      str(value[i+j][1]).rjust(5), end="   ")
        print("")
        i += 1

with open(file, 'r', encoding='ISO-8859-1') as f:      # File processing
    alph_freq = defaultdict(int)    # declaring defaultdictonaries
    len_freq = defaultdict(int)
    record_count = 0
    character_count = 0
    character_read = 0
    dash_line = 0
    invalid_char = []
    print('words of length 16, 19, or 20:')
    for line in f:      # processing through each line
        record_count += 1
        character_count += len(line)
        if line.find('--') != -1:
            dash_line += 1
        line = line.replace('--', '  ')
        L = ["'", "-", " "]
        letters = list(string.ascii_letters)
        for letter in line:  # finding and replacing unwanted characters
            if letter in letters:
                letter = letter
            else:
                if letter in L:
                    letter = letter
                else:
                    if letter not in invalid_char:
                        invalid_char.append(letter)
                    line = line.replace(letter, ' ')

        line = line.lower()  # converting line to lower case

        words = line.split()   # splitting the line into words
        len_word = [len(word) for word in words]
        w_length = [16, 19, 20]
        for word in words:
            if(len(word) in w_length):
                print('***  ' + word)

            for letter in word:  # creating a letter frequency dictonary
                keys = alph_freq.keys()
                if letter in keys:
                    alph_freq[letter] += 1
                else:
                    alph_freq[letter] = 1

        for count in len_word:  # creating a word length frequency dictonary
            keys = len_freq.keys()
            if count in keys:
                len_freq[count] += 1
            else:
                len_freq[count] = 1

    alph_freq.pop('-')   # taking off unwanted keys from dictonaries
    alph_freq.pop("'")

    # sorting the alphabet dictonary by key
    key_sort = sorted(alph_freq.items(), key=operator.itemgetter(0))
    printTable('', '', key_sort)  # calling columnwise print fucntion
    for k, v in key_sort:
        character_read += v

    # sorting the alphabet dictonary by value
    value_sort = sorted(alph_freq.items(), key=operator.itemgetter(1),
                        reverse=True)
    printTable('', '', value_sort)   # calling columnwise print fucntion

    # sorting the word length dictonary by key
    key_len_sort = sorted(len_freq.items(), key=operator.itemgetter(0))
    print('\n')
    printTable('len', 'count', key_len_sort)  # calling print fucntion

    # sorting the word length dictonary by value
    key_cnt_sort = sorted(len_freq.items(), key=operator.itemgetter(1),
                          reverse=True)
    i = 0
    total_word_count = 0
    print('\n')
    print('rank length   freq  len*fre rank*fre lgf/lgr')
    # printing the table row wise
    for k, v in sorted(len_freq.items(), key=lambda x: (x[1], x[0]),
                       reverse=True):
        i += 1
        total_word_count += v
        if i == 1:
            print(str(i).rjust(4), str(k).rjust(6), str(v).rjust(6),
                  str(k*v).rjust(8), str(i*v).rjust(8), ' ')
        else:
            print(str(i).rjust(4), str(k).rjust(6), str(v).rjust(6),
                  str(k*v).rjust(8), str(i*v).rjust(8),
                  str("%.2f" % (math.log2(v)/math.log2(i))).rjust(7))

    print('\nTotal\t     ' + str(total_word_count))  # printing attributes
    print('\nRecords read:           ' + str(record_count).rjust(6))
    print('Characters read:        ' + str(character_count).rjust(6))
    print('Characters counted:     ' + str(character_read).rjust(6))
    print('Words counted:          ' + str(total_word_count).rjust(6))
    print('Distinct characters:    ' + str(len(alph_freq)).rjust(6))

    print('\nLines with --           ' + str(dash_line).rjust(6))
    print('Invalid chars:        ' + str(sorted(invalid_char)) + '\n')
