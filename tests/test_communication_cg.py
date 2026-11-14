# pyright: reportCallIssue=false

from unittest.mock import AsyncMock, Mock

import discord
import pytest

from commands import CommunicationCommands


@pytest.mark.asyncio
async def test_communication_commands_greet() -> None:
    """Tests /communication greet"""
    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    communication_commands = CommunicationCommands()

    await communication_commands.greet.callback(communication_commands, interaction)

    interaction.response.send_message.assert_awaited_once_with("Hello!")


@pytest.mark.asyncio
async def test_communication_commands_dm(monkeypatch) -> None:
    """Tests /communication dm"""
    monkeypatch.setattr(
        "commands.communication_cg.send_censor_word_warning",
        AsyncMock(return_value=False),
    )

    interaction = Mock()
    interaction.user.send = AsyncMock()
    interaction.response.send_message = AsyncMock()
    interaction.followup.send = AsyncMock()

    communication_commands = CommunicationCommands()

    await communication_commands.dm.callback(
        communication_commands, interaction, "Hello!"
    )

    interaction.user.send.assert_awaited_once()

    interaction.response.send_message.assert_awaited_once_with(
        "DM has been sent!", ephemeral=True
    )

    interaction.followup.send.assert_awaited_once_with(
        "Attempted to send DM.", ephemeral=True
    )


@pytest.mark.asyncio
async def test_communication_commands_dm_forbidden(monkeypatch) -> None:
    """Tests /communication dm when DMs are disabled"""
    monkeypatch.setattr(
        "commands.communication_cg.send_censor_word_warning",
        AsyncMock(return_value=False),
    )

    interaction = Mock()
    interaction.user.send = AsyncMock(
        side_effect=discord.Forbidden(Mock(), "Forbidden")
    )
    interaction.response.send_message = AsyncMock()
    interaction.followup.send = AsyncMock()

    communication_commands = CommunicationCommands()

    await communication_commands.dm.callback(
        communication_commands, interaction, "Hello!"
    )

    interaction.response.send_message.assert_awaited_once_with(
        "I could not send you a DM. This may be because you have them turned off. Please try turning them on and try again.",
        ephemeral=True,
    )

    interaction.followup.send.assert_awaited_once_with(
        "Attempted to send DM.", ephemeral=True
    )


@pytest.mark.asyncio
async def test_communication_commands_dm_censored(monkeypatch) -> None:
    """Tests /communication dm with a censored message"""
    monkeypatch.setattr(
        "commands.communication_cg.send_censor_word_warning",
        AsyncMock(return_value=True),
    )

    interaction = Mock()
    interaction.user.send = AsyncMock()
    interaction.response.send_message = AsyncMock()
    interaction.followup.send = AsyncMock()

    communication_commands = CommunicationCommands()

    await communication_commands.dm.callback(
        communication_commands, interaction, "Censored message"
    )

    interaction.user.send.assert_not_awaited()
    interaction.response.send_message.assert_not_awaited()
    interaction.followup.send.assert_not_awaited()


@pytest.mark.asyncio
async def test_communication_commands_echo(monkeypatch) -> None:
    """Tests /communication echo"""
    monkeypatch.setattr(
        "commands.communication_cg.send_censor_word_warning",
        AsyncMock(return_value=False),
    )

    interaction = Mock()
    interaction.user = "TestUser"
    interaction.response.send_message = AsyncMock()

    communication_commands = CommunicationCommands()

    await communication_commands.echo.callback(
        communication_commands, interaction, "Hello!"
    )

    embed_message = interaction.response.send_message.call_args.kwargs["embed"]

    assert embed_message.title == "TestUser has said: "
    assert embed_message.description == "Hello!"
    assert embed_message.colour == discord.Colour.green()


@pytest.mark.asyncio
async def test_communication_commands_echo_censored(monkeypatch) -> None:
    """Tests /communication echo with a censored message"""
    monkeypatch.setattr(
        "commands.communication_cg.send_censor_word_warning",
        AsyncMock(return_value=True),
    )

    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    communication_commands = CommunicationCommands()

    await communication_commands.echo.callback(
        communication_commands, interaction, "Censored message"
    )

    interaction.response.send_message.assert_not_awaited()
