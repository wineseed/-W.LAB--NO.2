import discord
import random
import os
d = discord.Client()
async def on_ready():
    print("login.....")



@d.event

async def on_message(message):
    if message.content.startswith("!날씨"):

         msg = message.content[4:]

         url = msg + "날씨"

         await message.channel.send("https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=" + url)

    if message.content.startswith("!검색"):

        msg2 = message.content[4:]

        await message.channel.send("입벌려 검색결과 들어간다=>" + "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=" + msg2)

    if message.content.startswith("/제작자"):

        await message.channel.send("와인씌인가.....아무튼 스트리머임")

    if message.content.startswith("!저장 NO.2"):
        global msg5
        global msg6
        msg5 = message.content[9:]
        msg6 = message.content[9:11]
        await message.channel.send(msg6 + "에" + msg5 + "가 저장되었습니다") 
    if message.content.startswith("!확인 NO.2"):
        global msg8
        msg8 = message.content[9:]
        await message.channel.send(msg8 + "의 갚:" + msg5) 
    if message.content.startswith("!삭제 NO.2"):
        msg5 = None
        await message.channel.send("갚이 삭제되었습니다") 
    

access_token = os.inviron["BOT_TOKEN"]
d.run(access_token)

