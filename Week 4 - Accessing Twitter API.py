## Access Twitter API in Python -
# Step 1 - importing the libraries
import os
import tweepy as tw
import pandas as pd
import json

# Step 2 - defining your keys
consumer_key = 'ZgUcrsAS6ioexAygXcdGsNr9A'
consumer_secret = 'SCQXe01Sp4NABDkcctILmLvoFTT0hgkRsEdjO96PgEOnWt6MzK'
access_token = '1339180888580567043-yiP8uqFcliJCZhSwA9ML3XaSQQdPGJ'
access_token_secret = 'yKyr7xTC6x8d2dcEG2MjD9p3dQWXrpRJDRN63Q0Axbdzo'

# Step 3 - pass the access credentials
auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tw.API(auth,wait_on_rate_limit=True)

# Step 4 - search Twitter for Tweets
# Example 1 - collect tweets with search term #wildfires
# define the search term and the date_since date as variables
search_words = "#wildfires"
date_since = "2018-11-16"

# Step 5 - use .Cursor() to search twitter for tweets containing the search term
tweets = tw.Cursor(api.search,q=search_words,lang='en',since=date_since).items(5) # return 5 of the most recent tweets
tweets

# Step 6 - code below loops through the object and prints the text associated with each tweet
# iterate & print the tweets (using for loop)
for tweet in tweets:
    print(tweet.text)

# Example 2 - collect tweets with search term #Trump
search_words2 = "#Trump"
date_since2 = "2020-11-01"
tweets2 = tw.Cursor(api.search,q=search_words2,lang='en',since=date_since2).items(5) # return 5 of the most recent tweets
tweets2
for tweet in tweets2:
    print(tweet.text)


# Step 7 - keep or Remove Retweets
new_search = search_words + '-filter:retweets'
new_search

tweets = tw.Cursor(api.search,q=search_words,lang='en',since=date_since).items(5) # return 5 of the most recent tweets
tweets
for tweet in tweets:
    print(tweet.text)

# Step 8 - who is Tweeting Data?
tweets = tw.Cursor(api.search,q=new_search,lang='en',since=date_since).items(5) # return 5 of the most recent tweets
user_locs = [[tweet.user.screen_name,tweet.user.location] for tweet in tweets]
print(user_locs)

# Step 9 - create a Pandas Dataframe From A List of Tweet Data
tweet_text = pd.DataFrame(data=user_locs,columns=['user',"location"])
print(tweet_text)

# Step 10 - customizing Twitter Queries
# search climate change rekated tweets by removing any retweets
new_search = "climate+change -filter:retweets"
tweets = tw.Cursor(api.search,q=new_search,lang='en',since=date_since).items(1000)
all_tweets = [tweet.text for tweet in tweets]
print(all_tweets[:5])


# Step 11 - scraping a specific Twitter user’s Tweets:
# Scrape 10 of Twitter CEOs most recent tweets (@jack username)
username = 'jack'
count = 10
# query specific-user's tweets  iterate over them
try:
    tweets = tw.Cursor(api.user_timeline,id=username).items(count)
    tweets_list = [[tweet.created_at,tweet.id,tweet.text] for tweet in tweets]
# create a dataframe from tweet list
    tweets_df = pd.DataFrame(tweets_list)
except BaseException as e:
    print('failed on_status,',str(e))
    time.sleep(3)
# print the tweet dataframe
print(tweets_df)

# Step 12 - scraping tweets from a text search query:
# Scrape the 10 most recent tweets that were relevant to the 2020 US Election
text_query = '2020 US Election'
count = 10
# query specific-user's tweets  iterate over them
try:
    tweets = tw.Cursor(api.search,q=text_query).items(count)
    tweets_list = [[tweet.created_at,tweet.id,tweet.text]for tweet in tweets]
# create a dataframe from tweet list
    tweets_df = pd.DataFrame(tweets_list)
except BaseException as e:
    print('failed on_status,',str(e))
    time.sleep(3)
# print the tweet dataframe
print(tweets_df)

