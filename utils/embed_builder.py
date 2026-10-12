import discord


def make_embed(title: str, description: str, colour: discord.Colour) -> discord.Embed:
    """
    Util function for creating embeds

    Args:
        title (str): Embed's title
        description (str): Embed's description
        colour (): Embed's colour

    Returns:
        discord.Embed
    """
    embed = discord.Embed(
        title=title,
        description=description,
        colour=colour,
    )

    return embed
