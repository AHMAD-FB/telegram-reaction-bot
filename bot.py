import requests
import random
from flask import Flask, request

app = Flask(__name__)

# List of bot tokens
BOT_TOKENS = [
    "7860467798:AAGkMGQt4JZ5UCRPYeiZiB7u3xkSp-OLffk",
    "7617468749:AAHnlNx1jZgTeNjHewEbx2f_kWV_DoAuToY"
]

# Emoji reactions list
EMOJIS = ["🤤", "🤯", "🥰", "🔥", "😘", "🆒", "👍", "⚡", "👏", "😍"]

def send_reaction(bot_token, chat_id, message_id):
    """Send a random emoji reaction using a bot token."""
    emoji = random.choice(EMOJIS)
    url = f"https://api.telegram.org/bot{bot_token}/setMessageReaction"

    data = {
        "chat_id": chat_id,
        "message_id": message_id,
        "reaction": [{"type": "emoji", "emoji": emoji}],
        "is_big": False
    }

    response = requests.post(url, json=data)
    print(response.json())  # Debugging

@app.route("/", methods=["GET"])
def home():
    return "Bot is running with multiple tokens!"

@app.route("/webhook", methods=["POST"])
def webhook():
    """Handle incoming Telegram updates and react using random bots."""
    update = request.json

    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        message_id = update["message"]["message_id"]

        # Pick a random bot token to send the reaction
        bot_token = random.choice(BOT_TOKENS)
        send_reaction(bot_token, chat_id, message_id)

    return "OK", 200

if __name__ == "__main__":
    # Run the Flask app on Railway
    app.run(host="0.0.0.0", port=5000)
