# Social-Computing-Project<br/>
<b>Progress Steps :</b><br/>
1. Used  - https://pushshift.io/ to get the data from the google bigquery<br/>
2. Since the number of instances returned is large hence it cannot be directly stored as a CSV file. So this had to be first stored in the cloud storage by creating a bucket and a project within the bucket. The files were then 'exported' to this folder in the bucket. They were then downloaded from there in the csv format<br/>
3. I have uploaded the scripts and the data collected so far to the servers I was provided access to - flashmob00.cc.gatech.edu, flashmob01.cc.gatech.edu, flashmob02.cc.gatech.edu, flashmob03.cc.gatech.edu. Since I use a Windows machine, I used WinSCP to transfer the files from my local machine to the servers. Hence forth i will be transferring everything to flashmob00.cc.gatech.edu.<br/>
4. I have computed the unigrams and the bigrams of the title and body fields from the submissions and comments respectively.<br/>
<br/>

<b>Obtaining the data from the subreddit:</b> <br/>
ScriptName:Scripts.txt<br/>
1. The reddit data has been obtaibed from google big query.<br/>
2. The subreddits that were identified to be studied were - r/Conspiracy and r/ConspiracyAMA<br/>
3. Comments and submissions were obtained from the pushshift database and the rt_reddit.commennts and rt_reddit.submissions tables.<br/>
4. Step 3 was followed for both the subreddits under study.<br/>
5. Unique users are identified from among the comments and submissions in the conspiracy subreddit.<br/>
6. Number of posts and comments for each unique usesr are obtained from the conspiracy subreddit.<br/>

Location of data : flashmob00 has this data.<br/>
<br/>

<b>Obtaining the user timelines: </b><br/>
ScriptName:Scripts_UserTimeline<br/>
1. The unique users obtained above are stored as a CSV and as a table in the bigquery.<br/>
2. To do so, I have created my own database called commennst_conspiracy, where I have stored all the tables that I would require.<br/>
3. Select all fields from reddit_comments for all the unique users identified.<br/>
4. Step 3 was repeated for the time period 2009 - August,2016.<br/>
5. Step 3 was repeated for the full corpus as well. <br/>
6. The queries that run were had too many entries to be processed so they were first stored in a table --> Show Options 
-->Select Destination Table -->Check 'Allow Large Results' in the Result Size--> Uncheck Flatten results in Results Schema --> Run Query<br/>
7. Once the table is created --> Export Table --> For the google cloud storage uri give the value -->  reddit-data-conspiracy/?project=reddit-143620/filename-*.csv(it stores it in parts) --> Ok <br/>
8. Once the job is run go to the google cloud storage location and download the CSV files manually to your local machine.<br/>
9. Upload the files to the server.<br/>

Roadblocks faced : Since the whole process described above was manual and there was not automatic way of doing it, it took me a really long time to get all this data (~50 - 60 hours).<br/>

Location of data : flashmob00 has data from 2009-2011 ;flashmob01 has data from 2012-2016 and the full corpus.<br/>

<br/>

<b>Obtaining the ngrams from data, alongwith their frequency :</b><br/>
ScriptName : Conspiracy_Sub_ngrams.py<br/>
1. This script is used to obtain the unigrams and bigrams from the text that is present in the conspiracy subreddits comments and submissions section. <br/>

Location of script : flashmob00 has this script.<br/>
<br/>
<b>Obtaining the comments corresponding to the submissions:</b><br/>
ScriptName : Submission_Comment.py<br/>
1. Obtain the id's from the submissions. This is done so as to get the comments correspomding to these id's. Id's uniquely identify the submissions. <br/>
2. Get a unique set of these id's.<br/>
3. Obtain the parent id's from the comments and for each of the comment.<br/>
4. For every id (unique) in the submissions, obtain the comments corresponding to the keys.<br/>
5. This is represented in the dictionary format, with the key as the unique submission id and the value as the comments.<br/>

Location of script : flashmob00 has this script.<br/>
<br/>
<b>Obtaining unique users from both the submissions and comments:</b><br/>
ScriptName : Unique_Users.py<br/>
1. The requirement and hence the identification of unique users that span across the submissions and comments was identified and this script does that.<br/>
2. It gathers the unique users across and stores it as a list and then as a table.<br/>

Location of script : flashmob00 has this script.<br/>
<br/>

<b>Basic analysis of the thread structure:</b><br/>
ScriptName : Thread_structure.py<br/>
1.The id's for both the submissions and the comments are identified. These id's are used to obtain the unique identifiers.<br/>
2.For each id in the submission, search is made through the parent id's of the comments to observe how many comments are linked to each of these submissions.<br/>
3. The output of the script is the id from the submission and the corresponding number of comments for those submissions.<br/>
4. This gives a naive understanding of whether the subreddit has expanded breadth-wise or depth-wise.<br/>

Location of script : flashmob00 has this script.<br/>
<br/>

<b>Analysis of the thread structure - Lifetime of a thread:</b><br/>
ScriptName : Thread_structure2.py<br/>
1.The id's for both the submissions and the comments are identified. The id and the time in which the submissions and the comments were created are stored as a dictionary.<br/>
2.For each id in the submission, search is made through the parent id's of the comments to observe how many comments are linked to each of these submissions.<br/>
3. The created time of the submission is retained and for this id, the last comment posted is obtained.<br/>
4. This gives the lifetime of a thread.<br/>

Location of script : flashmob01 has this script.<br/>
<br/>
<b>Analysis of the thread structure - Re-entry of participants:</b><br/>
ScriptName : Thread_structure3.py<br/>
1.The id's for both the submissions and the comments are identified. The comment id corresponding to the matched parent id was found. The matches for the parent id were performed from the submission and the comment.<br/>
2.For each matched id in the comments, the corresponding id's of the comments were found. These represented the different users contributing to the same thread<br/>
3. A count of this dtype object was obtained.<br/>
4. A set of these users was created to obtain the unique users contributing to a submission.<br/>
5. The score was computed as : number of users contributing/number of unique users contributing. This was done per submission.<br/>
6. This gives the re-entry score of the participants<br/>

Location of script : flashmob01 has this script.<br/>
<br/>
<b>Miscellaneous activities:</b><br/>
1. Setting up the servers and transferring all the data files and the scripts to the server.<br/>
2. Setting up github and updating with the activited on a periodic basis.<br/>
3. Understanding how to use the google bigquery and the google cloud storage to obtain and store these huge amounts of data.<br/>
<br/>

<b>Related papers read:</b><br/>
1. Mental Health Discourse on reddit: Self-disclosure, Social Support, and Anonymity; AUthors: Munmun De Choudhury, Sushovan De.<br/>
2. Winning Arguments: Interaction Dynamics and Persuasion Strategies in Good-faith Online Discussions; Authors: Chenhao Tan,  Vlad Niculae, Cristian Danescu-Niculescu-Mizil, Lillian Lee.<br/>
3. A Parsimonious Language Model of Social Media Credibility Perceptions Across Multiple Events; Paper under review.<br/>
<br/>

<b>Future Work:</b><br/>
1. This describes the proposal of work that I intend to accomplish to make sense out of the data I have obtained so far.<br/>
2. The points are jotted down in the file Future Work.md
<br/>
# Conspiracy-theories
