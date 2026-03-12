import argparse
import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--deploy", action="store_true")
    args = parser.parse_args()

    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    await bot.load_extension("bot.cogs.utility")

    if args.deploy:
        try:
            print("Syncing application commands...")
            await bot.tree.sync()
            print("Application commands synced")
        except discord.Forbidden:
            print(
                "Warning: Unable to sync application commands - ensure the bot has the 'applications.commands' scope enabled."
            )

    await bot.load_extension("bot.cogs.events")

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
