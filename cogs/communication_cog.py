import discord
from discord import app_commands

from bot import OutBot
from utils import make_embed, send_censor_word_warning


class CommunicationCommands(app_commands.Group):
    """Commands that 'talk' to the user"""

    def __init__(self):
        super().__init__(name="communication")

    @app_commands.command(
        name="greet",
        description="OutBot greets you!",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def greet(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        OutBot greets you.

        Args:
            interaction (discord.Interaction): The discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        await interaction.response.send_message("Hello!")

    @app_commands.command(
        name="dm",
        description="OutBot DMs you. This command requires your DMs to be turned on.",
    )
    @app_commands.describe(message="What would you like OutBot to DM you?")
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def dm(
        self,
        interaction: discord.Interaction,
        message: app_commands.Range[str, 1, 1000],
    ) -> None:
        """
        DM the user

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            message (str): The message the user wants to be DMed by OutBot. Maximum length: 1000 characters.

        Allowed Mentions:
            None

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        if await send_censor_word_warning(interaction, message):
            return

        try:
            await interaction.user.send(
                embed=make_embed(
                    title="You have a special message by ||yourself||!",
                    description=f"||{message}||",
                    colour=discord.Colour.green(),
                )
            )

        except discord.Forbidden:
            await interaction.response.send_message(
                "I could not send you a DM. This may be because you have them turned off. Please try turning them on and try again.",
                ephemeral=True,
            )

        else:
            await interaction.response.send_message(
                "DM has been sent!",
                ephemeral=True,
            )

        finally:
            await interaction.followup.send(
                "Attempted to send DM.",
                ephemeral=True,
            )

    @app_commands.command(
        name="echo",
        description="Make OutBot say a specific message!",
    )
    @app_commands.describe(message="What would you like OutBot to say?")
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def echo(
        self,
        interaction: discord.Interaction,
        message: app_commands.Range[str, 1, 750],
    ) -> None:
        """
        Says what the user passed in.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            message (str): What the user wants OutBot to say. Maximum length: 750 characters.

        Allowed Mention:
            None

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        if await send_censor_word_warning(interaction, message):
            return

        await interaction.response.send_message(
            embed=make_embed(
                title=f"{interaction.user} has said: ",
                description=message,
                colour=discord.Colour.green(),
            ),
        )


def setup(bot: OutBot) -> CommunicationCommands:
    return CommunicationCommands()
