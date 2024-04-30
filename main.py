from message import get_chat_id
from monitor import monitor
import toml
import sys
import os

def load_config():
    absolute_path = os.path.abspath(__file__)
    config_location = os.path.dirname(absolute_path)+"\\config.toml"
    with open(config_location) as file:
        config = toml.load(file)  # Make a dict of the config values

    if not config["token"]:  # No token supplied
        sys.exit("Please enter a token in the config file")

    updated_config = False
    while not config["chat_id"]:  # Keep trying to find chat id until we get a valid one
        updated_config = True
        input("Please send a message to the Telegram bot you created. Once done, wait 1 \
            minute then press Enter. If it doesn't work, send another message then try \
            again.")
        config["chat_id"] = get_chat_id(config["token"])

    if updated_config:
        with open(config_location, "w") as file:
            toml.dump(config, file)  # Output new config (to file) with updated chat id

    return config

def main():
    config = load_config()
    monitor(config)

if __name__ == "__main__":
    main()
