# pyright: reportCallIssue=false

from unittest.mock import AsyncMock, Mock

import discord
import pytest

from cogs import PrivacyCommands
from utils import PRIVACY_POLICY


@pytest.mark.asyncio
async def test_privacy_commands_data() -> None:
    """Tests the command /privacy data"""

    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    privacy_commands = PrivacyCommands()

    await privacy_commands.data.callback(privacy_commands, interaction)

    call = interaction.response.send_message.call_args
    embed_message = call.kwargs["embed"]

    assert embed_message.title == "🗃️ What data does OutBot collect?\n"
    assert embed_message.description == (
        "\nOutBot collects/logs **NOTHING**.\n"
        "OutBot does **NOT** keep logs. All errors are printed to console.\n" 
        f"For more information, please read: {PRIVACY_POLICY}\n"
    )
    assert embed_message.colour == discord.Colour.dark_green()
