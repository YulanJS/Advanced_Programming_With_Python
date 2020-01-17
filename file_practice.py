'''
import string
with open('yesterday.txt', 'r', encoding='UTF-8') as input_file:
    for each_line in input_file:
        for each_word in each_line.split():
            each_word = each_word.strip(string.punctuation)
'''

