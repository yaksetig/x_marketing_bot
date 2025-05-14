#!/usr/bin/env python3
import os
import time
from dotenv import load_dotenv
from openai import OpenAI
import tweepy

load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT = os.getenv(
    "PROMPT",
    "Write a single original marketing tweet of up to 280 characters in a professional yet modern tone. Call out the pain of time-wasting captchas and bot-fighting boredom, then highlight how GotCHA’s gameplay makes verification fast, fun, and frustration-free. The output should not have any quotation marks. Make sure your tweets are very original and not generic since they can never repeated."

)

# Twitter API credentials
TW_API_KEY = os.getenv("TW_API_KEY")
TW_API_SECRET = os.getenv("TW_API_SECRET")
TW_ACCESS_TOKEN = os.getenv("TW_ACCESS_TOKEN")
TW_ACCESS_SECRET = os.getenv("TW_ACCESS_SECRET")
TW_BEARER_TOKEN = os.getenv("TW_BEARER_TOKEN")

# Initialize Tweepy client
twitter_client = tweepy.Client(
    bearer_token=TW_BEARER_TOKEN,
    consumer_key=TW_API_KEY,
    consumer_secret=TW_API_SECRET,
    access_token=TW_ACCESS_TOKEN,
    access_token_secret=TW_ACCESS_SECRET,
    wait_on_rate_limit=True
)


def generate_marketing_tweet():
    """
    Generate a marketing tweet using OpenAI.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are the Chief Marketing Officer of GotCHA (Games Orchestrated to Tell Computers and Humans Apart), a company that turns dull CAPTCHAs into quick, engaging mini-games."},
            {"role": "user", "content": PROMPT}
        ],
        max_tokens=100,
        temperature=0.8
    )
    text = response.choices[0].message.content.strip()
    return text[:280]  # Ensure max length


def post_to_twitter(text: str):
    """
    Post the text to Twitter using Tweepy.
    """
    twitter_client.create_tweet(text=text)
    print(f"Posted tweet: {text}")


if __name__ == "__main__":
    while True:
        try:
            tweet = generate_marketing_tweet()
            post_to_twitter(tweet)
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(24 * 60 * 60)  # Sleep for 24 hours
