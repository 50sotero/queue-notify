import requests
import datetime

def get_chat_id(token):
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    data = requests.get(url).json()  # Try find chat that user sent to our bot
    try:
        chat_id = data["result"][0]["message"]["chat"]["id"]  # Retrieve chat id so we can reply
    except IndexError:
        return None
    return str(chat_id)


def send_message(token, chat_id):
    message = f"""Your Solo Shuffle is ready now ({datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})"""
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)  # Send the message to the user
