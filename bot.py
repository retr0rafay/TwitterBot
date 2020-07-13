import tweepy
import time

auth = tweepy.OAuthHandler('', '')
auth.set_access_token('',
                      '')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


search_string = 'retr0rafay'
numberOfTweets = 5

# Generous Bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == "Engineering Bytes":
        follower.unfollow()
        print('all done!')
        break

# Narcissistic Bot
for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print(f'I liked that tweet: {tweet.text}')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

