import discord
from discord import embeds
from discord.ext import commands
import os, asyncpraw
from datetime import datetime

class logger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        print(message.guild_id)
        try:
            server = self.bot.get_guild(message.guild_id)
            for channel in server.channels:
                if channel.name == "logs":
                    logs = channel
                    break
            embed = discord.Embed(
                description = f"{message.author}:\n\n{message.content}",
                color = discord.Color.red(),
                timestamp = datetime.now())
            embed.set_author(name = f"{message.author} sent a message", icon_url = message.author.avatar)
            embed.set_footer(text = f"<#{message.channel}>")
            await logs.send(embed = embed)
        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(logger(bot))