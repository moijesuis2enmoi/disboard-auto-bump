# Discord Bumper Bot

This project is a selfbot designed to automatically bump a Discord server at regular intervals using the Discord API.

## Installation

1. Clone this repository to your machine.
2. Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **.env File**: A `.env` file is needed for the bot to function properly. An example file, `x.env`, is included in this project.
   
   - **Step 1**: Rename `x.env` to `.env`.
   - **Step 2**: Open the `.env` file and fill in the value for the token (`TOKEN`), the guild id (`GUILD_ID`) and the channel id (`CHANNEL_ID`) with your bot’s authentication token.

2. The `.env` file should look like this:
   ```plaintext
   TOKEN= "YOUR_USER_TOKEN"
   GUILD_ID = "YOUR_GUILD_ID"
   CHANNEL_ID = "YOUR_CHANNEL_ID"
   ```

   Replace `YOUR_USER_TOKEN` with your actual bot token.

## Usage

Run the script to start the bot:
```bash
python main.py
```

The bot will automatically send a "bump" request every 2 hours (approximately).

## Disclaimer

This bot is provided for educational and informational purposes only. The creator is not responsible for any misuse or violations of Discord's Terms of Service resulting from its use. Users are solely responsible for ensuring they comply with all applicable Discord API rules, including rate limits and permissions. Use this bot at your own risk.

---

### License

This project is licensed under the MIT License.
