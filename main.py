import discord
from discord.ext import commands

# 봇 토큰을 입력하세요
TOKEN = 'MTE1NzkyMzIzMjkxODI3ODE0NQ.GtAIkX.6Djr0_SymThJiu5Yt66zyLkvmybdGYSSu8T7GQ'
# 유튜브 스트리밍 채널 ID를 입력하세요
YOUTUBE_CHANNEL_ID = 'UC9TEHnMdrTEJ_Nmy1Jv2M8g'
# 디스코드 알림을 보낼 채널 ID를 입력하세요
DISCORD_CHANNEL_ID = '1157923347603144775'

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    await bot.process_commands(message)

@bot.event
async def on_member_update(before, after):
    if before.activity is None and after.activity is not None and isinstance(after.activity, discord.Streaming):
        if after.activity.platform.lower() == 'youtube' and after.activity.channel_id == YOUTUBE_CHANNEL_ID:
            stream_url = f'https://www.youtube.com/watch?v={after.activity.twitch_name}'
            channel = bot.get_channel(DISCORD_CHANNEL_ID)
            await channel.send(f'{after.display_name}님이 방송을 시작하였습니다!\n{stream_url}')

bot.run(TOKEN)
