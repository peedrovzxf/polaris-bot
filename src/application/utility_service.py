import discord
from dataclasses import dataclass

class UtilityService:
    def get_server_info(self, guild: discord.Guild):
        if not guild:
            return None
        if not guild.member_count:
            return None
        if not guild.icon:
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
            if role.name == '@everyone':
                continue
            roles.append(role.mention)
        
        if not guild.owner:
            return None
        
        return ServerInfo(
            name=guild.name,
            member_count=member_count,
            bot_count=bot_count,
            icon_url=guild.icon.url,
            guild_id=guild.id,
            roles=roles,
            owner=guild.owner.name
        )

@dataclass
class ServerInfo:
    name: str
    member_count: int
    bot_count: int
    icon_url: str
    guild_id: int
    roles: list
    owner: str