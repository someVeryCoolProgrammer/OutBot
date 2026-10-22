import time

import discord

from bot import load_env_bot_token
from config.outbot_custom import custom_setup


def run_bot() -> None:
    """Runs OutBot"""
    outbot = custom_setup()
    try:
        outbot.run(load_env_bot_token(), reconnect=True)
    except discord.LoginFailure:
        raise RuntimeError(
            'Discord bot token in "config/.env" is invalid. Please set your DISCORD_TOKEN to your discord bot token. It can be found: https://discord.com/developers/home'
        )
    finally:
        print("Shutting down OutBot...")
        time.sleep(1)
        print("OutBot has shutdown successfully.")
        print("GoodBye :)")
