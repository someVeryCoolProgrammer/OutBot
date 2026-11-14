import importlib
from pathlib import Path

import discord
from discord import app_commands

from .errors import on_app_command_error


class OutBot(discord.Client):
    """Loads cogs."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tree = app_commands.CommandTree(self)
        self.tree.on_error = on_app_command_error

    async def setup_hook(self) -> None:
        """Loads all cogs and syncs all commands to the command tree"""

        commands_path = Path("commands")

        for command in commands_path.glob("*_cg.py"):
            module_name = command.stem

            module = importlib.import_module(f"commands.{module_name}")

            if hasattr(module, "setup"):
                self.tree.add_command(module.setup(self))
