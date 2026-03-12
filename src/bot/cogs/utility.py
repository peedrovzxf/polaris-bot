import discord
from discord import app_commands
from discord.ext import commands
from application.utility_service import UtilityService

class UtilityCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name="ping", description="Ping the bot")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("Pong!")
    
    @app_commands.command(name="serverinfo", description="Get information about the server")
    async def get_server_info(self, interaction: discord.Interaction):
        await interaction.response.send_message("Getting server info...", ephemeral=True)

        guild = interaction.guild
        if not guild:
            await interaction.followup.send("You must be in a guild to use this command")
            return
        utility_service = UtilityService()
        server_info = utility_service.get_server_info(guild)

        if not server_info:
            await interaction.followup.send("Unable to get server info")
            return

        embed = discord.Embed(
            title="Server Information",
            color=discord.Color.from_rgb(0, 0, 0)
        )
        embed.add_field(name="Owner", value=server_info.owner, inline=True)
        embed.add_field(name="Name", value=server_info.name, inline=True)
        embed.add_field(name="Member Count", value=server_info.member_count, inline=True)
        embed.add_field(name="Bot Count", value=server_info.bot_count, inline=True)
        
        embed.add_field(name="Roles", value=", ".join(server_info.roles) + f" ({len(server_info.roles)})", inline=False)
        
        if not interaction.user.avatar:
            await interaction.followup.send("Unable to get user avatar")
            return
        embed.set_footer(text=f"Asked by {interaction.user.name}", icon_url=interaction.user.avatar.url)
        
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1343460842318073896/1481716543644766291/server-info-thumbnail.jpg?ex=69b45390&is=69b30210&hm=c3b7477fbf2284cbe131840b616a5f6ff0322f6cf703a06c158bd84f1f61e8f1&")
        await interaction.followup.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(UtilityCog(bot))
