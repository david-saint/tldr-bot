import time
import tweepy
from openai import OpenAI
from config import TWITTER_API_KEY, TWITTER_API_SECRET_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET, OPENAI_API_KEY

# Set up Twitter API authentication
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Set up OpenAI API key
client = OpenAI(api_key=OPENAI_API_KEY)

def check_mentions(api, keywords, since_id):
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if any(keyword in tweet.text.lower() for keyword in keywords):
            handle_tweet(tweet)
    return new_since_id

def handle_tweet(tweet):
    tweet_id = tweet.id
    screen_name = tweet.user.screen_name
    thread = get_thread(tweet.in_reply_to_status_id)
    summary = summarize_thread(thread)
    reply_text = f"@{screen_name} TL;DR: {summary}"
    api.update_status(status=reply_text, in_reply_to_status_id=tweet_id)

def get_thread(tweet_id):
    thread = []
    while tweet_id:
        tweet = api.get_status(tweet_id, tweet_mode='extended')
        thread.append(tweet.full_text)
        tweet_id = tweet.in_reply_to_status_id
    return thread[::-1]

def summarize_thread(thread):
    text = " ".join(thread)
    prompt = f"Summarize the following thread:\n\n{text}"
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI assistant, skilled in summarizing threads into concise and informative bullet points."},\
            {"role": "user", "content": prompt},
        ],
    )
    summary = completion.choices[0].message['content'].strip()
    return summary

if __name__ == '__main__':
    since_id = 1
    while True:
        since_id = check_mentions(api, ["@david_saint_"], since_id)
        time.sleep(10 * 60) # Check for new mentions every hour
