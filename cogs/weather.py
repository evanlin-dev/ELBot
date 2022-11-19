import discord
from discord import embeds
from discord.ext import commands
import os, asyncpraw
import requests

class weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def weather(self, ctx, *, city):
        api_key = os.getenv("WEATHER_API_KEY")
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = city
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"Weather in {city_name}", description=weather_description, color=0x00ff00)
            embed.add_field(name="Temperature (in kelvin unit)", value=str(current_temperature), inline=False)
            embed.add_field(name="atmospheric pressure (in hPa unit)", value=str(current_pressure), inline=False)
            embed.add_field(name="humidity (in percentage)", value=str(current_humidiy), inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("City not found.")

    @commands.Cog.listener()
    async def on_message(self, ctx, message):
        ctx.send("Hello World")

async def setup(bot):
    await bot.add_cog(weather(bot))