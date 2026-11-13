# Table Of Contents

- [Code Command Group](#code-command-group)
- [Developer Command Group](#developer-command-group)
- [Communication Command Group](#communication-command-group)
- [Information Command Group](#information-command-group)
- [Link Command Group](#link-command-group)
- [Moderation Command Group](#moderation-command-group)
- [Privacy Command Group](#privacy-command-group)
- [Rules Command Group](#rules-command-group)

# Code Command Group
OutBot codes something

Command group name = code

1) /code hello_world: Sends hello world in the python programming language 

# Communication Command Group
OutBot "talks" to the user

1) /communication hello: Says hello to the user who uses it
2) /communication dm: DMs the user
    Args:
        message (str) = The message the user wants to send themselves
        1 - 1000 Characters long
3) /communication echo: Make OutBot say something 
    Args:
        message(str) = The message the user wants OutBot to say
        1 - 750 Characters

# Developer Command Group
Commands for developers or credit people who contributed to OutBot

1) /developer credit: The people who contributed to Outbot
2) /developer sync: Sync OutBot's command tree

# Information Command Group
Information about OutBot

1) /info ping: Get OutBot's gateway latency
2) /info help: OutBot's command guide
3) /info about: What is OutBot
4) /info roadmap: OutBot's planned features

# Link Command Group 

1) /link discord: OutBot's discord server invite link
2) /link invite: OutBot's invite link
3) /link github: OutBot's GitHub repository link
4) /link policy: All of OutBot's policy links

# Moderation Command Group
Moderation commands

1) /mod ban: Moderation ban a user
    Args:
        user (disocrd.Member): The user being banned
        reason (str): Why they are getting banned
        15 - 500 Characters

2) /mod unban: Moderation unban a user
    Args:
        user (disocord.User): The user being banned
        reason (str): Why they are getting banned
    Args:
        user (disocord.Member): The user being banned
        reason (str): Why they are getting un-banned
        15 - 500 Characters

3) /mod kick: Moderation kick a user
    Args:
        user (disocord.Member): The user being kicked 
        reason (str): Why they are getting banned
    Args:
        user (disocrd.Member): The user being kicked 
        reason (str): Why they are getting kicked 
        15 - 500 Characters

# Privacy Command Group
Information about OutBot's privacy

1) /privacy data: What data does OutBot collect about you

# Rules Command Group
OutBot's rules

1) /rules outbot: OutBot's rules
