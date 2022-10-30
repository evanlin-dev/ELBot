import praw
import os
from dotenv import load_dotenv

load_dotenv()
clientId = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
userAgent = {"User-Agent": "ELBot"}
reddit = praw.Reddit(
    client_id=clientId, 
    client_secret=clientSecret, 
    user_agent=userAgent, 
    username=username, 
    password=password)

reddit.read_only = True

subreddit = reddit.subreddit("Hololive")
 
# display the subreddit name
print(subreddit.display_name)
 
# display the subreddit title
print(subreddit.title)      
 
# display the subreddit description
print(subreddit.description)

# let the redditor be "AutoModerator"
redditor = reddit.redditor('AutoModerator')
 
# display AutoModerator's karma
print(redditor.link_karma)