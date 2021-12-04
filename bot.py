""""
FireEngine V.0.1.0_pa-01 "Azure"- Original by VanDerFire
(C)2021 
"""
import discord
#import random
import os
import json
from discord.ext import commands

#Open config.json
if os.path.isfile("config.json"):
	with open("config.json") as file:
		data = json.load(file)
		#load the token
		token = data["token"]
		prefix = data["prefix"]
		print("config.json loaded")
else:
    print("config.json does not exist. Create the file and try again.")

#Bot Configuration
bot = commands.Bot(command_prefix=prefix, activity = discord.Game(name='FlameEngine Azure'))

#Bot Events
@bot.event
async def on_ready():
	print('FireEngine V.0.1.0_pa_01 "Azure"')
	print(bot.user.name)
	print(bot.user.id)

#Bot Commands

#Example command
@bot.slash_command(guild_ids=[...]) #Put here the IDs of the servers where you want the bot to run, this can be omitted, but keep in mind that new commands may take up to an hour to be registered (This applies to all slash-type commands, including cogs)
async def say(ctx, message):

	await ctx.respond(message)

bot.load_extension('cogs.Moderation')
bot.load_extension('cogs.Interaction')
bot.run(token)