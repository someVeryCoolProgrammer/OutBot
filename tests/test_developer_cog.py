# pyright: reportCallIssue=false

from unittest.mock import AsyncMock, Mock

import discord
import pytest

from bot import OutBot
from cogs import DeveloperCommands, developer_id_int


@pytest.mark.asyncio
async def test_developer_commands_credit() -> None:
    """Tests the command /developer credit"""

    bot = Mock(spec=OutBot)
    developer_commands = DeveloperCommands(bot)

    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    await developer_commands.credit.callback(developer_commands, interaction)  # pyright: ignore[reportCallIssue]

    call = interaction.response.send_message.call_args
    embed_message = call.kwargs["embed"]

    assert embed_message.title == "OutBot's Contributors/Developers: "
    assert embed_message.description == (
        "'someVeryCoolProgrammer' is the only developer/s and/or contributor/s for OutBot currently!"
    )
    assert embed_message.colour == discord.Colour.red()


@pytest.mark.asyncio
async def test_developer_commands_sync() -> None:
    """Tests the command /developer sync"""

    bot = Mock(spec=OutBot)
    bot.tree = Mock()
    bot.tree.sync = AsyncMock(...)
    developer_commands = DeveloperCommands(bot)

    interaction = Mock()
    interaction.user.id = developer_id_int
    interaction.response.defer = AsyncMock()
    interaction.followup.send = AsyncMock()

    await developer_commands.sync.callback(developer_commands, interaction)  # pyright: ignore[reportCallIssue]

    interaction.response.defer.assert_awaited_once_with(ephemeral=True)
    bot.tree.sync.assert_awaited_once()

    embed_message = interaction.followup.send.call_args.kwargs["embed"]

    assert embed_message.title == "Synced!"
    assert embed_message.description == ("0 slash command groups have been synced.")
    assert embed_message.colour == discord.Colour.green()


@pytest.mark.asyncio
async def test_developer_commands_sync_unauthorized() -> None:
    """Tests the command /developer sync with an unauthorized user"""

    bot = Mock(spec=OutBot)
    bot.tree = Mock()
    bot.tree.sync = AsyncMock()
    developer_commands = DeveloperCommands(bot)

    interaction = Mock()
    interaction.user.id = -1
    interaction.response.send_message = AsyncMock()

    await developer_commands.sync.callback(developer_commands, interaction)  # pyright: ignore[reportCallIssue]

    bot.tree.sync.assert_not_awaited()

    embed_message = interaction.response.send_message.call_args.kwargs["embed"]

    assert embed_message.title == "You cannot use this command!"
    assert embed_message.description == ("Hmmm, you do not look like a developer...")
    assert embed_message.colour == discord.Colour.red()
    interaction.response.send_message.assert_awaited_once_with(
        embed=embed_message, ephemeral=True
    )
