import csv
from collections import defaultdict
import copy
id_subs = [];
id_comments = [];
thread_struct = {};
columns = defaultdict(list)
columns1 = defaultdict(list)# each value in each column is appended to a list
with open('D:\Fall Semester 2016\Special Problem\conspiracy_submissions.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value
            columns1[k].append(v)
#obtaining the submission id's
id_subs = copy.copy(columns1['id'])
#print len(id_subs)
#obtaining the unique id's
#id_subs = set(id_subs)
#print len(id_subs)
with open('D:\Fall Semester 2016\Special Problem\conspiracy_comments.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value
            columns[k].append(v)
id_comments = copy.copy(columns['parent_id'])
#analysing the thread structure
count = 0;
for i in range(0,len(id_subs)):
    for j in range(0,len(id_comments)):
             if (id_subs[i] in id_comments[j]):
                count = count +1;
    thread_struct[id_subs[i]] = count;
    count =0;

