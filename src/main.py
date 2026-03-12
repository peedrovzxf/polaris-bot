import discord
import os
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

async def main():

    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    bot = commands.Bot(command_prefix='!', intents=intents)
    
    @bot.event
    async def on_ready():
        await bot.load_extension("bot.cogs.utility")
        try:
            await bot.tree.sync()
        except discord.Forbidden:
            print("Warning: Unable to sync application commands - ensure the bot has the 'applications.commands' scope enabled.")
        await bot.tree.sync()

        if not bot.user:
            print("Bot is not logged in")
            return
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')

    token = os.getenv("TOKEN")
    if token is None:
        print("Token not found")
        return
    await bot.start(token)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass