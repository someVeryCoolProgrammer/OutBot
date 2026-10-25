import asyncio

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
    async def hello_world(self, interaction: discord.Interaction) -> None:
        await interaction.response.defer()
        await asyncio.sleep(5)
        await interaction.response.send_message(
            make_embed(
                title="Hello World In The Python Programming Language",
                description=(
                    "`# You can use single or double quotes``print('Hello, World!')`"
                ),
                colour=discord.Colour.green(),
            )
        )


def setup(bot: OutBot) -> CodeCog:
    return CodeCog()
