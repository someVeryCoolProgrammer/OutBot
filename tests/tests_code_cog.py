# pyright: reportCallIssue=false

from unittest.mock import AsyncMock, Mock

import discord
import pytest

from cogs import CodeCommands


@pytest.mark.asyncio
async def test_communication_commands_greet() -> None:
    """Tests /communication hello"""
    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    code_commands = CodeCommands()

    await code_commands.hello_world.callback(code_commands, interaction)

    call = interaction.response.send_message.call_args
    embed_message = call.kwargs["embed"]

    assert embed_message.title == "Hello World In The Python Programming Language"
    assert (
        embed_message.description
        == "# You can use single or double quotes\n`print('Hello, World!')`"
    )
    assert embed_message.colour == discord.Colour.green()
