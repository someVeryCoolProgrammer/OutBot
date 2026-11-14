# pyright: reportCallIssue=false

from unittest.mock import AsyncMock, Mock

import discord
import pytest

from commands import ModerationCommands


@pytest.mark.asyncio
async def test_moderation_commands_ban(monkeypatch: pytest.MonkeyPatch) -> None:
    """Tests the command /mod ban."""
    monkeypatch.setattr(
        "commands.mod_cg.send_censor_word_warning",
        AsyncMock(return_value=False),
    )

    command = ModerationCommands(Mock())
    interaction = Mock()
    interaction.response.defer = AsyncMock()
    interaction.followup.send = AsyncMock()
    interaction.user = Mock()

    user = Mock()
    guild = Mock()
    guild.owner_id = 3
    guild.ban = AsyncMock()
    interaction.guild = guild

    reason = "This is a test"

    await command.ban.callback(command, interaction, user, reason)

    interaction.response.defer.assert_awaited_once_with(ephemeral=True)
    guild.ban.assert_awaited_once_with(user, reason=reason)
    interaction.followup.send.assert_awaited_once_with(
        f"User: {user} was banned by {interaction.user} because of {reason}.",
        ephemeral=True,
    )


@pytest.mark.asyncio
async def test_moderation_commands_ban_censored(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Tests /mod ban with a censored reason."""
    monkeypatch.setattr(
        "commands.mod_cg.send_censor_word_warning",
        AsyncMock(return_value=True),
    )

    command = ModerationCommands(Mock())
    interaction = Mock()
    interaction.response.defer = AsyncMock()
    interaction.followup.send = AsyncMock()

    guild = Mock()
    guild.ban = AsyncMock()
    interaction.guild = guild

    await command.ban.callback(command, interaction, Mock(), "This is a test")

    interaction.response.defer.assert_awaited_once_with(ephemeral=True)
    guild.ban.assert_not_awaited()
    interaction.followup.send.assert_not_awaited()


@pytest.mark.asyncio
async def test_moderation_commands_ban_in_dm(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Tests /mod ban when used in DMs."""
    monkeypatch.setattr(
        "commands.mod_cg.send_censor_word_warning",
        AsyncMock(return_value=False),
    )

    command = ModerationCommands(Mock())
    interaction = Mock()
    interaction.response.defer = AsyncMock()
    interaction.followup.send = AsyncMock()
    interaction.guild = None

    await command.ban.callback(command, interaction, Mock(), "This is a test")

    interaction.followup.send.assert_awaited_once_with(
        "This command cannot be used in DMs.",
        ephemeral=True,
    )


@pytest.mark.asyncio
async def test_moderation_commands_kick(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Tests the command /mod kick."""
    monkeypatch.setattr(
        "commands.mod_cg.send_censor_word_warning",
        AsyncMock(return_value=False),
    )

    command = ModerationCommands(Mock())
    interaction = Mock()
    interaction.response.defer = AsyncMock()
    interaction.followup.send = AsyncMock()
    interaction.user = Mock()

    user = Mock()
    guild = Mock()
    guild.owner_id = 3
    guild.kick = AsyncMock()
    interaction.guild = guild

    reason = "This is a test"

    await command.kick.callback(command, interaction, user, reason)

    interaction.response.defer.assert_awaited_once_with(ephemeral=True)
    guild.kick.assert_awaited_once_with(user, reason=reason)
    interaction.followup.send.assert_awaited_once_with(
        f"User: {user} was kicked by {interaction.user} because of {reason}.",
        ephemeral=True,
    )


@pytest.mark.asyncio
async def test_moderation_commands_kick_censored(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Tests /mod kick with a censored reason."""
    monkeypatch.setattr(
        "commands.mod_cg.send_censor_word_warning",
        AsyncMock(return_value=True),
    )

    command = ModerationCommands(Mock())
    interaction = Mock()
    interaction.response.defer = AsyncMock()
    interaction.followup.send = AsyncMock()

    guild = Mock()
    guild.kick = AsyncMock()
    interaction.guild = guild

    await command.kick.callback(command, interaction, Mock(), "This is a test")

    interaction.response.defer.assert_awaited_once_with(ephemeral=True)
    guild.kick.assert_not_awaited()
    interaction.followup.send.assert_not_awaited()


@pytest.mark.asyncio
async def test_moderation_commands_kick_in_dm(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Tests /mod kick when used in DMs."""
    monkeypatch.setattr(
        "commands.mod_cg.send_censor_word_warning",
        AsyncMock(return_value=False),
    )

    command = ModerationCommands(Mock())
    interaction = Mock()
    interaction.response.defer = AsyncMock()
    interaction.followup.send = AsyncMock()
    interaction.guild = None

    await command.kick.callback(command, interaction, Mock(), "This is a test")

    interaction.followup.send.assert_awaited_once_with(
        "This command cannot be used in DMs.",
        ephemeral=True,
    )


@pytest.mark.asyncio
async def test_moderation_commands_unban(monkeypatch: pytest.MonkeyPatch) -> None:
    """Tests the command /mod unban."""
    monkeypatch.setattr(
        "commands.mod_cg.send_censor_word_warning",
        AsyncMock(return_value=False),
    )

    command = ModerationCommands(Mock())
    interaction = Mock()
    interaction.response.defer = AsyncMock()
    interaction.followup.send = AsyncMock()
    interaction.user = Mock()

    user = Mock()
    guild = Mock()
    guild.ban = AsyncMock()
    interaction.guild = guild

    reason = "This is a test"

    await command.unban.callback(command, interaction, user, reason)

    interaction.response.defer.assert_awaited_once_with(ephemeral=True)
    guild.ban.assert_awaited_once_with(user, reason=reason)
    interaction.followup.send.assert_awaited_once_with(
        f"User: {user} was unbanned by {interaction.user} because of {reason}.",
        ephemeral=True,
    )


@pytest.mark.asyncio
async def test_moderation_commands_unban_censored(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Tests /mod unban with a censored reason."""
    monkeypatch.setattr(
        "commands.mod_cg.send_censor_word_warning",
        AsyncMock(return_value=True),
    )

    command = ModerationCommands(Mock())
    interaction = Mock()
    interaction.response.defer = AsyncMock()
    interaction.followup.send = AsyncMock()

    guild = Mock()
    guild.ban = AsyncMock()
    interaction.guild = guild

    await command.unban.callback(command, interaction, Mock(), "This is a test")

    guild.ban.assert_not_awaited()
    interaction.followup.send.assert_not_awaited()


@pytest.mark.asyncio
async def test_moderation_commands_unban_in_dm(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Tests /mod unban when used in DMs."""
    monkeypatch.setattr(
        "commands.mod_cg.send_censor_word_warning",
        AsyncMock(return_value=False),
    )

    command = ModerationCommands(Mock())
    interaction = Mock()
    interaction.response.defer = AsyncMock()
    interaction.followup.send = AsyncMock()
    interaction.guild = None

    await command.unban.callback(command, interaction, Mock(), "This is a test")

    interaction.followup.send.assert_awaited_once_with(
        "This command cannot be used in DMs.",
        ephemeral=True,
    )


@pytest.mark.asyncio
async def test_moderation_commands_unban_not_found(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Tests /mod unban when the user cannot be found."""
    monkeypatch.setattr(
        "commands.mod_cg.send_censor_word_warning",
        AsyncMock(return_value=False),
    )

    command = ModerationCommands(Mock())
    interaction = Mock()
    interaction.response.defer = AsyncMock()
    interaction.followup.send = AsyncMock()

    user = Mock()
    guild = Mock()
    guild.ban = AsyncMock(
        side_effect=discord.NotFound(
            Mock(status=404, reason="Not Found"),
            "Not found",
        )
    )
    interaction.guild = guild

    await command.unban.callback(command, interaction, user, "This is a test")

    guild.ban.assert_awaited_once_with(user, reason="This is a test")
    interaction.followup.send.assert_awaited_once_with(
        "User not found :(",
        ephemeral=True,
    )
