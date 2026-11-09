<div align="center">
    <h1>OutBot</h1>
    <h3>Private. Secure. Reliable.</h3>
    <br>
</div>

# Table Of Contents

- [About](#about)
- [Quick Link](#quick-links)
- [Requirements](#requirements)
- [Virtual Environment](#virtual-environment)
- [Installing Dependencies](#installing-dependencies)
- [Getting A Local Copy Of OutBot](#getting-a-local-copy-of-outbot)
- [Discord Developer Portal Setup](#discord-developer-portal-setup)
- [Developer ID And Env](#developer-id-and-env)
- [Adding Your Bot To Your Apps/Servers](#adding-your-bot-to-your-appsservers)
- [Run OutBot](#run-outbot)
- [Developer notes](#developer-notes)

---

# About

OutBot is an open source, privacy respecting Discord utility bot built using **discord.py**. Most popular Discord bots are **NOT**. Open source is covered in more detail in docs/OPEN_SOURCE.md and [here](https://opensource.org/osd).

OutBot uses **NO** privileged intents nor does OutBot use **ANY GATEWAY INTENTS**. Intents will be covered in more detail in docs/INTENTS.md

OutBot has built in features such as swear word filters. 

[![OutBot's Version](https://img.shields.io/github/v/release/someVeryCoolProgrammer/OutBot)](https://github.com/someVeryCoolProgrammer/OutBot/releases/latest)

---

# Quick Links

[OutBot's TOS](https://github.com/someVeryCoolProgrammer/OutBot/blob/main/TERMS.md) | [OutBot's Privacy Policy](https://github.com/someVeryCoolProgrammer/OutBot/blob/main/PRIVACY.md) | [OutBot's Security Policy](https://github.com/someVeryCoolProgrammer/OutBot?tab=security-ov-file) | [OutBot's License](https://github.com/someVeryCoolProgrammer/OutBot/?tab=MIT-1-ov-file) | [OutBot's Invite Link Guild (Server)](https://discord.com/oauth2/authorize?client_id=1525595736706781384&scope=bot%20applications.commands) | [OutBot's Invite Link (User)](https://discord.com/oauth2/authorize?client_id=1525595736706781384&scope=applications.commands)

---

# Requirements

- [Python's Latest Version](https://www.python.org/downloads/)
- discord.py (Newest version) You can check discord.py latest version [here](https://pypi.org/project/discord.py/)
- [git](https://git-scm.com/install/)
- [make (Only if you're on windows)](https://gnuwin32.sourceforge.net/packages/make.htm)
- Text editor of your choice (eg: vscode, vscodium, nvim, etc)

---

# Virtual Environment

Windows:
```shell
makeAW
```

Activating It On Windows:
```shell
makeW
```

Linux/macOS:
```shell
makeAU
```

Activating It On Linux/macOS:
```shell
makeU
```

---

# Installing Dependencies:

Installing Dependencies On Windows
```shell
installW
```

Installing Dependencies On Linux/macOS:
```shell
installU
```

---

# Getting A Local Copy Of OutBot

```shell
git clone https://github.com/someVeryCoolProgrammer/OutBot.git
```

```shell
cd outbot
```

---

# Discord Developer Portal Setup

Head over to [Discord Developer portal](https://discord.com/developers/applications) and sign in/create an account. Click "new application". Name your bot and accept Discord's Developer TOS/Privacy Policy. 

---

# Developer Id And Env

Create a new file called config/.env and make sure it is in .gitignore. Create a variable called DISCORD_TOKEN. To get your discord bot's token. Head over to [Discord Developer Portal](https://discord.com/developers/home), click "Bot" and then click "Reset Token". Click "Yes do it to" confirm. Copy your Discord token into the file ".env". DO NOT SHARE YOUR DISCORD BOT TOKEN WITH ANYONE. IF YOU DO, YOU GIVE THEM ACCESS TO YOUR BOT.

First, create another variable called: "DEVELOPER_ID". Then, go to Discord's settings and enable developer mode. Right click on your profile and click "copy user id". Copy that user id into config/.env.

---

# Adding Your Bot To Your Apps/Servers

To add OutBot to your apps and/or servers change the placeholder in the links (YOUR_BOT_ID) to your bot's id.

```text
OutBot's Invite Link Guild (Server): https://discord.com/oauth2/authorize?client_id=YOUR_BOT_ID&scope=bot%20applications.commands
```
```text
OutBot's Invite Link (User): https://discord.com/oauth2/authorize?client_id=YOUR_BOT_ID&scope=applications.commands
```

(You get your bot's discord id the same way you got your own discord id.)

---

# Run OutBot

Run OutBot On Windows:
```shell
python -m bot
```

Run OutBot On Linux/macOS:
```shell
python3 -m bot
```

---

# Developer notes

If you fork this repo, I would greatly appreciate it if you make it clear that your project is a fork of OutBot. Thank **you** for using OutBot!
