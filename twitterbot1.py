import tweepy
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("fGH75nbfiBE0z1Cww8v9BVkkp",
    "AUOAueCiABg0RyD1m0qR4EX42RlJzEI5vcwvamhZKF8V4CXBJn")
auth.set_access_token("1593837249744932864-NT7BW8HfXtPTthN0YJ4NIg2PX63Lzg",
    "KkA3WUyNSnagmSnDfmR3cyu1hhxZkQ301Iodx5a5glDrF")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Get the user's timeline
timeline = api.user_timeline(screen_name='CandideThovex', count=1)

# Get the most recent tweet
tweet = timeline[0]

# Get the list of users who have liked the tweet
likes = api.favorites(id=tweet.id)

# Extract the screen names of the users who have liked the tweet
liked_by = [like.user.screen_name for like in likes]
