import asyncio

import discord
from discord import app_commands

from bot import OutBot
from utils import EMOJIS, FreeNitroButton, make_embed, send_censor_word_warning


class FunCommands(app_commands.Group):
    """Commands for user's to have fun"""

    def __init__(self) -> None:
        super().__init__(name="fun")

    @app_commands.command(
        name="freenitro",
        description="Free Nitro...",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def freenitro(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        Sends a gif to rickroll the user.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """

        await interaction.response.send_message(view=FreeNitroButton())

    @app_commands.command(name="fakeban", description="Pretend to ban a user.")
    @app_commands.describe(
        user="Who do you want to ban?",
        reason="Why would you like to ban them?",
        duration="How long will you like to ban this user for (in years)?",
        delete_messages="How many of their messages would you like to delete?",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def fakeban(
        self,
        interaction: discord.Interaction,
        user: discord.Member,
        reason: app_commands.Range[str, 15, 100],
        duration: app_commands.Range[int, 1, 1000],
        delete_messages: app_commands.Range[int, 1, 1000],
    ) -> None:
        """
        Moderation Bans a user.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            user (discord.Member): What user a moderator wants to ban.
            reason (str): What is the reason for banning them? Maximum length: 200 characters.
            duration (int): How long do they want the user to stay banned. Maximum length: Any number 1 - 1000.
            delete_messages (int): How many of their messages do they want to delete? Maximum length: Any number 1 - 1000.

        Allowed Mentions:
            Other users

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        if await send_censor_word_warning(interaction, reason):
            return

        embed_message: discord.Embed = discord.Embed(
            title=f"{user} has been banned!",
            description=f"Reason: {reason}",
            colour=discord.Colour.red(),
        )
        embed_message.add_field(
            name="Duration:",
            value=f"{user} has been banned for: {duration} years!",
        )
        embed_message.add_field(
            name="Amount of messages deleted:",
            value=f"{delete_messages} messages have been deleted that were sent by {user}.",
        )
        embed_message.set_footer(text="Uhhh, how are they still here?")

        await interaction.response.send_message(
            embed=embed_message,
        )

    @app_commands.command(
        name="poll",
        description="Create a poll.",
    )
    @app_commands.describe(
        title="What is your poll's title?",
        question="What is the question you would like to ask?",
    )
    async def poll(
        self,
        interaction: discord.Interaction,
        title: app_commands.Range[str, 5, 100],
        question: app_commands.Range[str, 10, 150],
    ) -> None:
        """
        Creates an embed with a title and a question that users can add reactions to.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            title (str): The title the user wants their embed to have. Maximum length: 100 characters.
            question (str): The question of their poll (description). Maximum length: 150 characters.

        Allowed Mentions:
            None

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        if await send_censor_word_warning(
            interaction, title
        ) or await send_censor_word_warning(interaction, question):
            return

        await interaction.response.defer()

        await interaction.followup.send(
            embed=make_embed(
                title=title, description=question, colour=discord.Colour.green()
            ),
        )

        poll_message = await interaction.original_response()

        asyncio.gather(*(poll_message.add_reaction(emoji) for emoji in EMOJIS))


def setup(bot: OutBot) -> FunCommands:
    return FunCommands()
