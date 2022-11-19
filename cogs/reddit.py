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
userAgent = os.getenv("USER_AGENT")

class reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = asyncpraw.Reddit(
                       client_id = clientId, 
                       client_secret = clientSecret, 
                       username = username, 
                       password = password,
                       user_agent = userAgent)

        self.reddit.read_only = True

    @commands.command()
    async def top(self, ctx, sub):
        posts = await self.reddit.subreddit(sub, fetch=True)
        async for post in posts.top(limit=10):
            embed = discord.Embed(
                title=post.title,
                url="https://www.reddit.com"+post.permalink,
                description=post.author,
                color=discord.Color.blue()
            )
            embed.set_footer(text="⬆ "+str(post.ups)+" ⬇"+str(post.downs))
            embed.set_image(url=post.url)
            await ctx.send(embed=embed)
            
    @commands.command()
    async def random(self, ctx, sub):
        posts = await self.reddit.subreddit(sub, fetch=True)
        post = random.choice([post async for post in posts.hot(limit=25)])
        embed = discord.Embed(
            title=post.title,
            url="https://www.reddit.com"+post.permalink,
            description=post.author,
            color=discord.Color.blue()
        )
        embed.set_footer(text="⬆"+str(post.ups)+" ⬇"+str(post.downs))
        embed.set_image(url=post.url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def meme(self, ctx):
        posts = await self.reddit.subreddit("memes", fetch=True)
        post = random.choice([post async for post in posts.hot(limit=25)])
        embed = discord.Embed(
            title=post.title,
            url="https://www.reddit.com"+post.permalink,
            description="Posted by u/"+post.author,
            color=discord.Color.blue(),
        )
        embed.set_footer(text="⬆ "+str(post.ups)+" ⬇"+str(post.downs))
        embed.set_image(url=post.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(reddit(bot))