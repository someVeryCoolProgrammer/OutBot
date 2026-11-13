<div align="center">
    <h1>OutBot</h1>
    <h3>Private. Secure. Reliable.</h3>
    <br>
</div>

# Table Of Contents

- [About](#about)
- [Quick Link](#quick-links)
- [Requirements](#requirements)
- [Getting A Local Copy Of OutBot](#getting-a-local-copy-of-outbot)
- [Virtual Environment](#virtual-environment)
- [Installing Dependencies](#installing-dependencies)
- [Discord Developer Portal Setup](#discord-developer-portal-setup)
- [Developer ID And Env](#developer-id-and-env)
- [Adding Your Bot To Your Apps/Servers](#adding-your-bot-to-your-appsservers)
- [Run OutBot](#run-outbot)
- [Notes](#notes)

# About

OutBot is a self-hosted, open source, privacy respecting Discord general utility bot built using **discord.py**. Most popular Discord bots are **NOT**. Open source is covered in more detail in docs/OPEN_SOURCE.md and [here](https://opensource.org/osd). OutBot uses **NO** privileged intents nor does OutBot use **ANY GATEWAY INTENTS**. Intents will be covered in more detail in docs/INTENTS.md

[![OutBot's Version](https://img.shields.io/github/v/release/someVeryCoolProgrammer/OutBot)](https://github.com/someVeryCoolProgrammer/OutBot/releases/latest)

# Quick Links

[OutBot's TOS](https://github.com/someVeryCoolProgrammer/OutBot/blob/main/TERMS.md) | [OutBot's Privacy Policy](https://github.com/someVeryCoolProgrammer/OutBot/blob/main/PRIVACY.md) | [OutBot's Security Policy](https://github.com/someVeryCoolProgrammer/OutBot?tab=security-ov-file) | [OutBot's License](https://github.com/someVeryCoolProgrammer/OutBot/?tab=MIT-1-ov-file) | [OutBot's Invite Link Guild (Server)](https://discord.com/oauth2/authorize?client_id=1525595736706781384&scope=bot%20applications.commands) | [OutBot's Invite Link (User)](https://discord.com/oauth2/authorize?client_id=1525595736706781384&scope=applications.commands)

# Requirements

- [Python's >= 3.10](https://www.python.org/downloads/)
- discord.py (>= 2.71) You can check discord.py latest version [here](https://pypi.org/project/discord.py/)
- [git](https://git-scm.com/install/)
- [make (Only if you're on windows)](https://gnuwin32.sourceforge.net/packages/make.htm)
- Text editor of your choice (eg: vscode, vscodium, nvim, etc)

# Getting A Local Copy Of OutBot

```shell
git clone https://github.com/someVeryCoolProgrammer/OutBot.git
```

```shell
cd outbot
```

# Virtual Environment

Windows:
```shell
python -m venv .venv
```

Activating It On Windows:
```shell
.\.venv\Scripts\activate.ps1
```

Linux/macOS:
```shell
python3 -m venv .venv
```

Activating It On Linux/macOS:
```shell
source .venv/bin/activate
```

# Installing Dependencies:

Installing Dependencies On Windows
```shell
make installW
```

Installing Dependencies On Linux/macOS:
```shell
make installU
```

# Discord Developer Portal Setup

Head over to [Discord Developer portal](https://discord.com/developers/applications) and sign in/create an account. Click "new application". Name your bot and accept Discord's Developer TOS/Privacy Policy. 

# Developer Id And Env

Create a new file called config/.env and make sure it is in .gitignore. Create a variable called DISCORD_TOKEN. To get your discord bot's token. Head over to [Discord Developer Portal](https://discord.com/developers/home), click "Bot" and then click "Reset Token". Click "Yes do it to" confirm. Copy your Discord token into the file ".env". DO NOT SHARE YOUR DISCORD BOT TOKEN WITH ANYONE. IF YOU DO, YOU GIVE THEM ACCESS TO YOUR BOT.

First, create another variable called: "DEVELOPER_ID". Then, go to Discord's settings and enable developer mode. Right click on your profile and click "copy user id". Copy that user id into config/.env.

# Adding Your Bot To Your Apps/Servers

To add OutBot to your apps and/or servers change the placeholder in the links (YOUR_BOT_ID) to your bot's id.

```text
OutBot's Invite Link Guild (Server): https://discord.com/oauth2/authorize?client_id=YOUR_BOT_ID&scope=bot%20applications.commands
```
```text
OutBot's Invite Link (User): https://discord.com/oauth2/authorize?client_id=YOUR_BOT_ID&scope=applications.commands
```

(You get your bot's discord id the same way you got your own discord id.)

# Run OutBot

Run OutBot On Windows:
```shell
make runW
```

Run OutBot On Linux/macOS:
```shell
make runU 
```

# Notes

If you fork this repo, I would greatly appreciate it if you make it clear that your project is a fork of OutBot. 
