import discord
import random
from discord.ext import commands
from discord.commands import slash_command

ball_responses = [
        'Yes',
        'No',
        'Try Again'
    ]

class Interaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    #8Ball - Returns a random answer
    @commands.slash_command(name="8ball", guild_ids=[...])
    async def _8ball(self, ctx, question):
        
        embed = discord.Embed(title = question, description = random.choice(ball_responses))
        
        await ctx.respond(embed=embed)

    #Confession - Anonymous confession

    @commands.slash_command(name="confess", guild_ids=[...])
    async def confess(self, ctx, confession):
        
        embed = discord.Embed(title = 'Confession', description = confession, color = discord.Colour.random())
        
        embed.set_footer(text="Posted by anonymous")
        
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Interaction(bot))