import discord
from discord import embeds
from discord.ext import commands
import os
import asyncio

class clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, amount):
        await ctx.channel.purge(limit=int(amount))
        await ctx.send(f"Deleted {amount} messages")

async def setup(bot):
    await bot.add_cog(clear(bot))