# pyright: reportCallIssue=false

from unittest.mock import AsyncMock, Mock

import discord
import pytest

from cogs import RulesCommands
from utils import TERMS_OF_SERVICE


@pytest.mark.asyncio
async def test_rules_commands_outbot_rules() -> None:
    """Tests the command /rules outbot"""

    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    rules_commands = RulesCommands()

    await rules_commands.outbot_rules.callback(rules_commands, interaction)

    call = interaction.response.send_message.call_args
    embed_message = call.kwargs["embed"]

    assert embed_message.title == "📜OutBot Rules: "
    assert embed_message.description == (
        "By using OutBot you agree to comply with Discord's Terms Of Service and Community Guidelines.\n"
        f"More information is available at: {TERMS_OF_SERVICE}.\n"
        "Breaking these rules will result in a punishment. The severity of the punishment depends on how nature and seriousness of the violation.\n"
    )
    assert embed_message.colour == discord.Colour.teal()
