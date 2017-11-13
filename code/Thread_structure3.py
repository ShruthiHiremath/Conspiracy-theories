import pandas as pd
import math
df_sub = pd.read_csv('D:\Fall Semester 2016\Special Problem\conspiracy_submissions.csv')


df_comments = pd.read_csv('D:\Fall Semester 2016\Special Problem\conspiracy_comments.csv')
df_pid = df_comments['parent_id']
df_id = df_comments['id']
df_comm = pd.concat([df_pid,df_id],axis=1)
index = 0
df_result = pd.DataFrame()
for i in df_sub['id']:
    users_list = [];
    for j in df_comm['parent_id']:
        if (i==j):
            index = df_comm['parent_id'][df_comm['parent_id'] ==j].index.tolist()
    users_list.append(df_comm['id'].ix[index])
    count_users = len(users_list[0])
    unique_users = len(set(users_list[0]))
    #print count_users
    df_result = df_result.append({'Parent_id':i,'Number of users':count_users,'Unique users':unique_users,'Score': math.ceil(count_users/unique_users)}, ignore_index=True)
print df_result


