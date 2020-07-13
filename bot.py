import tweepy
import time

auth = tweepy.OAuthHandler('rX6wNCPNawKFSej2hnftk8Qqi', '1HCpbylkKydS7blkg3ZJ9mKzQB6Qkcp5WMuU7od6IdJhBAwyCP')
auth.set_access_token('902519548896620544-1RbuDD3FW68XtLzjiFcVo24ZmUMkuGe',
                      'XcnMZqlvnhW0h5X4B0O74KY4FdD0Qr8HnxiEfWP4oMuVf')

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

