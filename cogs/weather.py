import discord
from discord import embeds
from discord.ext import commands
import os, asyncpraw
import requests

class weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx, message):
        ctx.send("Hello World")

async def setup(bot):
    await bot.add_cog(weather(bot))