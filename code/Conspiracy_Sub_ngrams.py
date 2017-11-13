import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
import csv
from collections import defaultdict
#Submissions
columns = defaultdict(list) # each value in each column is appended to a list
unigrams_subs = defaultdict(list)
bigrams_subs = defaultdict(list)
columns_comments = defaultdict(list) # each value in each column is appended to a list
unigrams_comments = {}
bigrams_comments = {}
with open('conspiracy_submissions.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k

for val in columns['title']:
    token = nltk.word_tokenize(val)
    unigrams_subs[val].append(Counter(ngrams(token,1)))

for val in columns['title']:
    token = nltk.word_tokenize(val)
    bigrams_subs[val].append(Counter(ngrams(token, 2)))
print unigrams_subs
print bigrams_subs

# #Comments#
with open('conspiracy_comments.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value
            columns_comments[k].append(v) # append the value into the appropriate list
                                 # based on column name k
#
for val in columns_comments['body']:
    token = nltk.word_tokenize(val)
    unigrams_comments[val].append(Counter(ngrams(token,1)))
for val in columns_comments['body']:
    token = nltk.word_tokenize(val)
    bigrams_comments[val].append(Counter(ngrams(token, 2)))