import discord
from discord import embeds
from discord.ext import commands
import os, asyncpraw
import requests

class starboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


async def setup(bot):
    await bot.add_cog(starboard(bot))