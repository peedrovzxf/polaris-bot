from dataclasses import dataclass

import discord


@dataclass
class ServerInfo:
    name: str
    member_count: int
    bot_count: int
    guild_id: int
    roles: list[str]
    owner: str


class UtilityService:
    def get_server_info(self, guild: discord.Guild) -> ServerInfo | None:
        if not guild:
            return None
        if not guild.member_count:
            return None
        if not guild.owner:
            return None

        bot_count = 0
        member_count = 0
        for member in guild.members:
            if member.bot:
                bot_count += 1
            else:
                member_count += 1

        roles = []
        for role in guild.roles:
            if role.name == "@everyone":
                continue
            roles.append(role.mention)

        return ServerInfo(
            name=guild.name,
            member_count=member_count,
            bot_count=bot_count,
            guild_id=guild.id,
            roles=roles,
            owner=guild.owner.name,
        )
