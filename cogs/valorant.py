import discord
from discord import embeds
from discord.ext import commands
import os, asyncpraw
import requests

response = requests.get("https://valorant-api.com/v1/agents?isPlayableCharacter=true")
data = response.json()["data"]
agents = {}
for i in data:
    color = i["backgroundGradientColors"][0]
    agents[i["displayName"]] = [i["uuid"], i["displayName"], i["description"], i["displayIcon"], i["bustPortrait"], i["fullPortrait"], i["role"]["displayName"], i["role"]["description"], i["role"]["displayIcon"], color[2:]]

class valorant(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def agent(self, ctx, agent):
        agent = agent.capitalize()
        if agent in agents:
            embed = discord.Embed(
                title=agents[agent][1] + " - " + agents[agent][6],
                description=agents[agent][2],
                color=discord.Color.from_str("#"+agents[agent][9])
            )
            embed.set_image(url=agents[agent][4])
            embed.set_thumbnail(url=agents[agent][3])
            await ctx.send(embed=embed)
        else:
            await ctx.send("Agent not found")

async def setup(bot):
    await bot.add_cog(valorant(bot))