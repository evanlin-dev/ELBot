import discord
from discord import embeds
from discord.ext import commands
import random, os, asyncpraw
from dotenv import load_dotenv

load_dotenv()
clientId = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
userAgent = {"User-Agent": "ELBot"}
reddit = asyncpraw.Reddit(
    client_id=clientId, 
    client_secret=clientSecret, 
    user_agent=userAgent, 
    username=username, 
    password=password)

class reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reddit(self, ctx):
        subreddit = await reddit.subreddit(ctx)
        hotPosts = subreddit.top(limit=10)
        for post in hotPosts:
            await ctx.send(f"Found post: {post['data']['title']}")

def setup(bot):
    bot.add_cog(reddit(bot))