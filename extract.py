import tweepy
import json
import config

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

count = 0
search_keyword = 'gstsimplified -filter:retweets'

with open('gst.json', 'w+') as file:
    file.write('\n')
    print(file.tell())
    try:
        for tweet in tweepy.Cursor(api.search, q=search_keyword, tweet_mode='extended', lang="en",
                                   result_type="mixed").items():
            if file.tell() != 1:  # check if current file position is nonzero
                file.write(',')  # seperate ',' tweets excluding first instance
            json.dump(tweet._json, file, indent=4)
            count += 1
            print("tweet #" + str(count) + " extracted")
        file.write('\n]')
        file.seek(0, 0)
        file.write('[')
    except tweepy.TweepError:
        print("Rate limit reached")
print("extracted tweets")
