import discord
from discord import app_commands
from discord.ext import commands

class UtilityCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name="ping", description="Ping the bot")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("Pong!")

async def setup(bot: commands.Bot):
    await bot.add_cog(UtilityCog(bot))
