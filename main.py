import discord
from discord import embeds
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("!help"))
    print("Bot is ready! Welcome back {0.user}!".format(bot))

bot.remove_command("help")

bot.load_extension("cogs.reddit")
bot.load_extension("cogs.help")

bot.run(token)