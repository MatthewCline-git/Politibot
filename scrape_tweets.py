import tweepy
import time
import re
import gpt_2_simple as gpt2
import tensorflow as tf

CONSUMER_KEY = "XXXXX"
CONSUMER_SECRET = "XXXXX"

ACCESS_TOKEN = "XXXXX"
ACCESS_SECRET = "XXXXX"

def getAPI():
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)

    try: 

        data_list = []
        
        statuses = tweepy.Cursor(api.user_timeline, screen_name="mattyglesias", count=200, tweet_mode="extended").items()
        
        for status in statuses:
            id = status.id
            new_tweet = re.sub(r'https:\S+', '', status.full_text)
            data_list.append(new_tweet)

        statuses = tweepy.Cursor(api.user_timeline, screen_name="mattyglesias", count=200, max_id=id, tweet_mode="extended").items()

        for status in statuses:
            id = status.id
            new_tweet = re.sub(r'https:\S+', '', status.full_text)
            data_list.append(new_tweet)

        statuses = tweepy.Cursor(api.user_timeline, screen_name="mattyglesias", count=200, max_id=id, tweet_mode="extended").items()

        for status in statuses:
            id = status.id
            new_tweet = re.sub(r'https:\S+', '', status.full_text)
            data_list.append(new_tweet)

        statuses = tweepy.Cursor(api.user_timeline, screen_name="mattyglesias", count=200, max_id=id, tweet_mode="extended").items()

        for status in statuses:
            id = status.id
            new_tweet = re.sub(r'https:\S+', '', status.full_text)
            data_list.append(new_tweet)

        statuses = tweepy.Cursor(api.user_timeline, screen_name="mattyglesias", count=200, max_id=id, tweet_mode="extended").items()

        for status in statuses:
            id = status.id
            new_tweet = re.sub(r'https:\S+', '', status.full_text)
            data_list.append(new_tweet)

        textfile = open("file.txt", "w")
        for element in data_list:
            textfile.write(element + "\n")
        textfile.close()

    except BaseException as e:
        print('failed on_status,', str(e))

        time.sleep(3)

if __name__ == '__main__':
    getAPI()
