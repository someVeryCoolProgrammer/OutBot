import discord
from discord import app_commands

from bot import OutBot
from utils import PRIVACY_POLICY, make_embed


class PrivacyCommands(app_commands.Group):
    """Information about privacy (OutBot)."""

    def __init__(self):
        super().__init__(name="privacy")

    @app_commands.command(
        name="data",
        description="Information on what data OutBot retains.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def data(self, interaction: discord.Interaction) -> None:
        """
        What data does OutBot collect about you/process

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """

        await interaction.response.send_message(
            embed=make_embed(
                title="🗃️ What data does OutBot collect?\n",
                description=(
                    "\nOutBot collects/logs no data about you. The only data OutBot may keep is user feedback to help improve OutBot.\n"
                    "User feedback is only kept for only the amount of time it needs to be retained for.\n"
                    "OutBot does keep logs and doesn't delete them. Logs are deleted manually. Logs are only used for debugging purposes. "
                    "Logs do **NOT** contain information about users.\n"
                    f"For more information, please read: {PRIVACY_POLICY}\n"
                ),
                colour=discord.Colour.dark_green(),
            )
        )


def setup(bot: OutBot) -> PrivacyCommands:
    return PrivacyCommands()
