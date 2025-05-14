#!/usr/bin/env python3
import os
import time
import openai
from dotenv import load_dotenv
import tweepy

# Load environment variables from .env
load_dotenv()

# OpenAI configuration
openai.api_key = os.getenv("OPENAI_API_KEY")
PROMPT = os.getenv(
    "PROMPT",
    "Write a punchy marketing tweet about our new product launch that engages our audience and highlights key benefits."
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
    Use OpenAI's ChatCompletion to generate a marketing tweet.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a creative marketing assistant."},
            {"role": "user", "content": PROMPT}
        ],
        max_tokens=100,
        temperature=0.8
    )
    text = response.choices[0].message.content.strip()
    # Ensure tweet length <= 280 characters
    return text[:280]


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
        # Sleep for 24 hours
        time.sleep(24 * 60 * 60)
