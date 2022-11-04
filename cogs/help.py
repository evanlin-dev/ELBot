import discord
from discord import embeds
from discord.ext import commands

botPrefix = "!"

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title="Help",
            description="This is the help command!",
            color=discord.Color.blue()
        )
        embed.add_field(name="!reddit", value="This is the reddit command!", inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(help(bot))