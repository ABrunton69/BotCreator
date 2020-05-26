import discord 
from discord.ext import commands
import os 

os.system("cls")


print("\u001b[36;1mWelcome to a FiveM bot, I will take you through a few steps on how to set it up\nThis bot was developed and created by Aram Brunton!\u001b[0m\n")

botToken = input("\u001b[32;1mPlease enter your bot token (Copy the token from https://discordapp.com/developers/applications and right click in this terminal): \u001b[0m")
print("\u001b[32;1mBot token entered: \u001b[0m"+botToken+"\n")

botPrefix = input("\u001b[32;1mPlease enter a prefix for your bot: \u001b[0m")
print("\u001b[32;1mPrefix set to \u001b[0m"+botPrefix+"\n")

serverIp = input("\u001b[32;1mPlease enter your server IP and port: \u001b[0m")
print("\u001b[32;1mServer IP entered: \u001b[0m"+serverIp+"\n")


endOfSetup = print("You have come to the end of the setup\na file will now be created for your server with some basic commands")

f = open("bot.py", "rt")
data = f.read()
data = data.replace('BotTokenHere', botToken)
f.close()
f = open("bot.py", "wt")
f.write(data)
f.close()

d = open("bot.py", "rt")
data2 = d.read()
data2 = data2.replace('PrefixHere', botPrefix)
d.close()
d = open("bot.py", "wt")
d.write(data2)
d.close()

a = open("bot.py", "rt")
data4 = a.read()
data4 = data4.replace('ServerIPHere', serverIp)
a.close()
a = open("bot.py", "wt")
a.write(data4)
a.close()

print("The Discord.py library will now be installed! and your bot will be launched")

installDiscordPY = os.system('pip install discord.py')

runTesting = os.system('python bot.py')





