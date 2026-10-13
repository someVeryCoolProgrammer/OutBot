# pyright: reportCallIssue=false

from unittest.mock import AsyncMock, Mock

import pytest

from cogs import CommunicationCommands


@pytest.mark.asyncio
async def test_general_commands_greet() -> None:
    """Tests /link discord"""
    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    communication_commands = CommunicationCommands()

    await communication_commands.greet.callback(communication_commands, interaction)

    interaction.response.send_message.assert_awaited_once_with("Hello!")
