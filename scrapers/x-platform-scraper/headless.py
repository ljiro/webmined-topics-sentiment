from dotenv import load_dotenv
import os
from Scweet.scweet import Scweet

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials from environment variables
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# Initialize Scweet with login
scweet = Scweet(
    cookies=None,
    cookies_path='cookies',
    user_agent=None,
    env_path='.env',
    disable_images=True,
    headless=False
)

# Scrape tweets
tweets = scweet.scrape(
    since="2025-01-01",   # Jan 2025
    until="2025-09-17",   # today
    words=[
        "Trump",
        "Donald Trump",
        "Trump administration",
        "Trump executive order",
        "Trump policy",
        "Trump directive",
        "Trump rollback",
        "Trump immigration",
        "Trump border security",
        "Trump DEI",
        "Trump gender policy",
        "Trump environment",
        "Trump climate",
        "Trump conservation",
        "Trump foreign policy",
        "Trump global health",
        "Trump lawsuit",
        "Trump court ruling"
    ],
    lang="en",               # English tweets
    limit=100000,
    save_dir="outputs",
    custom_csv_name="trump_tweets_2025.csv",
)

print(f"Scraped {len(tweets)} tweets")
