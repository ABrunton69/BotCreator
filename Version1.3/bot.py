import discord
from discord.ext import commands
import os

os.system("cls")

if os.path.exists("runSetup.bat"):
    os.remove("runSetup.bat")
if os.path.exists("setup.py"):
    os.remove("setup.py")

print("\u001b[36mThis bot has been created by the automated bot creator!\n\u001b[31mAll credit of this bot maker goes to Aram Brunton\u001b[0m")
print("\u001b[31mTo use the Kick and Ban Command you will require to have a role called Staff\u001b[0m")

client = commands.Bot(command_prefix = "PrefixHere")


@client.event
async def on_ready():
    print("Bot is \u001b[32mOnline!")

@client.command()
async def ip(ctx):
    command = str("""```Server IP ServerIPHere```""")
    embed = discord.Embed(title="Server IP", colour=0x002EFF)
    embed.add_field(name ="Here is our server IP!", value=command)
    await ctx.send(embed=embed)



client.run('BotTokenHere')