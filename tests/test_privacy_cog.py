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
        "\nOutBot collects/logs no data about you. The only data OutBot may keep is user feedback to help improve OutBot.\n"
        "User feedback is only kept for only the amount of time it needs to be retained for.\n"
        "OutBot does keep logs and doesn't delete them. Logs are deleted manually. Logs are only used for debugging purposes. "
        "Logs do **NOT** contain information about users.\n"
        f"For more information, please read: {PRIVACY_POLICY}\n"
    )
    assert embed_message.colour == discord.Colour.dark_green()
