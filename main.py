import discord
from discord import embeds
from discord.ext import commands
import os
import asyncio

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("!help"))
    print("Bot is ready! Welcome back {0.user}!".format(bot))

bot.remove_command("help")
async def main():
    async with bot:
        await bot.load_extension("cogs.reddit")
        await bot.load_extension("cogs.help")
        await bot.load_extension("cogs.valorant")
        await bot.load_extension("cogs.logger")
        await bot.load_extension("cogs.weather")
        await bot.load_extension("cogs.starboard")
        await bot.load_extension("cogs.clear")

        await bot.start(os.getenv("TOKEN"))

asyncio.run(main())