<div align="center">
    <h1>OutBot</h1>
    <h3>Private. Secure. Reliable.</h3>
    <br>
</div>

# Table Of Contents

- [About](#about)
- [Quick Link](#quick-links)
- [Requirements](#requrirements)
- [Windows](#installing-dependencies-on-windows)
- [Linux/macOS](#installing-dependencies-on-linuxmacos)
- [Getting A Local Copy Of OutBot](#getting-a-local-copy-of-outbot)
- [Virtual Environment](#creating-a-virtual-environment)
- [Windows Virtual Environment](#windows-virtual-environment)
- [Linux/macOS Virtual Environment](#linuxmacos-virtual-environment)
- [Discord Bot Token](#discord-bot-token)
- [Discord Developer Portal Setup](#discord-developer-portal-setup)
- [Creating .env](#creating-env)
- [Adding Your Bot To Your Apps/Servers](#adding-your-bot-to-your-appsservers)
- [Changing Developer Id](#changing-developer-id)
- [Run OutBot](#run-outbot)
- [Inviting OutBot To Your Apps/Discord Servers](#inviting-outbot-to-your-appsdiscord-servers)
- [Developer notes](#developer-notes)

---

# About

OutBot is an open source, privacy respecting Discord utility bot built using **discord.py**. **OutBot is 100% open source**. Most popular Discord bots are **NOT** open source. Open source is covered in more detail [here](https://opensource.org/osd).

OutBot uses **NO** privileged intents. OutBot does **NOT** use **ANY GATEWAY INTENTS**. Intents will be covered in more detail [here](#intents).

[![OutBot's Version](https://img.shields.io/github/v/release/someVeryCoolProgrammer/OutBot)](https://github.com/someVeryCoolProgrammer/OutBot/releases/latest)

---

# Quick Links

[OutBot's TOS](https://github.com/someVeryCoolProgrammer/OutBot/blob/main/TERMS.md) | [OutBot's Privacy Policy](https://github.com/someVeryCoolProgrammer/OutBot/blob/main/PRIVACY.md) | [OutBot's Security Policy](https://github.com/someVeryCoolProgrammer/OutBot?tab=security-ov-file) | [OutBot's License](https://github.com/someVeryCoolProgrammer/OutBot/?tab=MIT-1-ov-file) | [OutBot's Invite Link Guild (Server)](https://discord.com/oauth2/authorize?client_id=1525595736706781384&scope=bot%20applications.commands) | [OutBot's Invite Link (User)](https://discord.com/oauth2/authorize?client_id=1525595736706781384&scope=applications.commands)

---

# Requirements

- [Python's Latest Version](https://www.python.org/downloads/)
- discord.py (Newest version) You can check discord.py latest version [here](https://pypi.org/project/discord.py/)
- [git](https://git-scm.com/install/) 

# Installing Dependencies On Windows:

You have to install this to allow OutBot to work:
```shell
pip install -r requirements/core.txt
```

If you want to use ruff and cloc:
```shell
pip install -r requirements/developer.txt
```

If you want to use tests:
```shell
pip install -r requirements/tests.txt
```

# Installing Dependencies On Linux/macOS:

You have to install this to allow OutBot to work:
```shell
pip3 install -r requirements/core.txt
```

If you want to use ruff and cloc use:
```shell
pip3 install -r requirements/developer.txt
```

If you want to use tests:
```shell
pip3 install -r requirements/tests.txt
```

# Getting A Local Copy Of OutBot

```shell
git clone https://github.com/someVeryCoolProgrammer/OutBot.git
```

```shell
cd outbot
```

# Windows Virtual Environment

Windows:
```shell
python -m venv .venv
```

Activating it:
Windows:
```shell
.venv\Scripts\Activate.ps1
```

# Linux/macOS Virtual Environment

Linux/macOS:
```shell
python3 -m venv .venv
```

```shell
source .venv/bin/activate
```

# Discord Bot Token

You now have a local copy of OutBot on your computer. For OutBot to actually run, we will need a Discord Bot Token. 
DO NOT SHARE YOUR DISCORD BOT TOKEN WITH ANYONE. IF YOU DO, YOU GIVE THEM ACCESS TO YOUR BOT. THEY CAN EVEN FIND YOUR EMAIL WITH IT.

# Discord Developer Portal Setup

Head over to [Discord Developer portal](https://discord.com/developers/applications) and sign in/create an account. Click "new application". Name your bot and accept Discord's Developer TOS/Privacy Policy. 

# Creating .env

Create a new file called config/.env and make sure it is in .gitignore. Create a variable called DISCORD_TOKEN. To get your discord bot's token. Head over to [Discord Developer Portal](https://discord.com/developers/home), click "Bot" and then click "Reset Token". Click "Yes do it to" confirm. Copy your Discord token into the file ".env".

# Adding Your Bot To Your Apps/Servers

To add OutBot to your apps and/or servers change the placeholder in the links to your bots id.

```text
OutBot's Invite Link Guild (Server): https://discord.com/oauth2/authorize?client_id=YOUR_BOT_ID&scope=bot%20applications.commands
OutBot's Invite Link (User): https://discord.com/oauth2/authorize?client_id=YOUR_BOT_ID&scope=applications.commands
```

To get your bots id, head over to [discord developer portal](https://discord.com/developers) and log in with your discord account. Now click on your application and your bot id should be after application. Eg: https://discord.com/developers/applications/YOUR_BOT_ID  

# Changing Developer Id

There is one final thing we need to do and that is to change the developer id. By default it is set to OutBot's developers. By keeping it that way, you will **NOT** be able to sync OutBot's command tree. Go to Discord's settings and enable developer mode. Right click on your profile and click "copy user id". Copy that user id into config/.env (the same file with your disocrd token).  

# Run OutBot On Windows
```shell
python -m bot
```

# Run OutBot On Linux/macOS
```shell
python3 -m bot
```

To invite OutBot to your server(s)/add it to your apps, head over to this link:

[OutBot's Invite Link](https://discord.com/oauth2/authorize?client_id=1525595736706781384&scope=bot%20applications.commands)

Then choose if you want OutBot to your Discord server(s) or to your apps.

---

# Developer notes

To report any issues (other than security vulnerabilities) please open a GitHub issue, a ticket on OutMyth, or use /report.  
Before reporting a security issue please read [OutBot's Security Policy](https://github.com/abdfjakshduwiyernm123/OutBot?tab=security-ov-file).  
Thank **you** for using OutBot! ❤️
