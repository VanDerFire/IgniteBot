""""
FlameEngine V.0.1.0_pa-01 "Azure"- Original by VanDerFire
(C)2021 
"""
import discord
import os
import json
from discord.ext import commands

#Bot Configuration
bot = commands.Bot(activity = discord.Game(name='FlameEngine Azure'))

#Open config.json
if os.path.isfile("config.json"):
	with open("config.json") as file:
		data = json.load(file)
		#load the token
		token = data["token"]
		print("config.json loaded")
else:
    print("config.json does not exist. Create the file and try again.")

#Bot Events
@bot.event
async def on_ready():
	print('FireEngine V.0.1.0_pa_01 "Azure"')
	print(bot.user.name)
	print(bot.user.id)

#Bot Commands

#Example command
@bot.slash_command()
async def say(ctx, message):

	await ctx.send(message)

bot.run(token)