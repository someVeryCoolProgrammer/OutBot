# 8/11/'26

## 1.0.0

After 3months and 27days, OutBot is finally done! OutBot will know receive less frequent updates. OutBot will still receive them, just not as frequent as it was. OutBot was come a very long way since its first update on the 12th of July.

### Added:

- Updated all docstrings so they are more descriptive
- Improved /roadmap
- Added clickable links to all documentation
- Updated /ping to give OutBot's gateway latency instead of pinging the user
- New commands: (/links github and /code hello_world, /mod ban, /mod kick, /mod unban)
- Added more accurate type hints
- Created command groups
- Added a better warning to .env.example
- Set OutBot's status to idle
- Added custom activity to OutBot
- Created a guild and user invite link for OutBot
- Grouped security policy, privacy policy, contributing policy, and terms into one command called /links policy
- Created FUNDING.yml
- Wrote tests for all commands
- Added workflows

### Renamed:

- utility command ---> general
- /privacy ---> privacy_information
- /developers devs ---> /developer credit
- outmythrules ---> outbot
- /privacy privacy_information ---> /privacy guide
- response_check_error_handling ---> error_handling_response_check
- cencor_words.py ---> profanity.py
- outbot_custom_setup.py ---> outbot_custom.py
- run_outbot.py ---> run.py
- bot_info.py ---> constants.py
- general command group ---> talk command group
- main.py ---> dunder main.py
- error_handling.py ---> errors.py
- moderation command group ---> mod command group
- /rules outbotrules ---> /rules outbot
- /privacy privacy_information ---> /privacy info
- Architecture:
- Moved /ping from general cog to information cog
- Moved main.py into the "bot" directory
- Removed all gateway intents
- Shifted from commands.Bot to discord.Client
- Cogs are loaded with pathlib

### Code:

- Removed button when /info ping is used
- Made directory, file, function, and variable names shorter
- Improved error messages
- De-bloated README.md
- Moved some bits of README.md into separate files under the docs directory
- Fixed all typos

### Removed:

- Removed dytest from test.txt
- Removed all OutMyth branding
- Deleted command /privacy guide because it was the same as /privacy data
- Removed fun_cog, support_cog, and games_cog
- Removed command /outmythrules

# 1/11/'26

## 0.5.19

- Fixed /mod unabn not working. The "user" param was type-hinted as "discord.Member". This caused the bot to raise an error because the banned user was not a member of the guild it was used it. The correct type hint would be "discord.User",

# 31st October 2026

## Update 0.5.18

- Fixed bug: Added ephemeral=True for mod commands confirmation message

# 31st October 2026

## Update 0.5.17

- Fixed bug: docstring said the test for /communication greet tested /links discord

# 30th October 2026

## Update 0.5.16

- Fixed /code hello_world not having cooldown

# 26th October 2026

## Update 0.5.15

Fixed bugs:
- code hello_world not working
- Re-added ephemeral for command invoke error (I accidentally removed it)
- embed=make_embed() for /code hello_world

# 12th October 2026

## Update 0.5.14

- **Removed print when /games rps is used. (I forgot to remove it)**

# OutBot Bug Fix - 2nd October 2026

## Update 0.5.13

- **Fixed developer_id not being thrown away when converted from a string to an int**

# OutBot Bug Fix - 27 September 2026

## Update 0.5.12

- **Fixed /sync not working**

# OutBot Bug Fix - 25 September 2026

## Update 0.5.11

- **Fixed rate limit message not being sent**

# OutBot Bug Fix - 25 September 2026

## Update 0.5.10

- **Fixed discord developer id not being able to be none**

# OutBot Bug Fix - 22 September 2026

## Update 0.5.9

- **Fixed "bot is not defined" in the command /ping**

# OutBot Bug Fix - 19 September 2026

## Update 0.5.8

- **discord.user.id ---> interaction user.id**

---

# OutBot Bug Fix - 16 September 2026

## Update 0.5.7

- **Fixed unexpected error handling**
- **Fixed undifined ephemeral in rate limit error handling**
- **interaction.followup.send_message ---> interaction.followup.send**

---

# OutBot Bug Fix - 12 September 2026

## Update 0.5.6

- **Fixed /sync not working**

---

# OutBot Bug Fix - 12 September 2026

## Update 0.5.5

- **Fixed rate limit not working**

---

# OutBot Bug Fix - 12 September 2026

## Update 0.5.4

- **Fixed undefined name PingUserButton and type hint OutBot**
- **Added "bitch" to censor words**
- **Command prefix set to null terminator**

---

# OutBot Bug Fix - 11 September 2026

# Update 0.5.3

**Fixed import bug**

---

# OutBot Bug Fix - 10 September 2026

## Update 0.5.2

**Fixed messages not getting send because of allowed mentions**

---

# OutBot Bug Fix - 9 September 2026

## Version 0.5.1

**Fixed tests not working.**

---

# OutBot Update - 9 September 2026

## Version 0.5.0

### Added

- **type hints**
- **.gitignore**
- **Improved documentation**
- **All commands are inside cogs**
- **Centralized error handling**
- **Improved code readability**
- **Updated all commands and commands quality**
- **Added an MIT License, contributing, code of conduct, tos, privacy policy, and security to OutBot's repository**
- **New commands**
- **Improved ux and added buttons to the commands /ping and /freenitro**
- **Created a test for /developer**
- **Custom logger**
- **Logs that delete themselves daily**

### Renamed

- **/rickroll ---> /freenitro**
- **/outbot ---> /about**
- **/say ---> /echo**
- **/serverlink ---> /discord**
- **/hello ---> /greet**

### Removed

- **/outmyth and /outhis**
- **Removed most try except blocks and replaced it with error handling**
- **Commands pinging you every time you invoke them except /ping**
- **6 poll reactions**
- **ephemeral for /echo**

---

# OutBot - Update - 28th July 2026

## **Version 0.4**

- **New slash commands**
- **Removed all prefix commands**
- **Improved readability**
- **All typos fixed**
- **Bugs Patched**
- **Log mode | w ---> a**
- **Removed /outhis command**
- **Error handling for /dm and /say**
- **14 new poll reactions**
- **Better command names**
- **Checks if token is none**

---

# Update 0.3

## **OutBot - Update - 22nd July 2026**

### **Version 0.3**

- **Slash commands added.** (/obhelp or do !obhelp)
- **New prefixes:** !, ?, -,  =,  ;
- **Logging change | a ---> w**
- **Prefix reply command now replies with:** Hello <@mention>! How are you!
- **Bug fixes**
- **Typos fixed**
- **Removed censor filter**
- **More readable comments**
- **Better command names**
- **More readable code**
- **Description change**

---

# OutBot - Update - 19th July 2026

### **Version 0.2**

- **Name change** Outmyth Ai ---> OutBot
- **Description added**
- **Command Prefix is**  '/' (**Update 0.3 will add !**)
- **Swear word filter** 
- **Bot Commands Added** - /hello ,/outmyth ,/outmyth_history ,/dm /poll ,/bot_help. updates. If you want to know what each command does, type /help
- **All bot commands work in the bot's Dms.**

---

# OutBot - Update - 12th July 2026

## **Version: 0.1**

- **Responds when /outmyth is used.**
