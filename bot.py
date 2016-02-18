#First attempt at a python script, followed tutorial at https://praw.readthedocs.org/en/stable/pages/writing_a_bot.html
#Written by Kevin Koscica
#this is a work in progress
import time
import praw

user_agent="user"

r=praw.Reddit(user_agent=user_agent)

r.login()
already_Recieved= []
sub=r.get_subreddit('subreddit')

for submission in sub.get_hot(limit=5):
    text=submission.selftext.lower()
    msg='[new submission](%s)' % submission.short_link
r.send_message('user', 'test', msg)
already_Recieved.append(submission.id)
print("message sent")
   


