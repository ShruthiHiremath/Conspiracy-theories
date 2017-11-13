import pandas as pd
df_sub = pd.read_csv('D:\Fall Semester 2016\Special Problem\conspiracy_submissions.csv')
time_dict_sub = dict(zip(df_sub['id'], df_sub['created_utc']))

df_comments = pd.read_csv('D:\Fall Semester 2016\Special Problem\conspiracy_comments.csv')
time_dict_comment = dict(zip(df_comments['parent_id'], df_comments['created_utc']))

df_result = pd.DataFrame()
max = 0
for k1,v1 in time_dict_sub.iteritems():
    max = v1
    for k2,v2 in time_dict_comment.iteritems():
        if (k1==k2):
            if(max < v2):
                max=v2

                df_result = df_result.append({'Parent_id':k1,'Start_time':v1,'End_time':max}, ignore_index=True)
                print df_result


print df_result




