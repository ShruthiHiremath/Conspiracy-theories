import csv
from collections import defaultdict
import copy
unique_users = [];
columns = defaultdict(list)
columns1 = defaultdict(list)# each value in each column is appended to a list
with open('D:\Fall Semester 2016\Special Problem\NumberUniqueAuthors_Submissions.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value
            columns[k].append(v)
 # each value in each column is appended to a list
unique_users = copy.copy(columns['author'])
print "Number of authors in submission",len(columns['author'])
print "Number of uniue users in submission",len(unique_users)
with open('D:\Fall Semester 2016\Special Problem\NumberUniqueAuthors_Comments.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value
            columns1[k].append(v)
unique_users.extend(columns1['author'])
print "Number of authors in Comments",len(columns1['author'])
print "Number of authors in Submissions and Comments",len(unique_users)
unique_users = set(unique_users)
print "The unique users overall",len(unique_users)