import discord

PREFIX = "PREFIX"
ADMIN_ID = [000000000000000000]
TOKEN = 'TOKEN'
MAIN_CHAT_ID = 000000000000000000

###### Help Embed ######
HELP_EMBED = discord.Embed(title="BOTNAME Commands", description=f"Prefix: `{PREFIX}`")

HELP_EMBED.add_field(name="`help`",value="Sends a list of commands, duh...",inline=False)
