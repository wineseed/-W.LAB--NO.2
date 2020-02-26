import discord
import asyncio

from discord.ext import commands

app = commands.Bot(command_prefix = "!")

@app.event
async def on_ready():
    print("접속 완료")

@app.command()
async def 클(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"{amount} 만큼 삭제됨")
    await asyncio.sleep(3)
    await ctx.channel.purge(limit=1)

@app.command()
async def 서버정보(ctx):
    await ctx.send('''
가입일:2020/02/25
서버네임:닥이들
서버 위치:남한
잠수 채널:없음
서버 책임자:닥돌
봇 연구자:준영맨,인템,타나르,닥돌
봇의 수:5
연결된 서버:슈퍼준영맨
등업방법:!붙이고 등업 [자신의 정보]
''')

@app.command()
async def 역할(ctx):
    await ctx.send('''역할 종류:
DAKDOL
봇 연구자
스크림 팀
봇들
트위치 팔로워
구독자
등업 희망자
채팅정지자''')

@app.command()
async def 보안(ctx):
    await ctx.send('''보안강도:4단계
                 이메일 인증,가입 5분후,서버 가입 10분 후
                 콘텐츠 스캔 X''')
@app.command()
async def 등업(ctx):
    await ctx.send('감사합니다.관리자에게 전달되었으니 조금만 기다려주세요')

@app.command()
async def DM(ctx):
    await ctx.send('죄송합니다. 아직 연구중이니 조금만 기다려 주세요')
access_token = os.environ["BOT_TOKEN"]    
app.run('access_token')
