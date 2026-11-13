import discord
from discord import app_commands

from bot import OutBot
from utils import TERMS_OF_SERVICE, make_embed


class RulesCommands(app_commands.Group):
    """Commands related to rules. Users can use to commands to find out rules they did not know about"""

    def __init__(self):
        super().__init__(name="rules")

    @discord.app_commands.command(
        name="outbot",
        description="OutBot's Rules!",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def outbot_rules(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        OutBot's rules.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        await interaction.response.send_message(
            embed=make_embed(
                title="📜OutBot Rules: ",
                description=(
                    "By using OutBot you agree to comply with Discord's Terms Of Service and Community Guidelines.\n"
                    f"More information is available at: {TERMS_OF_SERVICE}.\n"
                    "Breaking these rules will result in a punishment. The severity of the punishment depends on how nature and seriousness of the violation.\n"
                ),
                colour=discord.Colour.teal(),
            )
        )


def setup(bot: OutBot) -> RulesCommands:
    return RulesCommands()
