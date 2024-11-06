import hashlib
import os
import random
import time
import logging
import cloudscraper
from dotenv import load_dotenv


load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

requests = cloudscraper.create_scraper()
requests.headers = {
    "Authorization": os.getenv("TOKEN"),
}

def bump():
    url = "https://discord.com/api/v9/interactions"
    payloads = {
        "type": 2,
        "application_id": "302050872383242240",
        "guild_id": os.getenv("GUILD_ID"),
        "channel_id": os.getenv("CHANNEL_ID"),
        "session_id": hashlib.md5(str(random.randint(1, 99999999999999)).encode()).hexdigest(),
        "data": {
            "version": "1051151064008769576",
            "id": "947088344167366698",
            "name": "bump",
            "type": 1,
            "options": [],
            "application_command": {
                "id": "947088344167366698",
                "type": 1,
                "application_id": "302050872383242240",
                "version": "1051151064008769576",
                "name": "bump",
                "description": "Pushes your server to the top of all your server's tags and the front page",
                "description_default": "Pushes your server to the top of all your server's tags and the front page",
                "dm_permission": True,
                "integration_types": [0],
                "global_popularity_rank": 1,
                "options": [],
                "description_localized": "Bumper ce serveur",
                "name_localized": "bump"
            },
            "attachments": []
        },
        "nonce": random.randint(1, 99999999999999),
        "analytics_location": "slash_ui"
    }
    
    try:
        r = requests.post(url, json=payloads)
        r.raise_for_status()
        logging.info(f"Request successful with status code: {r.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")

while True:
    bump()
    sleep_time = random.randint(7200, 7800)
    logging.info(f"Sleeping for {sleep_time} seconds")
    time.sleep(sleep_time)