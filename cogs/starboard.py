import discord
from discord import embeds
from discord.ext import commands
from discord.utils import get
from datetime import datetime


class starboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        server = self.bot.get_guild(payload.guild_id)
        for channel in server.channels:
            if channel.name == "starboard":
                starchannel = channel
                break
        channel = self.bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = self.bot.get_user(payload.user_id)
        if not user:
            user = await self.bot.fetch_user(payload.user_id)
        if(payload.emoji.name == "⭐"):
            embed = discord.Embed(
                    description = f"{message.author}:\n\n{message.content}\n\n**[Jump to message]({message.jump_url})**", 
                    color = discord.Color.yellow(), 
                    timestamp = datetime.now())
            embed.set_author(name = f"{user.name} starred a message", icon_url = user.avatar)
            embed.set_footer(text = f"<#{channel}>")
            await starchannel.send(embed = embed)

async def setup(bot):
    await bot.add_cog(starboard(bot))