import random

import discord
from discord import app_commands

from bot import OutBot
from utils import RpsButtons, make_embed


class GamesCommands(app_commands.Group):
    """Games for users to play"""

    def __init__(self) -> None:
        super().__init__(name="games")
        self.bot_choices: list[str] = ["rock", "paper", "scissors"]

    @app_commands.command(
        name="rps", description="Play rock, paper, scissors against OutBot!"
    )
    @app_commands.checks.cooldown(1, 1, key=lambda interaction: interaction.user.id)
    async def rps(self, interaction: discord.Interaction) -> None:
        """
        Allows users to play rock, paper, scissors against OutBot

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """

        embed_message = discord.Embed(
            title="Rock, Paper, Scissors Game",
            description="Please pick one of the options below to start the game: ",
            colour=discord.Colour.green(),
        )
        embed_message.add_field(
            name="Opponent: ",
            value="You will be playing against OutBot",
            inline=True,
        )

        rps_buttons: RpsButtons = RpsButtons()

        bot_choice = random.choice(self.bot_choices)

        await interaction.response.send_message(embed=embed_message, view=rps_buttons)

        await rps_buttons.wait()

        if rps_buttons.user_choice == bot_choice:
            await interaction.followup.send(
                embed=make_embed(
                    title="||TIED||!",
                    description="gg!",
                    colour=discord.Colour.blue(),
                ),
                ephemeral=True,
            )

        elif (
            rps_buttons.user_choice == rps_buttons.ROCK
            and bot_choice == "scissors"
            or rps_buttons.user_choice == rps_buttons.SCISSORS
            and bot_choice == "paper"
            or rps_buttons.user_choice == rps_buttons.PAPER
            and bot_choice == "rock"
        ):
            await interaction.followup.send(
                embed=make_embed(
                    title="You ||WON||!",
                    description="gg!",
                    colour=discord.Colour.green(),
                ),
                ephemeral=True,
            )

        else:
            await interaction.followup.send(
                embed=make_embed(
                    title="You ||LOST||!",
                    description="gg!",
                    colour=discord.Colour.red(),
                ),
                ephemeral=True,
            )


def setup(bot: OutBot) -> GamesCommands:
    return GamesCommands()
