import discord
from discord.ext import commands
import os

os.system("cls")

if os.path.exists("setup.py"):
    os.remove("setup.py")
if os.path.exists("runsetup.bat"):
    os.remove("runsetup.bat")

print("\u001b[36mThis bot has been created by the automated bot creator!\n\u001b[31mAll credit of this bot maker goes to Aram Brunton\u001b[0m")
print("\u001b[31mTo use the Kick and Ban Command you will require to have a role called Staff\u001b[0m")

client = commands.Bot(command_prefix = "PrefixHere")

# command template
# @client.command
# async def *command*(ctx):
#    command = str("""```*command text*```""")
#    embed = discord.Embed(title="*Title Of Command*", colour=*colour*)
#    embed.add_field(name = "*extra text*")
#    await ctx.send(embed=embed)

@client.event
async def on_ready():
    print("Bot is \u001b[32mOnline!")

@client.command()
async def ip(ctx):
    command = str("""```Server IP ServerIPHere```""")
    embed = discord.Embed(title="Server IP", colour=0x002EFF)
    embed.add_field(name ="Here is our server IP!", value=command)
    await ctx.send(embed=embed)

# Kick command
@client.command()
@commands.has_role('Staff')
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Hello {ctx.author.name}, {member.name} Has been Kicked from the server!")

# Ban command
@client.command()
@commands.has_role('Staff')
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Hello {ctx.author.name}, {member.name} Has been Banned from the server!")

client.run('BotTokenHere')