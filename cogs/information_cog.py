import discord
from discord import app_commands

from bot import OutBot
from utils import (
    BOT_VERSION,
    GITHUB_LINK,
    OUTBOT_INVITE_LINK,
    OUTBOT_LICENSE,
    PRIVACY_POLICY,
    TERMS_OF_SERVICE,
    make_embed,
)


class InformationCommands(app_commands.Group):
    """Information about OutBot/OutMyth."""

    def __init__(self, bot: OutBot) -> None:
        super().__init__(name="info")
        self.bot: OutBot = bot

    @app_commands.command(
        name="ping",
        description="Click a magical button that displays Outbot's ping.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def ping(self, interaction: discord.Interaction) -> None:
        """
        Sends Outbot's ping when a button is clicked.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        gateway_latency: int = round(self.bot.latency * 1000)

        await interaction.response.send_message(
            embed=make_embed(
                title="Pong 🏓!",
                description=f"OutBot's gateway latency: `{gateway_latency}`ms!",
                colour=discord.Colour.green(),
            ),
            ephemeral=True,
        )

    @app_commands.command(
        name="help",
        description="OutBot's Command Guide",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def help(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        OutBot's command guide.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """

        await interaction.response.send_message(
            embed=make_embed(
                title="📋 OutBot's Command List: \n",
                description=(
                    "\n# </> Code Commands: \n"
                    "- **`/code hello_world`**\n"
                    "\n# 💻 Developer Commands: \n"
                    "- **`/developer devs`**\n"
                    "- **`/developer sync`**\n"
                    "#\n 🗣️ Communication Commands: \n"
                    "- **`/communication hello`**\n"
                    "- **`/communication dm`**\n"
                    "- **`/communication echo`**\n"
                    "#\n 🧠 Information Commands: \n"
                    "- **`/info ping`**\n"
                    "- **`/info help`**\n"
                    "- **`/info about`**\n"
                    "- **`/info roadmap`**\n"
                    "#\n 🔗 Link Commands: \n"
                    "- **`/link discord`**\n"
                    "- **`/link invite`**\n"
                    "- **`/link github`**\n"
                    "- **`/link policy`**\n"
                    "#\n 🛡️ Mod Commands: \n"
                    "- **`/mod ban`**\n"
                    "- **`/mod kick`**\n"
                    "#\n 🔐 Privacy Commands: \n"
                    "- **`/privacy data`**\n"
                    "#\n ⚖️ Rules Commands: \n"
                    "- **`/rules outbot`**\n"
                ),
                colour=discord.Colour.blurple(),
            )
        )

    @app_commands.command(
        name="about",
        description="Useful Information About OutBot!",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def about(self, interaction: discord.Interaction) -> None:
        """
        General information about OutBot.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        embed_message: discord.Embed = discord.Embed(
            title="About: ",
            description=(
                "Outbot is a general utility bot that takes user privacy and security seriously.\n"
                "Most discord bots do not. OutBot is a general purpose utility bot.\n"
                f"- Outbot's Version: v{BOT_VERSION}\n"
                f"OutBot's sourse code is available at: {GITHUB_LINK} under {OUTBOT_LICENSE}\n"
                f"{OUTBOT_INVITE_LINK}\n"
                f"{PRIVACY_POLICY}\n"
                f"{TERMS_OF_SERVICE}\n"
            ),
            colour=discord.Colour.blurple(),
        )
        embed_message.set_footer(
            text="OutBot was made with python using discord.py.",
        )

        await interaction.response.send_message(embed=embed_message)

    @app_commands.command(
        name="roadmap",
        description="Planned Features For OutBot!",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def roadmap(self, interaction: discord.Interaction) -> None:
        """
        Features OutBot will get in future updates.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        embed_message: discord.Embed = discord.Embed(
            title="OutBot's Planned Features: ",
            description=(
                "# User: \n"
                "- ||🛠️|| More interactive and fun commands for users\n"
                "- ||🛠️|| Add better way to report.\n"
                "- ||❌️|| Host Outbot's privacy policy and terms of service on a website.\n"
                "\n# Code quality: \n"
                "- ||🛠️|| More tests and clearer docs.\n"
                "- ||❌️|| Add ymal files to .github.\n"
                "- ||✅|| More robust code.\n"
            ),
            colour=discord.Colour.green(),
        )
        embed_message.add_field(
            name="Key: ",
            value="✅ = Feature completed - 🛠️ = In development - ❌️ = Did not started to working on feature",
            inline=True,
        )
        await interaction.response.send_message(embed=embed_message)


def setup(bot: OutBot) -> InformationCommands:
    return InformationCommands(bot)
