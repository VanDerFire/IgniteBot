import discord
from discord.ext import commands
from discord.commands import slash_command

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
 
    #Ban Command
    @commands.slash_command(guild_ids=[884611858512887848])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if reason == None:
            reason = "no reason provided"
        
        embed = discord.Embed(title="AzureMOD",
	description=f"**{member.mention} ha sido baneado**",
	color=discord.Colour.dark_magenta())

        embed.add_field(name='BanInfo', value=f"Reason: {reason}")
        embed.set_thumbnail(url='./icons/Forbidden/forbidden_1.png')

        await ctx.respond(embed)
        await ctx.guild.ban(member)

    #Kick Command
    @commands.slash_command(guild_ids=[884611858512887848])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if reason == None:
            reason = "no reason provided"
        await ctx.respond(f'User {member.mention} has been kicked for "{reason}"')
        await ctx.guild.kick(member)

def setup(bot):
    bot.add_cog(Moderation(bot))
