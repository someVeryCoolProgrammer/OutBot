from .communication_cog import CommunicationCommands
from .developer_cog import DeveloperCommands
from .information_cog import InformationCommands
from .links_cog import LinksCommands
from .mod_cog import ModerationCommands
from .privacy_cog import PrivacyCommands
from .rules_cog import RulesCommands

__all__: list[str] = [
    "CommunicationCommands",
    "DeveloperCommands",
    "InformationCommands",
    "LinksCommands",
    "ModerationCommands",
    "PrivacyCommands",
    "RulesCommands",
]
