import discord
from discord import app_commands

from bot import OutBot
from utils import make_embed


class CodeCommands(app_commands.Group):
    """OutBot codes small programs in various languages."""

    def __init__(self):
        super().__init__(name="code")

    @app_commands.command(
        name="hello_world",
        description="'Hello World' in the python programming language.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def hello_world(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            embed=make_embed(
                title="Hello World In The Python Programming Language",
                description=(
                    "# You can use single or double quotes\n`print('Hello, World!')`"
                ),
                colour=discord.Colour.green(),
            )
        )


def setup(bot: OutBot) -> CodeCommands:
    return CodeCommands()
