import tweepy
import tkinter
import time

#keys
consumer_key = 'Your consumer_key';
consumer_secret = 'Your consumer_secret';
access_token = 'Your access_token';
access_token_secret = 'Your access_token_secret';


auth = tweepy.OAuthHandler(consumer_key, consumer_secret);
auth.set_access_token(access_token, access_token_secret);
api = tweepy.API(auth);

file_name = "last_seen_id.txt"

#just gets the last seen id from the text file
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, "r");
    last_seen_id = int(f_read.read().strip());
    f_read.close();
    return last_seen_id;

# stores the last id that we index over
def store_last_seen_id(last_seen_id,file_name):
    f_write = open(file_name,"w");
    f_write.write(str(last_seen_id));
    f_write.close();
    return

def replyToTweet():
    print("retrieving tweet");

    last_seen_id = retrieve_last_seen_id(file_name);
    mentions = api.mentions_timeline(last_seen_id, tweet_mode = "extended")

    #cycle through mentions
    for mention in reversed(mentions): # we reverse to see the first tweet to the last
        print(str(mention.id) + " - " + mention.full_text);
        last_seen_id = mention.id;
        store_last_seen_id(last_seen_id, file_name);

        if "#tweetbot" in mention.full_text.lower():
            print("found \nresponding back...");
            api.update_status("@" + mention.user.screen_name + " this is a test", last_seen_id); # sends a new tweet reponding to ones with the #tweetbot string

#continuously checks for if a new tweet comes out
while True:
    replyToTweet()
    time.sleep(15)


