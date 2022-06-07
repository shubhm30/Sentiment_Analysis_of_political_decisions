import json
import csv
import sys

f1 = sys.argv[1]
f2 = sys.argv[2]
with open(f1, 'r') as in_file, \
        open(f2, 'w') as out_file:
    fields = 'tweet_id, tweet_time, tweet_text, tweet_User_name, tweet_User_id, User_id_created_at, User_followers, User_friends, tweet_language, Retweet_count, favorite_count, hashtags'
    out_file.write(fields)
    out_file.write('\n')
    csv_writer = csv.writer(out_file)
    tweet_count = 0
    inf = json.load(in_file)
    for line in inf:
        # Pull out various data from the tweets
        row = (
            inf[tweet_count]["id"],  # tweet_id
            inf[tweet_count]["created_at"],  # tweet_time
            inf[tweet_count]["full_text"],  # tweet_text
            inf[tweet_count]["user"]["screen_name"],  # tweet_author
            inf[tweet_count]["user"]["id_str"],  # tweet_author_id
            inf[tweet_count]["user"]["created_at"],  # tweet_author_id
            inf[tweet_count]["user"]["followers_count"],  # tweet_author_id
            inf[tweet_count]["user"]["friends_count"],  # tweet_author_id
            inf[tweet_count]["lang"],  # tweet_language
            inf[tweet_count]["retweet_count"],  # tweet_rt_count
            inf[tweet_count]["favorite_count"],  # tweet_fav_count
            [hashtag["text"] for hashtag in inf[tweet_count]["entities"]["hashtags"]]
        )
        tweet_count += 1
        csv_writer.writerow(row)

# print the name of the file and number of tweets imported
# print("File Imported:", str(sys.argv[1]))
print("# Tweets Imported:", tweet_count)
# print("File Exported:", str(sys.argv[2]))
