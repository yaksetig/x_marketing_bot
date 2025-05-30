# Twitter Marketing Bot

A simple CLI-based Twitter that:

- Generates a tweet using OpenAI's GPT-3.5-turbo.
- Posts it to Twitter via the Tweepy client.
- Sleeps for 24 hours, then repeats.

Keep the script running on your CLI, and it will automatically post one marketing tweet per day.

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yaksetig/x_marketing_bot.git
   cd x_marketing_bot

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   
3. Create a .env file
   ```bash
   cp .env.example .env

5. (Optional) Customize the tweet prompt by editing the PROMPT variable in .env

## Usage

Run the bot:

   ```bash
   chmod +x daily_bot.py
   ./daily_bot.py

