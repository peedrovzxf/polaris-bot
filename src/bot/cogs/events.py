from discord.ext import commands


class EventsCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.bot.user:
            return
        banner = f"""
        ★ Polaris
✦ Bot is ready as {self.bot.user}
✦ Servers: {len(self.bot.guilds)}
✦ User ID: {self.bot.user.id}
        """
        print("\033[0m" + "-" * 40)

        print(self.gradient(banner.strip(), (255, 255, 255), (120, 170, 255)))
        print("\033[0m" + "-" * 40)

    def gradient(self, text: str, start_color: tuple, end_color: tuple):
        r1, g1, b1 = start_color
        r2, g2, b2 = end_color

        steps = max(len(text) - 1, 1)
        result = ""

        for i, char in enumerate(text):
            r = int(r1 + (r2 - r1) * (i / steps))
            g = int(g1 + (g2 - g1) * (i / steps))
            b = int(b1 + (b2 - b1) * (i / steps))

            result += f"\033[1;38;2;{r};{g};{b}m{char}"

        return result + "\033[0m"


async def setup(bot: commands.Bot):
    await bot.add_cog(EventsCog(bot))
