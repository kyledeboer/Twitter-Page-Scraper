import json
import csv
import tweepy
import re

def findWholeWord(word):
    return re.compile(r'\b({0})\b'.format(word), flags=re.IGNORECASE).search

def numberOfPositiveWords(tweet):
    x= positive_words.split(" ")
    count=0
    for word in x:
        if(findWholeWord(word)(tweet)):
            count+=1
    return count

def numberOfNegativeWords(tweet):
    x= negative_words.split(" ")
    count=0
    for word in x:
        if(findWholeWord(word)(tweet)):
            count+=1
    return count

def search_user(access_token, access_token_secret):
    numHappyWords =0
    numNegativeWords=0
    auth = tweepy.AppAuthHandler(access_token, access_token_secret)

    api = tweepy.API(auth)

    with open('%s.csv' % (fname), 'w', encoding='utf8') as file:
        w = csv.writer(file)
        w.writerow(['timestamp','tweet_text', 'all_hashtags', 'retweet_count', 'happy_freq', 'negative_freq'])

        for tweet in tweepy.Cursor(api.user_timeline, screen_name=fname).items(1000):
            #f=dateToNumber(tweet.created_at)

            happywords=numberOfPositiveWords(tweet.text.replace('\n',' '))
            numHappyWords+=happywords

            negativeWords=numberOfNegativeWords(tweet.text.replace('\n',' '))
            numNegativeWords+=negativeWords

            w.writerow([tweet.created_at, tweet.text.replace('\n',' '),
            [e['text'] for e in tweet._json['entities']['hashtags']], tweet.retweet_count, happywords, negativeWords])

        print("positive words per tweet is: ", (numHappyWords/1000))
        print("negative words per tweet is: ", (numNegativeWords/1000))

access_token = input("Insert Tweepy Key: ")
access_token_secret = input("Insert Key Secret:")
fname=input("Insert Twitter Page:")
positive_words= input("Insert positive words:" )
negative_words= input("Insert negative words:" )


if __name__ == '__main__':
    search_user(access_token, access_token_secret)
