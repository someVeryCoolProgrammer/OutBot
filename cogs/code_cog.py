import asyncio
import random
from typing import Final

import discord
from discord import app_commands

from bot import OutBot
from utils import make_embed


class CodeCog(app_commands.Group):
    """OutBot codes small programs in various languages."""

    def __init__(self):
        super().__init__(name="code")

    @app_commands.command(
        name="hello_world",
        description="'Hello World' in the python programming language.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def hello_world(self, interaction: discord.Interaction) -> None:
        await interaction.response.defer()
        # Bot sleeps to make it look like it is thinking.

        MAX_SLEEP_TIME: Final[float] = 5.0
        MIN_SLEEP_TIME: Final[float] = 2.5
        sleep = random.uniform(MAX_SLEEP_TIME, MIN_SLEEP_TIME)

        await asyncio.sleep(sleep)
        await interaction.followup.send(
            embed=make_embed(
                title="Hello World In The Python Programming Language",
                description=(
                    "# You can use single or double quotes\n`print('Hello, World!')`"
                ),
                colour=discord.Colour.green(),
            )
        )


def setup(bot: OutBot) -> CodeCog:
    return CodeCog()
