import os

from dotenv import load_dotenv


def load_env_bot_token() -> str:
    """
    Loads OutBot's discord bot token.

    Returns:
        discord_token (str | None): OutBot's discord token.
    """

    load_dotenv("config/.env")
    discord_token: str | None = os.getenv("DISCORD_TOKEN")

    if discord_token is None:
        raise RuntimeError(
            'Discord bot token in "config/.env" is invalid. Please set your DISCORD_TOKEN to your discord bot token. It can be found: https://discord.com/developers/home'
        )

    return discord_token
