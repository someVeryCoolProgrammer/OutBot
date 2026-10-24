# Table Of Contents

- [What Are Intents?](#what-are-intents)
- [What Intents Does OutBot Use?](#what-intents-does-outbot-use)

# What Are Intents?

There are two types of intents. Privileged intents and regular intents. Think of an intent as a way of the bot to "subscribe" to specific events (information). OutBot uses no intents at all because it does not need any. This may change in the future.
```py
intents = discord.Intents.none()
```

Discord always has something going on. A member gets banned, a member goes offline, a member sends a message etc. That information does not go to your bot. Intents are a way to tell discord what to send your bot. For example "message content privileged intent" is used when your bot needs command prefixes. This is because your bot needs to know if a message starts with your given command prefix with your command name (there are more uses to "message content privileged intent" prefix commands are probably the most common). 

A privileged intent is an intent that is more sensitive or potentially less private than regular intents. There are three privileged intents which are covered below. These need to be enabled in the Discord Developer Portal and requested by your bot in code. Non-privileged intents can be enabled by:  
```py
intents = discord.Intents.default()  # Enables all default non-privileged intents.
```

You can disable specific gateway intents by:  
```py
intents.guilds = False  # Disables guild intent.
```

To disable all non-privileged gateway intents 
```py
intents = discord.Intents.none()  # Disables all default non-privileged gateway intents.
```

---

# What Intents Does OutBot Use?

| Name | Privileged | What Does It Do? | Enabled |
| --- | --- | --- | --- |
| Member Intent | Yes | Receives member join, leave, and update information | No |
| Message Content Intent | Yes | Allows the bot to read message content | No |
| Presence Intent | Yes | Receives member activity and status updates | No |
| Guilds Intent | No | Receives guild/server-related events | No |
| Ban Intent | No | Receives information when users are banned or unbanned | No |
| Emoji Intent | No | Receives emoji/sticker creation, update, and deletion events | No |
| Integrations Intent | No | Receives integration-related events | No |
| Webhook Intent | No | Receives webhook creation, update, and deletion events | No |
| Invite Intent | No | Receives invite creation and deletion events | No |
| Voice States Intent | No | Receives voice state updates, such as users joining or leaving voice channels | No |
| Messages Intent | No | Receives message creation, update, and deletion events in guilds | No |
| Reactions Intent | No | Receives reaction add and removal events on messages | No |
| Typing Intent | No | Receives typing events in guild channels | No |
| DM Messages Intent | No | Receives message events in direct messages | No |
| DM Reactions Intent | No | Receives reaction events in direct messages | No |
| DM Typing Intent | No | Receives typing events in direct messages | No |

