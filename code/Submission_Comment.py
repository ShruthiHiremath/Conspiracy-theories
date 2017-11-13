import csv
from collections import defaultdict
#obtaining the id's from the submissions
columns = defaultdict(list) # each value in each column is appended to a list
with open('Subs.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k
#obtaining the unique id's from the submissions
unique_id = set(columns['id'])
#print unique_id

#obtaining the parent id's from the comments
columns_comments = defaultdict(list) # each value in each column is appended to a list
with open('Comments.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value
            columns_comments[k].append(v) # append the value into the appropriate list
                                 # based on column name k

#columns_comments['parent_id'] : this is all the parent id's from the comments
parent_id = columns_comments['parent_id'];
comments = columns_comments['body'];
dictionary = dict(zip(parent_id, comments))
#print dictionary ; this dictionary contains the parent_id as the key and the body of the comment as the vlaue
comm_sub = {}
#for every unique key in submissions trying to find the comments corresponding to the key
for val in unique_id:
    for par_val in dictionary.keys():
        if (val == par_val):
            comm_sub[val] = dictionary[par_val]
print comm_sub
