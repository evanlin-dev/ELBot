import discord
from discord import embeds
from discord.ext import commands
import os, asyncpraw

class logger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx, message):
        await ctx.send(f"{message.author} said {message.content}")


async def setup(bot):
    await bot.add_cog(logger(bot))